"use client";

import { OrgSidebar } from "@/components/OrgSidebar";
import { useOrg } from "@/components/providers/org-provider";
import { useParams, useRouter } from "next/navigation";
import { useEffect, useState } from "react";
import { Loader2 } from "lucide-react";
import { useTheme } from "next-themes";
import Link from "next/link";
import { UserNav } from "@/components/UserNav";

export default function OrgLayout({
    children,
}: {
    children: React.ReactNode;
}) {
    const { currentOrg, switchOrg, isLoading } = useOrg();
    const params = useParams();
    const router = useRouter();
    const orgId = params.orgId as string;
    const { setTheme, theme } = useTheme();

    useEffect(() => {
        if (!isLoading) {
            if (currentOrg && currentOrg.id !== orgId) {
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
                        <UserNav />
                    </div>
                </header>
                <main className="flex-1 overflow-y-auto subtle-gradient pt-14 lg:pt-0">
                    {children}
                </main>
            </div>
        </div>
    );
}
