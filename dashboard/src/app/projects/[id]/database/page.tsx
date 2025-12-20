"use client";

import { useEffect, useState } from "react";
import { useParams, useRouter } from "next/navigation";
import { Table as TableIcon, Plus, Search, Filter, SortAsc } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Breadcrumb } from "@/components/ui/breadcrumb";
import { EmptyState } from "@/components/EmptyState";
import { Skeleton } from "@/components/ui/skeleton";
import { TableDesigner } from "@/components/TableDesigner";
import { Toaster } from "sonner";
import { cn } from "@/lib/utils";

export default function DatabasePage() {
    const params = useParams();
    const router = useRouter();
    const projectId = params.id as string;

    const [tables, setTables] = useState<any[]>([]);
    const [loading, setLoading] = useState(true);
    const [searchQuery, setSearchQuery] = useState("");
    const [showDesigner, setShowDesigner] = useState(false);

    const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

    useEffect(() => {
        fetchTables();
    }, [projectId]);

    const fetchTables = async () => {
        setLoading(true);
        try {
            const resp = await fetch(`${API_URL}/v1/projects/${projectId}/tables`);
            const data = await resp.json();
            setTables(data);
        } catch (err) {
            console.error("Failed to fetch tables", err);
        } finally {
            setLoading(false);
        }
    };

    const filteredTables = tables.filter((table) =>
        table.table_name.toLowerCase().includes(searchQuery.toLowerCase())
    );

    return (
        <div className="space-y-8 animate-in fade-in slide-in-from-bottom-4 duration-700">
            {/* Breadcrumb */}
            <Breadcrumb
                items={[
                    { label: "Overview", href: `/projects/${projectId}` },
                    { label: "Database" },
                ]}
            />

            {/* Header */}
            <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
                <div>
                    <h2 className="text-3xl font-bold tracking-tight text-gradient">Database</h2>
                    <p className="text-sm text-muted-foreground mt-1">
                        Manage your data structures and browse through your tables.
                    </p>
                </div>
                <Button
                    className="gap-2 primary-gradient shadow-lg shadow-emerald-500/20 hover:scale-105 transition-all"
                    onClick={() => setShowDesigner(true)}
                >
                    <Plus size={18} />
                    Create New Table
                </Button>
            </div>

            {/* Toolbar */}
            <div className="flex items-center gap-3">
                <div className="relative flex-1 max-w-sm">
                    <Search className="absolute left-3 top-1/2 -translate-y-1/2 text-muted-foreground" size={16} />
                    <Input
                        placeholder="Search tables..."
                        value={searchQuery}
                        onChange={(e) => setSearchQuery(e.target.value)}
                        className="pl-9 bg-card border-border/50 focus:border-primary/50"
                    />
                </div>
                <Button variant="outline" size="icon" className="text-muted-foreground">
                    <Filter size={16} />
                </Button>
                <Button variant="outline" size="icon" className="text-muted-foreground">
                    <SortAsc size={16} />
                </Button>
            </div>

            {/* Tables Grid */}
            {loading ? (
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    {[...Array(6)].map((_, i) => (
                        <div key={i} className="h-32 border border-border/40 rounded-xl bg-card/30 p-4">
                            <Skeleton className="h-6 w-1/2 mb-4" />
                            <Skeleton className="h-4 w-3/4" />
                        </div>
                    ))}
                </div>
            ) : filteredTables.length === 0 ? (
                <EmptyState
                    icon={<TableIcon size={48} className="text-muted-foreground/40" />}
                    title={searchQuery ? "No matches found" : "Your database is empty"}
                    description={
                        searchQuery
                            ? `We couldn't find any tables matching "${searchQuery}"`
                            : "Start by creating a table to store your application data."
                    }
                    action={
                        !searchQuery && (
                            <Button className="gap-2 primary-gradient" onClick={() => setShowDesigner(true)}>
                                <Plus size={16} />
                                Create Table
                            </Button>
                        )
                    }
                />
            ) : (
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    {filteredTables.map((table) => (
                        <button
                            key={table.table_name}
                            onClick={() =>
                                router.push(`/projects/${projectId}/database/${table.table_name}`)
                            }
                            className="group relative flex flex-col p-6 bg-card border border-border/40 rounded-xl hover:border-primary/40 hover:shadow-xl hover:shadow-primary/5 transition-all text-left glass"
                        >
                            <div className="flex items-start justify-between mb-4">
                                <div className="p-2.5 bg-emerald-50 dark:bg-emerald-500/10 rounded-lg group-hover:scale-110 transition-transform duration-300">
                                    <TableIcon size={22} className="text-emerald-600 dark:text-emerald-400" />
                                </div>
                                <span className="text-[10px] font-bold uppercase tracking-wider text-muted-foreground/40 px-2 py-0.5 border border-border/30 rounded-full">
                                    {table.table_type}
                                </span>
                            </div>
                            <div className="flex-1 min-w-0">
                                <h3 className="text-lg font-bold text-foreground group-hover:text-primary transition-colors truncate mb-1">
                                    {table.table_name}
                                </h3>
                                <p className="text-sm text-muted-foreground line-clamp-2">
                                    Table in public schema with base configuration.
                                </p>
                            </div>
                            <div className="mt-4 pt-4 border-t border-border/30 flex items-center justify-between text-[11px] font-medium text-muted-foreground/60">
                                <span>Updated moments ago</span>
                                <div className="flex items-center gap-1">
                                    <div className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse" />
                                    <span>Active</span>
                                </div>
                            </div>
                        </button>
                    ))}
                </div>
            )}

            {/* Table Designer Modal */}
            <TableDesigner
                open={showDesigner}
                onOpenChange={setShowDesigner}
                projectId={projectId}
                onSuccess={fetchTables}
            />

            {/* Toast Notifications */}
            <Toaster position="top-right" />
        </div>
    );
}
