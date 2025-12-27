"use client";

import { useEffect, useState } from "react";
import { useParams, useRouter } from "next/navigation";
import { Table as TableIcon, Plus, Search, Filter, SortAsc, Trash2 } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Breadcrumb } from "@/components/ui/breadcrumb";
import { EmptyState } from "@/components/EmptyState";
import { Skeleton } from "@/components/ui/skeleton";
import { TableDesigner } from "@/components/TableDesigner";
import { Toaster, toast } from "sonner";
import { cn } from "@/lib/utils";
import { Modal, ModalContent, ModalHeader, ModalTitle, ModalFooter } from "@/components/ui/modal";
import { ImportProject } from "@/components/ImportProject";

export default function DatabasePage() {
    const params = useParams();
    const router = useRouter();
    const projectId = params.id as string;

    const [tables, setTables] = useState<any[]>([]);
    const [loading, setLoading] = useState(true);
    const [searchQuery, setSearchQuery] = useState("");
    const [showDesigner, setShowDesigner] = useState(false);
    const [tableToDelete, setTableToDelete] = useState<string | null>(null);
    const [deleting, setDeleting] = useState(false);
    const [sortOrder, setSortOrder] = useState<"asc" | "desc">("asc");
    const [filterType, setFilterType] = useState<"all" | "BASE TABLE" | "VIEW">("all");

    const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

    useEffect(() => {
        fetchTables();
    }, [projectId]);

    const fetchTables = async () => {
        setLoading(true);
        try {
            const token = localStorage.getItem("token");
            const resp = await fetch(`${API_URL}/api/v1/projects/${projectId}/tables`, {
                headers: {
                    "Authorization": `Bearer ${token}`
                }
            });
            if (resp.ok) {
                const data = await resp.json();
                setTables(Array.isArray(data) ? data : []);
            } else {
                setTables([]);
            }
        } catch (err) {
            console.error("Failed to fetch tables", err);
        } finally {
            setLoading(false);
        }
    };

    const deleteTable = async () => {
        if (!tableToDelete) return;
        setDeleting(true);
        try {
            const token = localStorage.getItem("token");
            const resp = await fetch(`${API_URL}/api/v1/projects/${projectId}/sql`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${token}`
                },
                body: JSON.stringify({ sql: `DROP TABLE public."${tableToDelete}" CASCADE;` }),
            });
            const result = await resp.json();
            if (result.success !== false) {
                toast.success(`Table "${tableToDelete}" deleted`);
                fetchTables();
            } else {
                toast.error(result.error || "Failed to delete table");
            }
        } catch (err) {
            toast.error("Network error while deleting table");
        } finally {
            setDeleting(false);
            setTableToDelete(null);
        }
    };

    const toggleSort = () => {
        setSortOrder(prev => prev === "asc" ? "desc" : "asc");
    };

    const cycleFilter = () => {
        setFilterType(prev => {
            if (prev === "all") return "BASE TABLE";
            if (prev === "BASE TABLE") return "VIEW";
            return "all";
        });
    };

    const filteredTables = tables
        .filter((table) => {
            const matchesSearch = table.table_name.toLowerCase().includes(searchQuery.toLowerCase());
            const matchesFilter = filterType === "all" || table.table_type === filterType;
            return matchesSearch && matchesFilter;
        })
        .sort((a, b) => {
            const comparison = a.table_name.localeCompare(b.table_name);
            return sortOrder === "asc" ? comparison : -comparison;
        });

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
                <Button
                    variant="outline"
                    size="icon"
                    onClick={cycleFilter}
                    className={cn(
                        "text-muted-foreground",
                        filterType !== "all" && "bg-primary/10 text-primary border-primary/30"
                    )}
                    title={filterType === "all" ? "Filter: All" : `Filter: ${filterType}`}
                >
                    <Filter size={16} />
                </Button>
                <Button
                    variant="outline"
                    size="icon"
                    onClick={toggleSort}
                    className={cn(
                        "text-muted-foreground transition-transform",
                        sortOrder === "desc" && "rotate-180"
                    )}
                    title={`Sort: ${sortOrder === "asc" ? "A-Z" : "Z-A"}`}
                >
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
                        <div
                            key={table.table_name}
                            onClick={() =>
                                router.push(`/projects/${projectId}/database/${table.table_name}`)
                            }
                            onKeyDown={(e) => {
                                if (e.key === 'Enter' || e.key === ' ') {
                                    router.push(`/projects/${projectId}/database/${table.table_name}`);
                                }
                            }}
                            role="button"
                            tabIndex={0}
                            className="group relative flex flex-col p-6 bg-card border border-border/40 rounded-xl hover:border-primary/40 hover:shadow-xl hover:shadow-primary/5 transition-all text-left glass cursor-pointer outline-none focus-visible:ring-2 focus-visible:ring-primary"
                        >
                            <div className="flex items-start justify-between mb-4">
                                <div className="p-2.5 bg-emerald-50 dark:bg-emerald-500/10 rounded-lg group-hover:scale-110 transition-transform duration-300">
                                    <TableIcon size={22} className="text-emerald-600 dark:text-emerald-400" />
                                </div>
                                <div className="flex items-center gap-2">
                                    <span className="text-[10px] font-bold uppercase tracking-wider text-muted-foreground/40 px-2 py-0.5 border border-border/30 rounded-full">
                                        {table.table_type}
                                    </span>
                                    <Button
                                        variant="ghost"
                                        size="icon"
                                        onClick={(e) => {
                                            e.stopPropagation();
                                            setTableToDelete(table.table_name);
                                        }}
                                        className="h-7 w-7 text-muted-foreground hover:text-destructive hover:bg-destructive/10 opacity-0 group-hover:opacity-100 transition-all rounded-md"
                                    >
                                        <Trash2 size={14} />
                                    </Button>
                                </div>
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
                        </div>
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
            {/* Delete Confirmation Modal */}
            <Modal open={!!tableToDelete} onOpenChange={(open) => !open && setTableToDelete(null)}>
                <ModalContent className="max-w-md bg-card border-border/40 shadow-2xl glass rounded-2xl p-6">
                    <ModalHeader className="mb-4">
                        <ModalTitle className="text-xl font-bold text-destructive">Delete Table</ModalTitle>
                    </ModalHeader>
                    <div className="space-y-4">
                        <p className="text-sm text-muted-foreground">
                            Are you sure you want to delete <span className="font-mono font-bold text-foreground">"{tableToDelete}"</span>? This action cannot be undone and will delete all stored data.
                        </p>
                        <ModalFooter className="flex items-center justify-end gap-3 mt-8">
                            <Button variant="ghost" onClick={() => setTableToDelete(null)} disabled={deleting} className="rounded-xl">
                                Cancel
                            </Button>
                            <Button
                                onClick={deleteTable}
                                disabled={deleting}
                                className="bg-destructive text-destructive-foreground hover:bg-destructive/90 px-6 rounded-xl shadow-lg shadow-destructive/20"
                            >
                                {deleting ? "Deleting..." : "Delete Table"}
                            </Button>
                        </ModalFooter>
                    </div>
                </ModalContent>
            </Modal>

            {/* Import Project */}
            <div className="pt-8 border-t border-border/40">
                <h3 className="text-lg font-semibold mb-4">Database Tools</h3>
                <ImportProject projectId={projectId} onSuccess={fetchTables} />
            </div>

            {/* Toast Notifications */}
            <Toaster richColors position="top-right" />
        </div>
    );
}
