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
import { ArrowUpDown, Plus, Download, RefreshCw, ChevronLeft, ChevronRight, Settings } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Breadcrumb } from "@/components/ui/breadcrumb";
import { Skeleton } from "@/components/ui/skeleton";
import { Badge } from "@/components/ui/badge";
import { cn } from "@/lib/utils";

export default function TableDetailPage() {
    const params = useParams();
    const router = useRouter();
    const projectId = params.id as string;
    const tableName = params.table as string;

    const [data, setData] = useState<any[]>([]);
    const [columns, setColumns] = useState<ColumnDef<any>[]>([]);
    const [loading, setLoading] = useState(true);
    const [sorting, setSorting] = useState<SortingState>([]);
    const [rowCount, setRowCount] = useState(0);

    const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

    useEffect(() => {
        fetchTableData();
    }, [projectId, tableName]);

    const fetchTableData = async () => {
        setLoading(true);
        try {
            const resp = await fetch(
                `${API_URL}/v1/projects/${projectId}/tables/${tableName}/data`
            );
            const result = await resp.json();

            if (result.rows && result.columns) {
                setData(result.rows);
                setRowCount(result.rowCount || result.rows.length);

                // Create columns dynamically
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
                        return <span className="text-sm">{String(value)}</span>;
                    },
                }));

                setColumns(cols);
            }
        } catch (err) {
            console.error("Failed to fetch table data", err);
        } finally {
            setLoading(false);
        }
    };

    const table = useReactTable({
        data,
        columns,
        state: {
            sorting,
        },
        onSortingChange: setSorting,
        getCoreRowModel: getCoreRowModel(),
        getSortedRowModel: getSortedRowModel(),
        getPaginationRowModel: getPaginationRowModel(),
        initialState: {
            pagination: {
                pageSize: 25,
            },
        },
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
        const csv = [headers, ...rows].join("\n");

        const blob = new Blob([csv], { type: "text/csv" });
        const url = URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url;
        a.download = `${tableName}_export.csv`;
        a.click();
        URL.revokeObjectURL(url);
    };

    return (
        <div className="space-y-8 animate-in fade-in slide-in-from-bottom-4 duration-700 h-full flex flex-col">
            {/* Breadcrumb */}
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
                        <p className="text-sm text-muted-foreground mt-1">
                            Browse and managedata in the <span className="font-mono font-medium text-foreground">public.{tableName}</span> table.
                        </p>
                    </div>
                </div>
                <div className="flex items-center gap-2">
                    <Button variant="outline" size="sm" onClick={fetchTableData} className="gap-2 border-border/50">
                        <RefreshCw size={14} className={cn(loading && "animate-spin")} />
                        Refresh
                    </Button>
                    <Button variant="outline" size="sm" onClick={exportToCSV} className="gap-2 border-border/50">
                        <Download size={14} />
                        Export CSV
                    </Button>
                    <Button size="sm" className="gap-2 primary-gradient shadow-lg shadow-emerald-500/10">
                        <Plus size={14} />
                        Insert Row
                    </Button>
                </div>
            </div>

            {/* Data Grid Section */}
            <div className="flex-1 flex flex-col min-h-[400px]">
                {loading ? (
                    <div className="space-y-3 bg-card border border-border/40 rounded-2xl p-6 shadow-sm">
                        <Skeleton className="h-10 w-full rounded-lg" />
                        {[...Array(8)].map((_, i) => (
                            <Skeleton key={i} className="h-14 w-full rounded-lg opacity-40" />
                        ))}
                    </div>
                ) : data.length === 0 ? (
                    <div className="flex-1 flex flex-col items-center justify-center bg-card/40 border-2 border-dashed border-border/40 rounded-2xl p-12">
                        <div className="w-16 h-16 rounded-full bg-muted flex items-center justify-center mb-4">
                            <TableIcon size={32} className="text-muted-foreground/40" />
                        </div>
                        <h3 className="text-xl font-bold text-foreground">No data found</h3>
                        <p className="text-sm text-muted-foreground text-center mt-2 max-w-sm">
                            This table currently has no rows. Click "Insert Row" to add your first entry or import data via SQL.
                        </p>
                        <Button className="mt-6 primary-gradient" size="sm">
                            <Plus size={14} className="mr-2" />
                            Add First Row
                        </Button>
                    </div>
                ) : (
                    <div className="flex-1 flex flex-col border border-border/40 rounded-2xl overflow-hidden bg-card shadow-xl glass">
                        <div className="overflow-x-auto flex-1">
                            <table className="w-full border-collapse">
                                <thead className="bg-muted/50 border-b border-border/40 sticky top-0 z-10 backdrop-blur-md">
                                    {table.getHeaderGroups().map((headerGroup) => (
                                        <tr key={headerGroup.id}>
                                            <th className="w-10 px-4 py-4 text-center">
                                                <input type="checkbox" className="rounded border-border text-primary focus:ring-primary/20" />
                                            </th>
                                            {headerGroup.headers.map((header) => (
                                                <th
                                                    key={header.id}
                                                    className="px-6 py-4 text-left font-normal"
                                                >
                                                    {header.isPlaceholder
                                                        ? null
                                                        : flexRender(
                                                            header.column.columnDef.header,
                                                            header.getContext()
                                                        )}
                                                </th>
                                            ))}
                                            <th className="w-20 px-6 py-4" /> {/* Actions column */}
                                        </tr>
                                    ))}
                                </thead>
                                <tbody>
                                    {table.getRowModel().rows.map((row) => (
                                        <tr
                                            key={row.id}
                                            className="border-b border-border/20 hover:bg-emerald-50/30 dark:hover:bg-emerald-500/5 transition-colors group"
                                        >
                                            <td className="w-10 px-4 py-4 text-center">
                                                <input type="checkbox" className="rounded border-border text-primary focus:ring-primary/20" />
                                            </td>
                                            {row.getVisibleCells().map((cell) => (
                                                <td key={cell.id} className="px-6 py-4">
                                                    <div className="truncate max-w-[200px]">
                                                        {flexRender(cell.column.columnDef.cell, cell.getContext())}
                                                    </div>
                                                </td>
                                            ))}
                                            <td className="w-20 px-6 py-4 text-right">
                                                <Button variant="ghost" size="icon" className="h-8 w-8 opacity-0 group-hover:opacity-100 transition-opacity">
                                                    <Settings size={14} className="text-muted-foreground" />
                                                </Button>
                                            </td>
                                        </tr>
                                    ))}
                                </tbody>
                            </table>
                        </div>

                        {/* Professional Pagination */}
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
                                <Button
                                    variant="outline"
                                    size="sm"
                                    onClick={() => table.previousPage()}
                                    disabled={!table.getCanPreviousPage()}
                                    className="h-8 px-3 gap-1 border-border/40"
                                >
                                    <ChevronLeft size={14} />
                                    Previous
                                </Button>
                                <div className="flex items-center gap-1">
                                    {[...Array(Math.min(5, table.getPageCount()))].map((_, i) => (
                                        <button
                                            key={i}
                                            onClick={() => table.setPageIndex(i)}
                                            className={cn(
                                                "w-8 h-8 rounded-lg text-xs font-bold transition-all",
                                                table.getState().pagination.pageIndex === i
                                                    ? "bg-primary text-primary-foreground shadow-lg shadow-primary/20"
                                                    : "hover:bg-muted text-muted-foreground"
                                            )}
                                        >
                                            {i + 1}
                                        </button>
                                    ))}
                                </div>
                                <Button
                                    variant="outline"
                                    size="sm"
                                    onClick={() => table.nextPage()}
                                    disabled={!table.getCanNextPage()}
                                    className="h-8 px-3 gap-1 border-border/40"
                                >
                                    Next
                                    <ChevronRight size={14} />
                                </Button>
                            </div>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
}

const TableIcon = ({ size, className }: { size?: number, className?: string }) => (
    <svg
        width={size || 24}
        height={size || 24}
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        strokeWidth="2"
        strokeLinecap="round"
        strokeLinejoin="round"
        className={className}
    >
        <path d="M12 3h7a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-7m0-18H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h7m0-18v18" />
        <line x1="3" y1="9" x2="21" y2="9" />
        <line x1="3" y1="15" x2="21" y2="15" />
    </svg>
);
