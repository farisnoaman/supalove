"use client";

import { useEffect, useState } from "react";
import { useParams, useRouter } from "next/navigation";
import {
    useReactTable,
    getCoreRowModel,
    getSortedRowModel,
    getPaginationRowModel,
    flexRender,
    SortingState,
    ColumnDef,
    Column,
    CellContext,
} from "@tanstack/react-table";
import {
    ArrowUpDown, Plus, Download, RefreshCw, ChevronLeft, ChevronRight,
    Settings, Table as TableIcon, Trash2, CheckSquare, Square,
    Shield, Key, FileText, Database, Lock, Unlock, Copy, Zap
} from "lucide-react";
import { Button } from "@/components/ui/button";
import { Breadcrumb } from "@/components/ui/breadcrumb";
import { Skeleton } from "@/components/ui/skeleton";
import { Badge } from "@/components/ui/badge";
import { RowEditor } from "@/components/RowEditor";
import { RLSPolicyEditor } from "@/components/RLSPolicyEditor";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { cn } from "@/lib/utils";
import { Toaster, toast } from "sonner";
import { Modal, ModalContent, ModalHeader, ModalTitle, ModalFooter } from "@/components/ui/modal";
import { AddColumnModal } from "@/components/AddColumnModal";

export default function TableDetailPage() {
    const params = useParams();
    const router = useRouter();
    const projectId = params.id as string;
    const tableName = params.table as string;

    // Data State
    const [data, setData] = useState<any[]>([]);
    const [columns, setColumns] = useState<ColumnDef<any>[]>([]);
    const [loadingData, setLoadingData] = useState(true);

    // Table State
    const [sorting, setSorting] = useState<SortingState>([]);
    const [rowCount, setRowCount] = useState(0);
    const [rowEditorOpen, setRowEditorOpen] = useState(false);
    const [rowSelection, setRowSelection] = useState({});
    const [primaryKeys, setPrimaryKeys] = useState<string[]>([]);
    const [isDeletingRows, setIsDeletingRows] = useState(false);

    // Metadata State
    const [constraints, setConstraints] = useState<any[]>([]);
    const [indexes, setIndexes] = useState<any[]>([]);
    const [policies, setPolicies] = useState<any[]>([]);
    const [loadingMeta, setLoadingMeta] = useState(true);
    const [tableSchema, setTableSchema] = useState<any[]>([]);
    const [tableSql, setTableSql] = useState("");

    // RLS State
    const [rlsEnabled, setRlsEnabled] = useState(false);
    const [showPolicyEditor, setShowPolicyEditor] = useState(false);
    const [editingPolicy, setEditingPolicy] = useState<any | null>(null);
    const [deletingPolicy, setDeletingPolicy] = useState<string | null>(null);

    // Realtime State
    const [realtimeEnabled, setRealtimeEnabled] = useState(false);
    const [isTogglingRealtime, setIsTogglingRealtime] = useState(false);

    // Modal State
    const [showDeleteTableModal, setShowDeleteTableModal] = useState(false);
    const [isDeletingTable, setIsDeletingTable] = useState(false);
    const [showAddColumnModal, setShowAddColumnModal] = useState(false);

    const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

    useEffect(() => {
        fetchTableData();
        fetchMetadata();
        fetchPolicies();
    }, [projectId, tableName]);

    const fetchTableData = async () => {
        setLoadingData(true);
        try {
            const token = localStorage.getItem("token");
            // 1. Fetch Schema to find PKs
            const schemaResp = await fetch(`${API_URL}/api/v1/projects/${projectId}/tables/${tableName}/schema`, {
                headers: { "Authorization": `Bearer ${token}` }
            });
            const schema = await schemaResp.json();
            setTableSchema(schema);

            // Generate SQL from schema
            generateTableSQL(schema);

            // Heuristic for PKs
            const pks = schema
                .filter((col: any) => col.column_name.toLowerCase() === 'id' || col.column_default?.includes('nextval'))
                .map((col: any) => col.column_name);
            setPrimaryKeys(pks);

            // 2. Fetch Data
            const resp = await fetch(
                `${API_URL}/api/v1/projects/${projectId}/tables/${tableName}/data`,
                { headers: { "Authorization": `Bearer ${token}` } }
            );
            const result = await resp.json();

            if (result.rows && result.columns) {
                setData(result.rows);
                setRowCount(result.rowCount || result.rows.length);

                const cols: ColumnDef<any>[] = result.columns.map((col: string) => ({
                    accessorKey: col,
                    header: ({ column }: { column: Column<any> }) => {
                        return (
                            <button
                                className="flex items-center gap-2 font-bold text-[11px] uppercase tracking-wider text-muted-foreground hover:text-primary transition-colors py-2"
                                onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}
                            >
                                {col}
                                {column.getIsSorted() ? (
                                    <ArrowUpDown size={12} className="text-primary" />
                                ) : (
                                    <ArrowUpDown size={12} className="opacity-30" />
                                )}
                            </button>
                        );
                    },
                    cell: (info: CellContext<any, unknown>) => {
                        const value = info.getValue();
                        if (value === null) return <span className="text-muted-foreground/40 italic font-mono text-xs">NULL</span>;
                        if (typeof value === "boolean") return (
                            <Badge variant={value ? "default" : "secondary"} className="text-[10px] h-5">
                                {value ? "true" : "false"}
                            </Badge>
                        );
                        if (typeof value === "object") return <span className="font-mono text-xs text-blue-500">{JSON.stringify(value)}</span>;
                        return <span className="text-sm line-clamp-1">{String(value)}</span>;
                    },
                }));
                setColumns(cols);
            }
        } catch (err) {
            console.error("Failed to fetch table data", err);
            toast.error("Failed to load table content");
        } finally {
            setLoadingData(false);
        }
    };

    const fetchMetadata = async () => {
        setLoadingMeta(true);
        try {
            const token = localStorage.getItem("token");
            const [constResp, idxResp] = await Promise.all([
                fetch(`${API_URL}/api/v1/projects/${projectId}/tables/${tableName}/constraints`, {
                    headers: { "Authorization": `Bearer ${token}` }
                }),
                fetch(`${API_URL}/api/v1/projects/${projectId}/tables/${tableName}/indexes`, {
                    headers: { "Authorization": `Bearer ${token}` }
                })
            ]);

            if (constResp.ok) setConstraints(await constResp.json());
            if (idxResp.ok) setIndexes(await idxResp.json());
        } catch (err) {
            console.error("Failed to fetch metadata", err);
        } finally {
            setLoadingMeta(false);
        }
    };

    const fetchPolicies = async () => {
        try {
            const token = localStorage.getItem("token");
            // Check if RLS is enabled (via pg_class/pg_tables or try to fetch policies)
            // For now, we'll infer RLS status from whether we can fetch policies successfully
            // A better way would be a dedicated endpoint for table status, but let's use what we have
            const resp = await fetch(`${API_URL}/api/v1/projects/${projectId}/tables/${tableName}/policies`, {
                headers: { "Authorization": `Bearer ${token}` }
            });
            if (resp.ok) {
                const data = await resp.json();
                setPolicies(data);
                // If we get a response, RLS is likely enabled or at least queryable
                // We really should check pg_class.relrowsecurity, but for now let's assume if we have policies, it's enabled?
                // Actually, let's look at the result. If the table has RLS enabled, we might get an empty list if no policies.

                // Let's add an explicit check endpoint or just assume it's disabled if we can't tell?
                // The backend doesn't yet expose 'is_rls_enabled'. Let's add a todo for that.
                // For now, let's default to false unless we see policies? No, that's wrong.
                // Let's just track policies. The Enable/Disable RLS buttons will explicitly set state.
            }
        } catch (err) {
            console.error("Failed to fetch policies", err);
        }
    };

    const toggleRLS = async (enable: boolean) => {
        try {
            const token = localStorage.getItem("token");
            const endpoint = enable ? 'enable' : 'disable';
            const resp = await fetch(`${API_URL}/api/v1/projects/${projectId}/tables/${tableName}/rls/${endpoint}`, {
                method: 'POST',
                headers: { "Authorization": `Bearer ${token}` }
            });

            if (resp.ok) {
                setRlsEnabled(enable);
                toast.success(`RLS ${enable ? 'enabled' : 'disabled'} for table`);
                fetchPolicies();
            } else {
                toast.error(`Failed to ${endpoint} RLS`);
            }
        } catch (err) {
            toast.error("Network error");
        }
    };

    const deletePolicy = async () => {
        if (!deletingPolicy) return;
        try {
            const token = localStorage.getItem("token");
            const resp = await fetch(`${API_URL}/api/v1/projects/${projectId}/tables/${tableName}/policies/${deletingPolicy}`, {
                method: 'DELETE',
                headers: { "Authorization": `Bearer ${token}` }
            });

            if (resp.ok) {
                toast.success("Policy deleted");
                fetchPolicies();
            } else {
                toast.error("Failed to delete policy");
            }
        } catch (err) {
            toast.error("Network error");
        } finally {
            setDeletingPolicy(null);
        }
    };

    const generateTableSQL = (schema: any[]) => {
        if (!schema || schema.length === 0) return;

        let sql = `CREATE TABLE public.${tableName} (\n`;

        schema.forEach((col: any, index: number) => {
            sql += `  ${col.column_name} ${col.data_type}`;

            if (col.character_maximum_length) {
                sql += `(${col.character_maximum_length})`;
            }

            if (col.is_nullable === 'NO') {
                sql += ' NOT NULL';
            }

            if (col.column_default) {
                sql += ` DEFAULT ${col.column_default}`;
            }

            if (index < schema.length - 1) {
                sql += ',';
            }

            sql += '\n';
        });

        sql += ');';
        setTableSql(sql);
    };

    const copyToClipboard = async (text: string) => {
        try {
            await navigator.clipboard.writeText(text);
            toast.success("Copied to clipboard!");
        } catch (err) {
            toast.error("Failed to copy");
        }
    };

    const toggleRealtime = async () => {
        setIsTogglingRealtime(true);
        try {
            const token = localStorage.getItem("token");
            const endpoint = realtimeEnabled ? 'disable' : 'enable';
            const resp = await fetch(`${API_URL}/api/v1/projects/${projectId}/tables/${tableName}/realtime/${endpoint}`, {
                method: 'POST',
                headers: { "Authorization": `Bearer ${token}` }
            });

            if (resp.ok) {
                setRealtimeEnabled(!realtimeEnabled);
                toast.success(`Realtime ${!realtimeEnabled ? 'enabled' : 'disabled'} for table`);
            } else {
                toast.error(`Failed to ${endpoint} realtime`);
            }
        } catch (err) {
            toast.error("Network error");
        } finally {
            setIsTogglingRealtime(false);
        }
    };

    // ... (Existing deleteTable and deleteSelectedRows functions) ...
    const deleteTable = async () => {
        setIsDeletingTable(true);
        try {
            const token = localStorage.getItem("token");
            const resp = await fetch(`${API_URL}/api/v1/projects/${projectId}/sql`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${token}`
                },
                body: JSON.stringify({ sql: `DROP TABLE public."${tableName}" CASCADE;` }),
            });
            const result = await resp.json();
            if (result.success !== false) {
                toast.success(`Table "${tableName}" deleted`);
                router.push(`/projects/${projectId}/database`);
            } else {
                toast.error(result.error || "Failed to delete table");
            }
        } catch (err) {
            toast.error("Network error while deleting table");
        } finally {
            setIsDeletingTable(false);
            setShowDeleteTableModal(false);
        }
    };

    const deleteSelectedRows = async () => {
        const selectedIndices = Object.keys(rowSelection).map(Number);
        if (selectedIndices.length === 0) return;
        if (primaryKeys.length === 0) {
            toast.error("Cannot delete rows: No primary key detected.");
            return;
        }

        setIsDeletingRows(true);
        try {
            const pk = primaryKeys[0];
            const valuesToDelete = selectedIndices.map(idx => {
                const val = data[idx][pk];
                return typeof val === 'string' ? `'${val}'` : val;
            });

            const sql = `DELETE FROM public."${tableName}" WHERE "${pk}" IN (${valuesToDelete.join(', ')});`;

            const token = localStorage.getItem("token");
            const resp = await fetch(`${API_URL}/api/v1/projects/${projectId}/sql`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${token}`
                },
                body: JSON.stringify({ sql }),
            });
            const result = await resp.json();

            if (result.success !== false) {
                toast.success(`Deleted ${selectedIndices.length} row(s)`);
                setRowSelection({});
                fetchTableData();
            } else {
                toast.error(result.error || "Failed to delete rows");
            }
        } catch (err) {
            toast.error("Network error while deleting rows");
        } finally {
            setIsDeletingRows(false);
        }
    };

    const table = useReactTable({
        data,
        columns,
        state: { sorting, rowSelection },
        enableRowSelection: true,
        onRowSelectionChange: setRowSelection,
        onSortingChange: setSorting,
        getCoreRowModel: getCoreRowModel(),
        getSortedRowModel: getSortedRowModel(),
        getPaginationRowModel: getPaginationRowModel(),
        initialState: { pagination: { pageSize: 25 } },
    });

    const exportToCSV = () => {
        if (data.length === 0) return;
        const headers = columns.map((col: any) => col.accessorKey).join(",");
        const rows = data.map((row) =>
            columns.map((col: any) => {
                const val = row[col.accessorKey];
                return typeof val === 'object' ? `"${JSON.stringify(val).replace(/"/g, '""')}"` : `"${String(val ?? '').replace(/"/g, '""')}"`;
            }).join(",")
        );
        const csv = "\uFEFF" + [headers, ...rows].join("\n");
        const blob = new Blob([csv], { type: "text/csv;charset=utf-8;" });
        const url = URL.createObjectURL(blob);
        const link = document.createElement("a");
        link.setAttribute("href", url);
        link.setAttribute("download", `${tableName}.csv`);
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        URL.revokeObjectURL(url);
    };

    return (
        <div className="space-y-6 animate-in fade-in slide-in-from-bottom-4 duration-700 h-full flex flex-col">
            <Breadcrumb
                items={[
                    { label: "Overview", href: `/projects/${projectId}` },
                    { label: "Database", href: `/projects/${projectId}/database` },
                    { label: tableName },
                ]}
            />

            {/* Header */}
            <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
                <div className="flex items-center gap-4">
                    <div className="p-3 bg-emerald-50 dark:bg-emerald-500/10 rounded-xl">
                        <TableIcon size={24} className="text-emerald-600 dark:text-emerald-400" />
                    </div>
                    <div>
                        <div className="flex items-center gap-3">
                            <h2 className="text-3xl font-bold tracking-tight">{tableName}</h2>
                            <Badge variant="secondary" className="bg-muted/50 border-border/40 text-muted-foreground px-2">
                                {rowCount} rows
                            </Badge>
                        </div>
                    </div>
                </div>
                <div className="flex items-center gap-2">
                    <Button
                        variant="outline"
                        size="sm"
                        onClick={toggleRealtime}
                        disabled={isTogglingRealtime}
                        className={cn(
                            "gap-2 border-border/50",
                            realtimeEnabled && "border-emerald-500/50 bg-emerald-50 dark:bg-emerald-500/10 text-emerald-600 dark:text-emerald-400"
                        )}
                    >
                        <Zap size={14} className={realtimeEnabled ? "text-emerald-500" : ""} />
                        {isTogglingRealtime ? "..." : realtimeEnabled ? "Realtime On" : "Enable Realtime"}
                    </Button>
                    <Button variant="danger" size="sm" onClick={() => setShowDeleteTableModal(true)} className="gap-2 bg-destructive/10 text-destructive hover:bg-destructive hover:text-destructive-foreground border-destructive/20">
                        <Trash2 size={14} />
                        Delete Table
                    </Button>
                </div>
            </div>

            {/* Tabs */}
            <Tabs defaultValue="data" className="flex-1 flex flex-col">
                <TabsList className="w-full justify-start border-b border-border/40 bg-transparent p-0 mb-6 rounded-none space-x-6">
                    <TabsTrigger
                        value="data"
                        className="rounded-none border-b-2 border-transparent data-[state=active]:border-primary data-[state=active]:bg-transparent px-4 py-2"
                    >
                        <TableIcon size={16} className="mr-2" />
                        Data
                    </TabsTrigger>
                    <TabsTrigger
                        value="policies"
                        className="rounded-none border-b-2 border-transparent data-[state=active]:border-primary data-[state=active]:bg-transparent px-4 py-2"
                    >
                        <Shield size={16} className="mr-2" />
                        RLS Policies
                    </TabsTrigger>
                    <TabsTrigger
                        value="definition"
                        className="rounded-none border-b-2 border-transparent data-[state=active]:border-primary data-[state=active]:bg-transparent px-4 py-2"
                    >
                        <FileText size={16} className="mr-2" />
                        Definition
                    </TabsTrigger>
                </TabsList>

                {/* DATA TAB */}
                <TabsContent value="data" className="flex-1 flex flex-col m-0 data-[state=inactive]:hidden">
                    <div className="flex justify-between mb-4">
                        <div className="flex items-center gap-2">
                            {/* Filters could go here */}
                        </div>
                        <div className="flex items-center gap-2">
                            <Button variant="outline" size="sm" onClick={fetchTableData} className="gap-2 border-border/50">
                                <RefreshCw size={14} className={cn(loadingData && "animate-spin")} />
                                Refresh
                            </Button>
                            <Button variant="outline" size="sm" onClick={exportToCSV} className="gap-2 border-border/50">
                                <Download size={14} />
                                Export CSV
                            </Button>
                            <div className="w-px h-6 bg-border/40 mx-1" />
                            <Button size="sm" onClick={() => setRowEditorOpen(true)} className="gap-2 primary-gradient">
                                <Plus size={14} />
                                Insert Row
                            </Button>
                        </div>
                    </div>

                    <div className="flex-1 flex flex-col border border-border/40 rounded-2xl overflow-hidden bg-card shadow-xl glass">
                        {/* (Table Rendering Logic Same as Before) */}
                        <div className="overflow-x-auto flex-1">
                            <table className="w-full border-collapse">
                                <thead className="bg-muted/50 border-b border-border/40 sticky top-0 z-10 backdrop-blur-md">
                                    {table.getHeaderGroups().map((headerGroup) => (
                                        <tr key={headerGroup.id}>
                                            <th className="w-10 px-4 py-4 text-center">
                                                <button onClick={() => table.toggleAllRowsSelected()}>
                                                    {table.getIsAllRowsSelected() ? <CheckSquare size={16} className="text-primary" /> : <Square size={16} />}
                                                </button>
                                            </th>
                                            {headerGroup.headers.map((header) => (
                                                <th key={header.id} className="px-6 py-4 text-left font-normal">
                                                    {header.isPlaceholder ? null : flexRender(header.column.columnDef.header, header.getContext())}
                                                </th>
                                            ))}
                                            <th className="w-20 px-6 py-4" />
                                        </tr>
                                    ))}
                                </thead>
                                <tbody>
                                    {table.getRowModel().rows.map((row) => (
                                        <tr key={row.id} className={cn("border-b border-border/20 transition-colors group", row.getIsSelected() ? "bg-primary/5" : "hover:bg-muted/30")}>
                                            <td className="w-10 px-4 py-4 text-center">
                                                <button onClick={() => row.toggleSelected()} className={cn("transition-colors", row.getIsSelected() ? "text-primary" : "text-muted-foreground/40")}>
                                                    {row.getIsSelected() ? <CheckSquare size={16} /> : <Square size={16} />}
                                                </button>
                                            </td>
                                            {row.getVisibleCells().map((cell) => (
                                                <td key={cell.id} className="px-6 py-4">
                                                    <div className="truncate max-w-[200px]">{flexRender(cell.column.columnDef.cell, cell.getContext())}</div>
                                                </td>
                                            ))}
                                            <td className="w-20 px-6 py-4 text-right">
                                                <Button variant="ghost" size="icon" className="h-8 w-8 opacity-0 group-hover:opacity-100">
                                                    <Settings size={14} />
                                                </Button>
                                            </td>
                                        </tr>
                                    ))}
                                </tbody>
                            </table>
                        </div>

                        {/* Footer / Pagination */}
                        <div className="flex items-center justify-between px-8 py-4 border-t border-border/40 bg-muted/20">
                            <div className="flex items-center gap-6">
                                <span className="text-xs font-medium text-muted-foreground uppercase tracking-widest">
                                    Rows: <span className="text-foreground">{data.length}</span>
                                </span>
                                <div className="h-4 w-[1px] bg-border/40" />
                                <span className="text-xs font-medium text-muted-foreground uppercase tracking-widest">
                                    Page <span className="text-foreground">{table.getState().pagination.pageIndex + 1}</span> of <span className="text-foreground">{table.getPageCount() || 1}</span>
                                </span>
                            </div>
                            <div className="flex items-center gap-3">
                                <Button variant="outline" size="sm" onClick={() => table.previousPage()} disabled={!table.getCanPreviousPage()} className="h-8 px-3 gap-1 border-border/40">
                                    <ChevronLeft size={14} /> Previous
                                </Button>
                                <Button variant="outline" size="sm" onClick={() => table.nextPage()} disabled={!table.getCanNextPage()} className="h-8 px-3 gap-1 border-border/40">
                                    Next <ChevronRight size={14} />
                                </Button>
                            </div>
                        </div>

                        {/* Selection Floating Toolbar */}
                        {Object.keys(rowSelection).length > 0 && (
                            <div className="absolute bottom-20 left-1/2 -translate-x-1/2 bg-foreground text-background px-6 py-3 rounded-2xl shadow-2xl flex items-center gap-4 animate-in slide-in-from-bottom-4 z-20">
                                <span className="text-sm font-bold">{Object.keys(rowSelection).length} rows selected</span>
                                <div className="w-px h-4 bg-background/20" />
                                <Button size="sm" variant="ghost" onClick={deleteSelectedRows} disabled={isDeletingRows} className="h-8 text-red-400 hover:text-red-300 hover:bg-red-500/10 gap-2">
                                    <Trash2 size={14} /> {isDeletingRows ? "Deleting..." : "Delete Selected"}
                                </Button>
                            </div>
                        )}
                    </div>
                </TabsContent>

                {/* POLICIES TAB */}
                <TabsContent value="policies" className="space-y-6 m-0 data-[state=inactive]:hidden">
                    <div className="flex items-start justify-between">
                        <div>
                            <h3 className="text-lg font-bold">Row Level Security (RLS)</h3>
                            <p className="text-sm text-muted-foreground mt-1">
                                Restrict access to rows based on user roles and attributes.
                            </p>
                        </div>
                        <div className="flex items-center gap-3">
                            <Button variant="outline" onClick={() => toggleRLS(!rlsEnabled)}>
                                {rlsEnabled ? (
                                    <>
                                        <Lock size={16} className="mr-2 text-primary" />
                                        Disable RLS
                                    </>
                                ) : (
                                    <>
                                        <Unlock size={16} className="mr-2 text-muted-foreground" />
                                        Enable RLS
                                    </>
                                )}
                            </Button>
                            <Button className="primary-gradient" onClick={() => { setEditingPolicy(null); setShowPolicyEditor(true); }}>
                                <Plus size={16} className="mr-2" />
                                Create Policy
                            </Button>
                        </div>
                    </div>

                    <div className="grid grid-cols-1 gap-4">
                        {policies.length === 0 ? (
                            <div className="p-12 text-center border-2 border-dashed border-border/40 rounded-2xl bg-card/40">
                                <Shield size={48} className="mx-auto text-muted-foreground/30 mb-4" />
                                <h4 className="text-lg font-bold">No policies found</h4>
                                <p className="text-muted-foreground text-sm mt-2 max-w-sm mx-auto">
                                    Row Level Security policies determine which rows are visible or editable by users.
                                </p>
                            </div>
                        ) : (
                            policies.map((policy) => (
                                <div key={policy.policy_name} className="p-6 bg-card border border-border/40 rounded-xl hover:border-primary/40 transition-all flex items-start justify-between group">
                                    <div>
                                        <div className="flex items-center gap-2 mb-2">
                                            <h4 className="font-bold text-lg">{policy.policy_name}</h4>
                                            <Badge variant="outline" className="font-mono text-xs">{policy.command}</Badge>
                                            <Badge className="bg-primary/10 text-primary border-primary/20">{policy.roles.join(", ")}</Badge>
                                        </div>
                                        <div className="font-mono text-xs text-muted-foreground bg-muted/30 p-2 rounded-lg">
                                            USING ({policy.using_expression})
                                            {policy.check_expression && (
                                                <span className="block mt-1 pt-1 border-t border-border/20">
                                                    WITH CHECK ({policy.check_expression})
                                                </span>
                                            )}
                                        </div>
                                    </div>
                                    <div className="flex items-center gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                        <Button variant="ghost" size="sm" onClick={() => { setEditingPolicy(policy); setShowPolicyEditor(true); }}>
                                            Edit
                                        </Button>
                                        <Button variant="ghost" size="sm" className="text-destructive hover:bg-destructive/10" onClick={() => setDeletingPolicy(policy.policy_name)}>
                                            <Trash2 size={16} />
                                        </Button>
                                    </div>
                                </div>
                            ))
                        )}
                    </div>
                </TabsContent>

                {/* DEFINITION TAB */}
                <TabsContent value="definition" className="space-y-6 m-0 data-[state=inactive]:hidden">
                    <div className="flex items-center justify-end mb-4">
                        <Button onClick={() => setShowAddColumnModal(true)} size="sm" className="gap-2 primary-gradient">
                            <Plus size={14} />
                            Add Column
                        </Button>
                    </div>

                    {/* SQL Definition */}
                    <div className="mb-8">
                        <div className="flex items-center justify-between mb-4">
                            <h3 className="text-lg font-bold flex items-center gap-2">
                                <FileText size={18} className="text-primary" /> SQL Definition
                            </h3>
                            <Button
                                variant="outline"
                                size="sm"
                                onClick={() => copyToClipboard(tableSql)}
                                className="gap-2 border-border/50"
                                disabled={!tableSql}
                            >
                                <Copy size={14} />
                                Copy SQL
                            </Button>
                        </div>
                        {loadingData ? (
                            <Skeleton className="h-64 w-full rounded-xl" />
                        ) : (
                            <div className="bg-card border border-border/40 rounded-xl overflow-hidden">
                                <div className="bg-muted/30 px-4 py-2 border-b border-border/40">
                                    <span className="text-xs font-mono text-muted-foreground uppercase tracking-wider">CREATE TABLE</span>
                                </div>
                                <pre className="p-6 overflow-x-auto">
                                    <code className="text-sm font-mono text-foreground">{tableSql || "No schema available"}</code>
                                </pre>
                            </div>
                        )}
                    </div>

                    <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
                        <div>
                            <h3 className="text-lg font-bold mb-4 flex items-center gap-2">
                                <Key size={18} className="text-primary" /> Constraints
                            </h3>
                            {loadingMeta ? (
                                <Skeleton className="h-32 w-full rounded-xl" />
                            ) : constraints.length === 0 ? (
                                <p className="text-muted-foreground italic">No constraints definition</p>
                            ) : (
                                <div className="space-y-3">
                                    {constraints.map((c, i) => (
                                        <div key={i} className="p-4 bg-card border border-border/40 rounded-xl">
                                            <div className="flex items-center justify-between mb-2">
                                                <span className="font-mono font-bold text-sm">{c.constraint_name}</span>
                                                <Badge variant="outline">{c.constraint_type}</Badge>
                                            </div>
                                            <div className="text-xs text-muted-foreground">
                                                {c.constraint_type === "FOREIGN KEY" ? (
                                                    <span>References <strong className="text-foreground">{c.foreign_table_name}.{c.foreign_column_name}</strong></span>
                                                ) : c.constraint_type === "CHECK" ? (
                                                    <code className="bg-muted px-1 rounded">{c.check_clause}</code>
                                                ) : (
                                                    <span>On column <strong className="text-foreground">{c.column_name}</strong></span>
                                                )}
                                            </div>
                                        </div>
                                    ))}
                                </div>
                            )}
                        </div>

                        <div>
                            <h3 className="text-lg font-bold mb-4 flex items-center gap-2">
                                <Database size={18} className="text-primary" /> Indexes
                            </h3>
                            {loadingMeta ? (
                                <Skeleton className="h-32 w-full rounded-xl" />
                            ) : indexes.length === 0 ? (
                                <p className="text-muted-foreground italic">No indexes defined</p>
                            ) : (
                                <div className="space-y-3">
                                    {indexes.map((idx, i) => (
                                        <div key={i} className="p-4 bg-card border border-border/40 rounded-xl">
                                            <div className="font-mono font-bold text-sm mb-2">{idx.index_name}</div>
                                            <code className="block text-xs text-muted-foreground bg-muted/30 p-2 rounded break-all">
                                                {idx.definition}
                                            </code>
                                        </div>
                                    ))}
                                </div>
                            )}
                        </div>
                    </div>
                </TabsContent>
            </Tabs>

            {/* Modals */}
            <Modal open={showDeleteTableModal} onOpenChange={setShowDeleteTableModal}>
                <ModalContent className="max-w-md bg-card border-border/40 shadow-2xl glass rounded-2xl p-6">
                    <ModalHeader className="mb-4">
                        <ModalTitle className="text-xl font-bold text-destructive">Delete Table</ModalTitle>
                    </ModalHeader>
                    <p className="text-sm text-muted-foreground">
                        Are you sure you want to delete <span className="font-mono font-bold">"{tableName}"</span>?
                    </p>
                    <ModalFooter className="flex items-center justify-end gap-3 mt-6">
                        <Button variant="ghost" onClick={() => setShowDeleteTableModal(false)} disabled={isDeletingTable}>Cancel</Button>
                        <Button onClick={deleteTable} disabled={isDeletingTable} className="bg-destructive text-destructive-foreground">Delete</Button>
                    </ModalFooter>
                </ModalContent>
            </Modal>

            <RLSPolicyEditor
                open={showPolicyEditor}
                onOpenChange={setShowPolicyEditor}
                projectId={projectId}
                tableName={tableName}
                policy={editingPolicy}
                onSuccess={() => { fetchPolicies(); setShowPolicyEditor(false); }}
            />

            <RowEditor
                open={rowEditorOpen}
                onOpenChange={setRowEditorOpen}
                projectId={projectId}
                tableName={tableName}
                onSuccess={fetchTableData}
            />

            <AddColumnModal
                open={showAddColumnModal}
                onOpenChange={setShowAddColumnModal}
                projectId={projectId}
                tableName={tableName}
                onSuccess={() => {
                    fetchTableData();
                    fetchMetadata(); // Refresh schema/constraints
                }}
            />

            <Toaster richColors position="top-right" />
        </div>
    );
}
