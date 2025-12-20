"use client";

import { useEffect, useState } from "react";
import { useParams, useRouter } from "next/navigation";
import { Table as TableIcon, Plus, Search } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Breadcrumb } from "@/components/ui/breadcrumb";
import { EmptyState } from "@/components/EmptyState";
import { Skeleton } from "@/components/ui/skeleton";
import { TableDesigner } from "@/components/TableDesigner";
import { Toaster } from "sonner";

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
        <div className="space-y-6">
            {/* Breadcrumb */}
            <Breadcrumb
                items={[
                    { label: "Overview", href: `/projects/${projectId}` },
                    { label: "Database" },
                ]}
            />

            {/* Header */}
            <div className="flex items-center justify-between">
                <div>
                    <h2 className="text-2xl font-bold">Database</h2>
                    <p className="text-sm text-muted-foreground">
                        View and manage the data stored in your app.
                    </p>
                </div>
                <Button className="gap-2" onClick={() => setShowDesigner(true)}>
                    <Plus size={16} />
                    New Table
                </Button>
            </div>

            {/* Search */}
            <div className="relative max-w-sm">
                <Search className="absolute left-3 top-1/2 -translate-y-1/2 text-muted-foreground" size={16} />
                <Input
                    placeholder="Search tables..."
                    value={searchQuery}
                    onChange={(e) => setSearchQuery(e.target.value)}
                    className="pl-9"
                />
            </div>

            {/* Tables Grid */}
            {loading ? (
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    {[...Array(6)].map((_, i) => (
                        <Skeleton key={i} className="h-24" />
                    ))}
                </div>
            ) : filteredTables.length === 0 ? (
                <EmptyState
                    icon={<TableIcon size={48} />}
                    title={searchQuery ? "No tables found" : "No tables found for this project"}
                    description={
                        searchQuery
                            ? `No tables match "${searchQuery}"`
                            : "Get started by creating your first table."
                    }
                    action={
                        !searchQuery && (
                            <Button className="gap-2">
                                <Plus size={16} />
                                Create Table
                            </Button>
                        )
                    }
                />
            ) : (
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    {filteredTables.map((table) => (
                        <button
                            key={table.table_name}
                            onClick={() =>
                                router.push(`/projects/${projectId}/database/${table.table_name}`)
                            }
                            className="group relative flex items-start gap-4 p-4 bg-card border border-border rounded-lg hover:border-primary/50 hover:shadow-md transition-all text-left"
                        >
                            <div className="flex-shrink-0 p-2 bg-muted rounded-md group-hover:bg-primary/10 transition-colors">
                                <TableIcon size={20} className="text-muted-foreground group-hover:text-primary transition-colors" />
                            </div>
                            <div className="flex-1 min-w-0">
                                <h3 className="font-semibold text-foreground group-hover:text-primary transition-colors truncate">
                                    {table.table_name}
                                </h3>
                                <p className="text-sm text-muted-foreground mt-1">
                                    {table.table_type}
                                </p>
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
