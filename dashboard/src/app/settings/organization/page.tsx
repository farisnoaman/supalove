"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { Building2, Plus, ArrowRight, ArrowLeft } from "lucide-react";
import { Button } from "@/components/ui/button";
import { toast, Toaster } from "sonner";
import { Skeleton } from "@/components/ui/skeleton";

interface Organization {
    id: string;
    name: string;
    slug: string;
    role: string;
}

export default function OrganizationsPage() {
    const [orgs, setOrgs] = useState<Organization[]>([]);
    const [loading, setLoading] = useState(true);

    const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

    useEffect(() => {
        fetchOrgs();
    }, []);

    const fetchOrgs = async () => {
        try {
            const token = localStorage.getItem("token");
            if (!token) {
                window.location.href = "/login";
                return;
            }

            const resp = await fetch(`${API_URL}/api/v1/orgs`, {
                headers: { "Authorization": `Bearer ${token}` }
            });

            if (!resp.ok) throw new Error("Failed to fetch organizations");

            const data = await resp.json();
            setOrgs(Array.isArray(data) ? data : []);
        } catch (err) {
            console.error(err);
            toast.error("Failed to load organizations");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="min-h-screen bg-background">
            <Toaster richColors position="top-right" />

            <header className="border-b border-border bg-card/50 backdrop-blur-sm sticky top-0 z-10">
                <div className="container mx-auto px-4 md:px-8 h-16 flex items-center gap-4">
                    <Link href="/projects" className="text-muted-foreground hover:text-foreground transition-colors">
                        <ArrowLeft size={20} />
                    </Link>
                    <h1 className="text-xl font-bold">Organizations</h1>
                </div>
            </header>

            <main className="container mx-auto px-4 md:px-8 py-8">
                <div className="max-w-4xl mx-auto space-y-8">
                    <div className="flex items-center justify-between">
                        <div>
                            <h2 className="text-2xl font-bold tracking-tight">Your Organizations</h2>
                            <p className="text-sm text-muted-foreground mt-1">Manage your teams and billing.</p>
                        </div>
                        <Button className="gap-2">
                            <Plus size={16} />
                            New Organization
                        </Button>
                    </div>

                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                        {loading ? (
                            [...Array(2)].map((_, i) => (
                                <Skeleton key={i} className="h-32 rounded-xl" />
                            ))
                        ) : orgs.length === 0 ? (
                            <div className="col-span-full text-center py-20 bg-card border border-border rounded-xl">
                                <Building2 className="mx-auto h-12 w-12 text-muted-foreground/50 mb-4" />
                                <h3 className="text-lg font-bold">No Organizations</h3>
                                <p className="text-muted-foreground">You are not a member of any organization.</p>
                            </div>
                        ) : (
                            orgs.map((org) => (
                                <Link
                                    key={org.id}
                                    href={`/settings/organization/${org.id}`}
                                    className="group block p-6 bg-card border border-border hover:border-primary/50 transition-all rounded-xl shadow-sm hover:shadow-md"
                                >
                                    <div className="flex justify-between items-start mb-4">
                                        <div className="p-3 bg-primary/10 rounded-lg group-hover:bg-primary/20 transition-colors">
                                            <Building2 className="text-primary" size={24} />
                                        </div>
                                        <span className="text-xs font-mono px-2 py-1 bg-muted rounded text-muted-foreground">
                                            {org.role}
                                        </span>
                                    </div>
                                    <h3 className="font-bold text-lg mb-1 group-hover:text-primary transition-colors">{org.name}</h3>
                                    <p className="text-sm text-muted-foreground font-mono mb-4">{org.slug}</p>

                                    <div className="flex items-center text-sm text-primary font-medium opacity-0 group-hover:opacity-100 transition-opacity -translate-x-2 group-hover:translate-x-0 duration-300">
                                        Manage Organization <ArrowRight size={14} className="ml-1" />
                                    </div>
                                </Link>
                            ))
                        )}
                    </div>
                </div>
            </main>
        </div>
    );
}
