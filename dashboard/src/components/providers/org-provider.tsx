"use client";

import { createContext, useContext, useEffect, useState, ReactNode } from "react";
import { useRouter, usePathname } from "next/navigation";
import { toast } from "sonner";

interface Organization {
    id: string;
    name: string;
    slug: string;
    role: string;
}

interface OrgContextType {
    orgs: Organization[];
    currentOrg: Organization | null;
    isLoading: boolean;
    refreshOrgs: () => Promise<void>;
    switchOrg: (orgId: string) => void;
}

const OrgContext = createContext<OrgContextType | undefined>(undefined);

export function OrgProvider({ children }: { children: ReactNode }) {
    const [orgs, setOrgs] = useState<Organization[]>([]);
    const [currentOrg, setCurrentOrg] = useState<Organization | null>(null);
    const [isLoading, setIsLoading] = useState(true);
    const router = useRouter();
    const pathname = usePathname();
    const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

    const fetchOrgs = async () => {
        try {
            const token = localStorage.getItem("token");
            if (!token) {
                setIsLoading(false);
                return;
            }

            const res = await fetch(`${API_URL}/api/v1/orgs`, {
                headers: { "Authorization": `Bearer ${token}` }
            });

            if (res.status === 401) {
                localStorage.removeItem("token");
                router.push("/login");
                return;
            }

            if (res.ok) {
                const data = await res.json();
                setOrgs(data);

                // Logic to set initial Org
                const storedOrgId = localStorage.getItem("last_org_id");

                if (data.length > 0) {
                    const found = data.find((o: Organization) => o.id === storedOrgId) || data[0];
                    setCurrentOrg(found);
                    if (!storedOrgId) {
                        localStorage.setItem("last_org_id", found.id);
                    }
                } else {
                    setCurrentOrg(null);
                }
            }
        } catch (error) {
            console.error("Failed to load organizations", error);
        } finally {
            setIsLoading(false);
        }
    };

    useEffect(() => {
        fetchOrgs();
    }, []);

    const switchOrg = (orgId: string) => {
        const org = orgs.find(o => o.id === orgId);
        if (org) {
            setCurrentOrg(org);
            localStorage.setItem("last_org_id", org.id);
            // Optional: redirect to org dashboard if needed, or let the current page react
            toast.success(`Switched to ${org.name}`);
        }
    };

    return (
        <OrgContext.Provider value={{ orgs, currentOrg, isLoading, refreshOrgs: fetchOrgs, switchOrg }}>
            {children}
        </OrgContext.Provider>
    );
}

export function useOrg() {
    const context = useContext(OrgContext);
    if (context === undefined) {
        throw new Error("useOrg must be used within an OrgProvider");
    }
    return context;
}
