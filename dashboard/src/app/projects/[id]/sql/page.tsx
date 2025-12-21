"use client";

import { useState } from "react";
import { useParams } from "next/navigation";
import SQLEditor from "@/components/SQLEditor";
import { Breadcrumb } from "@/components/ui/breadcrumb";
import { Terminal, Shield, Zap } from "lucide-react";
import { Toaster, toast } from "sonner";

export default function SQLPage() {
    const params = useParams();
    const projectId = params.id as string;
    const [result, setResult] = useState<any>(null);
    const [executing, setExecuting] = useState(false);

    const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

    const runQuery = async (sql: string) => {
        setExecuting(true);
        setResult(null);
        try {
            const resp = await fetch(`${API_URL}/api/v1/projects/${projectId}/sql`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ sql }),
            });
            const res = await resp.json();
            setResult(res);

            if (res.success !== false) {
                toast.success("Query executed successfully");
            } else {
                toast.error(res.error || "Query failed");
            }
        } catch (err) {
            toast.error("Network error while running query");
        } finally {
            setExecuting(false);
        }
    };

    return (
        <div className="h-full flex flex-col space-y-6 animate-in fade-in slide-in-from-bottom-4 duration-700">
            <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
                <div>
                    <Breadcrumb
                        items={[
                            { label: "Overview", href: `/projects/${projectId}` },
                            { label: "SQL Editor" },
                        ]}
                    />
                    <div className="flex items-center gap-3 mt-4">
                        <div className="p-2.5 bg-emerald-500/10 rounded-xl">
                            <Terminal size={24} className="text-emerald-500" />
                        </div>
                        <div>
                            <h2 className="text-3xl font-bold tracking-tight text-gradient">SQL Editor</h2>
                            <p className="text-sm text-muted-foreground mt-1">
                                Run raw SQL queries to manage your data, create tables, or configure RLS policies.
                            </p>
                        </div>
                    </div>
                </div>

                <div className="hidden lg:flex items-center gap-4 px-6 py-3 bg-card border border-border/40 rounded-2xl glass shadow-sm">
                    <div className="flex items-center gap-2 text-xs font-medium text-muted-foreground">
                        <Shield size={14} className="text-emerald-500" />
                        Direct Access
                    </div>
                    <div className="w-px h-4 bg-border/20" />
                    <div className="flex items-center gap-2 text-xs font-medium text-muted-foreground">
                        <Zap size={14} className="text-amber-500" />
                        V2 Performance
                    </div>
                </div>
            </div>

            <div className="flex-1 min-h-0 bg-card border border-border/40 rounded-3xl shadow-2xl glass overflow-hidden">
                <SQLEditor projectId={projectId} onExecute={runQuery} result={result} />
            </div>

            <Toaster richColors position="top-right" />

            <div className="p-4 bg-amber-500/5 border border-amber-500/10 rounded-2xl flex gap-3 text-xs text-amber-700/80 dark:text-amber-400/60 items-center">
                <Shield size={14} />
                <span>Raw SQL execution can be destructive. Please review your queries before running them.</span>
            </div>
        </div>
    );
}
