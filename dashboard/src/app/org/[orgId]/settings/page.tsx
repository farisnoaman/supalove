"use client";

import { useOrg } from "@/components/providers/org-provider";
import { Building2 } from "lucide-react";

export default function OrgSettingsPage() {
    const { currentOrg } = useOrg();

    if (!currentOrg) return null;

    return (
        <div className="container mx-auto px-4 md:px-8 py-8 space-y-8 animate-in fade-in duration-500">
            <div>
                <h2 className="text-2xl font-bold tracking-tight">Organization Settings</h2>
                <p className="text-sm text-muted-foreground mt-1">Manage global settings for {currentOrg.name}.</p>
            </div>

            <div className="bg-card border border-border rounded-xl p-6 space-y-4 max-w-2xl shadow-sm">
                <div className="flex items-center gap-4 border-b border-border pb-4">
                    <div className="p-3 bg-primary/10 rounded-xl">
                        <Building2 size={24} className="text-primary" />
                    </div>
                    <div>
                        <h3 className="text-lg font-bold">{currentOrg.name}</h3>
                        <p className="text-sm text-muted-foreground font-mono">{currentOrg.slug}</p>
                    </div>
                </div>

                <div className="grid grid-cols-2 gap-4">
                    <div className="space-y-1">
                        <label className="text-xs font-bold uppercase tracking-wider text-muted-foreground">Org ID</label>
                        <p className="font-mono text-sm bg-muted/50 p-2 rounded">{currentOrg.id}</p>
                    </div>
                    <div className="space-y-1">
                        <label className="text-xs font-bold uppercase tracking-wider text-muted-foreground">My Role</label>
                        <p className="font-mono text-sm bg-muted/50 p-2 rounded">{currentOrg.role}</p>
                    </div>
                </div>
            </div>
        </div>
    );
}
