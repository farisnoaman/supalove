"use client";

import { useEffect, useState } from "react";
import { useParams, useRouter } from "next/navigation";
import { Table as TableIcon, Settings, Shield, Folder, Code2, Zap, ArrowRight, Database } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Skeleton } from "@/components/ui/skeleton";
import { Badge } from "@/components/ui/badge";
import { cn } from "@/lib/utils";

export default function ProjectOverviewPage() {
    const params = useParams();
    const router = useRouter();
    const projectId = params.id as string;

    const [tables, setTables] = useState<any[]>([]);
    const [userCount, setUserCount] = useState<number | null>(null);
    const [bucketCount, setBucketCount] = useState<number | null>(null);
    const [loading, setLoading] = useState(true);

    const API_URL = (process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000").replace(/\/$/, "");

    useEffect(() => {
        fetchAllStats();
    }, [projectId]);

    const fetchAllStats = async () => {
        setLoading(true);
        try {
            await Promise.all([
                fetchTables(),
                fetchUserCount(),
                fetchBucketCount()
            ]);
        } finally {
            setLoading(false);
        }
    };

    const fetchUserCount = async () => {
        try {
            const resp = await fetch(`${API_URL}/api/v1/projects/${projectId}/auth/users`);
            const data = await resp.json();
            setUserCount(Array.isArray(data) ? data.length : 0);
        } catch (err) {
            console.error("Failed to fetch user count", err);
            setUserCount(0);
        }
    };

    const fetchBucketCount = async () => {
        try {
            const resp = await fetch(`${API_URL}/api/v1/projects/${projectId}/storage/buckets`);
            const data = await resp.json();
            setBucketCount(Array.isArray(data) ? data.length : 0);
        } catch (err) {
            console.error("Failed to fetch bucket count", err);
            setBucketCount(0);
        }
    };

    const fetchTables = async () => {
        try {
            const resp = await fetch(`${API_URL}/api/v1/projects/${projectId}/tables`);
            const data = await resp.json();
            // Fetch row counts for each table
            const tablesWithCounts = await Promise.all(
                (data || []).map(async (table: any) => {
                    try {
                        const dataResp = await fetch(
                            `${API_URL}/api/v1/projects/${projectId}/tables/${table.table_name}/data`
                        );
                        const tableData = await dataResp.json();
                        return {
                            ...table,
                            rowCount: tableData.rowCount || tableData.rows?.length || 0
                        };
                    } catch {
                        return { ...table, rowCount: 0 };
                    }
                })
            );
            setTables(tablesWithCounts);
        } catch (err) {
            console.error("Failed to fetch tables", err);
        }
    };

    const topTables = tables.slice(0, 3);

    return (
        <div className="space-y-10 animate-in fade-in slide-in-from-bottom-4 duration-700 max-w-5xl">
            {/* Hero Section */}
            <div className="relative p-5 md:p-8 rounded-2xl md:rounded-3xl bg-card border border-border/40 overflow-hidden shadow-2xl glass">
                <div className="absolute top-0 right-0 w-64 h-64 bg-primary/5 rounded-full -translate-y-1/2 translate-x-1/2 blur-3xl" />
                <div className="relative z-10 flex flex-col gap-6">
                    <div>
                        <Badge variant="outline" className="mb-4 bg-emerald-500/10 text-emerald-600 border-emerald-500/20 px-3 py-1">
                            <Zap size={12} className="mr-1.5 fill-emerald-500" />
                            Project Active
                        </Badge>
                        <h1 className="text-2xl md:text-4xl font-black tracking-tight text-gradient">Project Overview</h1>
                        <p className="text-sm md:text-base text-muted-foreground mt-2 max-w-md">
                            Manage your backend infrastructure, browse your data, and configure authentication for your application.
                        </p>
                    </div>
                    <div className="flex flex-col sm:flex-row items-stretch sm:items-center gap-3">
                        <Button variant="outline" className="border-border/50 w-full sm:w-auto">
                            <Settings size={16} className="mr-2" />
                            Settings
                        </Button>
                        <Button className="primary-gradient shadow-lg shadow-emerald-500/20 w-full sm:w-auto">
                            Go to Docs
                            <ArrowRight size={16} className="ml-2" />
                        </Button>
                    </div>
                </div>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
                {/* Database Section */}
                <div className="bg-card border border-border/40 rounded-2xl overflow-hidden shadow-sm hover:shadow-xl hover:border-primary/20 transition-all flex flex-col">
                    <div className="p-6 border-b border-border/20 flex items-center justify-between bg-muted/30">
                        <div className="flex items-center gap-3">
                            <div className="p-2 bg-emerald-50 dark:bg-emerald-500/10 rounded-lg">
                                <Database size={20} className="text-emerald-600 dark:text-emerald-400" />
                            </div>
                            <div>
                                <h2 className="text-lg font-bold">Database</h2>
                                <p className="text-[10px] text-muted-foreground uppercase tracking-widest font-bold">PostgreSQL</p>
                            </div>
                        </div>
                        <span className="text-xs font-medium px-2 py-1 bg-background border border-border/40 rounded-md">
                            {tables.length} Tables
                        </span>
                    </div>
                    <div className="p-4 flex-1">
                        {loading ? (
                            <div className="space-y-2 p-2">
                                <Skeleton className="h-10 w-full" />
                                <Skeleton className="h-10 w-full" />
                            </div>
                        ) : tables.length === 0 ? (
                            <div className="text-center py-8 text-muted-foreground text-sm italic">
                                No tables found. Create your first table.
                            </div>
                        ) : (
                            <div className="space-y-1">
                                {topTables.map((table) => (
                                    <button
                                        key={table.table_name}
                                        onClick={() =>
                                            router.push(`/projects/${projectId}/database/${table.table_name}`)
                                        }
                                        className="w-full flex items-center justify-between px-3 py-3 rounded-lg hover:bg-muted/50 transition-colors text-left group"
                                    >
                                        <div className="flex items-center gap-3">
                                            <TableIcon size={14} className="text-muted-foreground group-hover:text-primary transition-colors" />
                                            <span className="text-sm font-semibold text-foreground group-hover:text-primary transition-colors">
                                                {table.table_name}
                                            </span>
                                        </div>
                                        <div className="flex items-center gap-2">
                                            <span className="text-[10px] text-muted-foreground font-mono">
                                                {table.rowCount} rows
                                            </span>
                                            <ArrowRight size={12} className="text-muted-foreground opacity-0 group-hover:opacity-100 -translate-x-2 group-hover:translate-x-0 transition-all" />
                                        </div>
                                    </button>
                                ))}
                                {tables.length > 3 && (
                                    <button
                                        onClick={() => router.push(`/projects/${projectId}/database`)}
                                        className="w-full mt-2 py-2 text-[10px] font-bold uppercase tracking-widest text-muted-foreground hover:text-primary transition-colors text-center border-t border-border/10"
                                    >
                                        View all {tables.length} tables
                                    </button>
                                )}
                            </div>
                        )}
                    </div>
                </div>

                {/* Users / Auth Section */}
                <div className="bg-card border border-border/40 rounded-2xl overflow-hidden shadow-sm hover:shadow-xl hover:border-blue-500/20 transition-all flex flex-col">
                    <div className="p-6 border-b border-border/20 flex items-center justify-between bg-muted/30">
                        <div className="flex items-center gap-3">
                            <div className="p-2 bg-blue-50 dark:bg-blue-500/10 rounded-lg">
                                <Shield size={20} className="text-blue-600 dark:text-blue-400" />
                            </div>
                            <div>
                                <h2 className="text-lg font-bold">Authentication</h2>
                                <p className="text-[10px] text-muted-foreground uppercase tracking-widest font-bold">Keycloak OIDC</p>
                            </div>
                        </div>
                        <Badge variant="outline" className="bg-blue-50 text-blue-600 border-blue-200">
                            {loading ? "..." : userCount} Users
                        </Badge>
                    </div>
                    <div className="p-6">
                        <p className="text-sm text-muted-foreground mb-6">
                            Securely manage users, configure login providers, and handle session management.
                        </p>
                        <Button
                            variant="outline"
                            className="w-full justify-between group border-border/50"
                            onClick={() => router.push(`/projects/${projectId}/auth`)}
                        >
                            <span className="flex items-center gap-2">
                                <Shield size={14} className="text-blue-500" />
                                Manage Auth & Users
                            </span>
                            <ArrowRight size={14} className="text-muted-foreground group-hover:translate-x-1 transition-transform" />
                        </Button>
                    </div>
                </div>

                {/* Storage Section */}
                <div className="bg-card border border-border/40 rounded-2xl overflow-hidden shadow-sm hover:shadow-xl hover:border-amber-500/20 transition-all flex flex-col">
                    <div className="p-6 border-b border-border/20 flex items-center justify-between bg-muted/30">
                        <div className="flex items-center gap-3">
                            <div className="p-2 bg-amber-50 dark:bg-amber-500/10 rounded-lg">
                                <Folder size={20} className="text-amber-600 dark:text-amber-400" />
                            </div>
                            <div>
                                <h2 className="text-lg font-bold">Storage</h2>
                                <p className="text-[10px] text-muted-foreground uppercase tracking-widest font-bold">MinIO S3</p>
                            </div>
                        </div>
                        <span className="text-xs font-medium px-2 py-1 bg-background border border-border/40 rounded-md">
                            {loading ? "..." : bucketCount} {bucketCount === 1 ? 'Bucket' : 'Buckets'}
                        </span>
                    </div>
                    <div className="p-6">
                        <p className="text-sm text-muted-foreground mb-6">
                            Store and serve large files like images, videos, and documents within project-isolated buckets.
                        </p>
                        <Button
                            variant="outline"
                            className="w-full justify-center border-border/50"
                            onClick={() => router.push(`/projects/${projectId}/storage`)}
                        >
                            Open File Browser
                        </Button>
                    </div>
                </div>

                {/* Edge Functions Section */}
                <div className="bg-card border border-border/40 rounded-2xl overflow-hidden shadow-sm hover:shadow-xl hover:border-purple-500/20 transition-all flex flex-col">
                    <div className="p-6 border-b border-border/20 flex items-center justify-between bg-muted/30">
                        <div className="flex items-center gap-3">
                            <div className="p-2 bg-purple-50 dark:bg-purple-500/10 rounded-lg">
                                <Code2 size={20} className="text-purple-600 dark:text-purple-400" />
                            </div>
                            <div>
                                <h2 className="text-lg font-bold">Edge Functions</h2>
                                <p className="text-[10px] text-muted-foreground uppercase tracking-widest font-bold">Deno Runtime</p>
                            </div>
                        </div>
                        <Badge variant="secondary" className="bg-muted text-muted-foreground">Beta</Badge>
                    </div>
                    <div className="p-10 flex flex-col items-center justify-center text-center">
                        <div className="w-12 h-12 rounded-full bg-purple-50 flex items-center justify-center mb-4">
                            <Zap size={24} className="text-purple-500 fill-purple-500" />
                        </div>
                        <h3 className="text-sm font-bold">No functions deployed</h3>
                        <p className="text-[11px] text-muted-foreground mt-2 max-w-[200px]">
                            Serverless functions will appear here when you add custom logic to your app.
                        </p>
                    </div>
                </div>
            </div>
        </div>
    );
}

