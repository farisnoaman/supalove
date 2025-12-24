"use client";

import { OrgSidebar } from "@/components/OrgSidebar";
import { useOrg } from "@/components/providers/org-provider";
import { useParams, useRouter } from "next/navigation";
import { useEffect } from "react";
import { Loader2 } from "lucide-react";
import Link from "next/link";

export default function OrgLayout({
    children,
}: {
    children: React.ReactNode;
}) {
    const { currentOrg, switchOrg, isLoading } = useOrg();
    const params = useParams();
    const router = useRouter();
    const orgId = params.orgId as string;

    useEffect(() => {
        if (!isLoading) {
            if (currentOrg && currentOrg.id !== orgId) {
                // If the URL says org A but context says org B, synchronize context to URL
                // This handles deep linking
                switchOrg(orgId);
            }
        }
    }, [orgId, currentOrg, isLoading, switchOrg]);

    if (isLoading) {
        return (
            <div className="flex h-screen items-center justify-center">
                <Loader2 className="animate-spin text-muted-foreground" />
            </div>
        );
    }

    return (
        <div className="flex min-h-screen bg-background">
            <OrgSidebar />
            <div className="flex-1 flex flex-col min-w-0">
                <header className="hidden lg:flex h-14 border-b border-border bg-card/30 backdrop-blur-sm items-center px-4 md:px-8 sticky top-0 z-10 justify-end">
                    <div className="flex items-center gap-4">
                        <button
                            onClick={() => {
                                localStorage.removeItem('token');
                                window.location.href = '/';
                            }}
                            className="px-4 py-2 text-sm font-medium text-muted-foreground hover:text-foreground hover:bg-muted rounded-md transition-colors"
                        >
                            Logout
                        </button>
                        <Link
                            href="/settings/profile"
                            className="w-8 h-8 rounded-full bg-emerald-100 flex items-center justify-center text-emerald-700 text-xs font-bold ring-2 ring-emerald-500/20 hover:ring-emerald-500/50 transition-all cursor-pointer"
                            title="Profile Settings"
                        >
                            U
                        </Link>
                    </div>
                </header>
                <main className="flex-1 overflow-y-auto subtle-gradient pt-14 lg:pt-0">
                    {children}
                </main>
            </div>
        </div>
    );
}
