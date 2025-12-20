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
import { ArrowUpDown, Plus, Download } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Breadcrumb } from "@/components/ui/breadcrumb";
import { Skeleton } from "@/components/ui/skeleton";
import { Badge } from "@/components/ui/badge";

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
                                className="flex items-center gap-2 font-semibold hover:text-primary transition-colors"
                                onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}
                            >
                                {col}
                                <ArrowUpDown size={14} />
                            </button>
                        );
                    },
                    cell: (info: CellContext<any, unknown>) => {
                        const value = info.getValue();
                        if (value === null) return <span className="text-muted-foreground italic">NULL</span>;
                        if (typeof value === "boolean") return value ? "true" : "false";
                        if (typeof value === "object") return JSON.stringify(value);
                        return String(value);
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
            columns.map((col: any) => JSON.stringify(row[col.accessorKey] ?? "")).join(",")
        );
        const csv = [headers, ...rows].join("\n");

        const blob = new Blob([csv], { type: "text/csv" });
        const url = URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url;
        a.download = `${tableName}.csv`;
        a.click();
        URL.revokeObjectURL(url);
    };

    return (
        <div className="space-y-6">
            {/* Breadcrumb */}
            <Breadcrumb
                items={[
                    { label: "Overview", href: `/projects/${projectId}` },
                    { label: "Database", href: `/projects/${projectId}/database` },
                    { label: tableName },
                ]}
            />

            {/* Header */}
            <div className="flex items-center justify-between">
                <div className="flex items-center gap-3">
                    <h2 className="text-2xl font-bold">{tableName}</h2>
                    <Badge variant="secondary">{rowCount} rows</Badge>
                </div>
                <div className="flex items-center gap-2">
                    <Button variant="outline" size="sm" onClick={exportToCSV} className="gap-2">
                        <Download size={16} />
                        Export
                    </Button>
                    <Button size="sm" className="gap-2">
                        <Plus size={16} />
                        Add Row
                    </Button>
                </div>
            </div>

            {/* Data Grid */}
            {loading ? (
                <div className="space-y-3">
                    <Skeleton className="h-12 w-full" />
                    {[...Array(10)].map((_, i) => (
                        <Skeleton key={i} className="h-16 w-full" />
                    ))}
                </div>
            ) : (
                <div className="border border-border rounded-lg overflow-hidden bg-card">
                    <div className="overflow-x-auto">
                        <table className="w-full">
                            <thead className="bg-muted border-b border-border">
                                {table.getHeaderGroups().map((headerGroup) => (
                                    <tr key={headerGroup.id}>
                                        {headerGroup.headers.map((header) => (
                                            <th
                                                key={header.id}
                                                className="px-4 py-3 text-left text-sm font-semibold text-foreground"
                                            >
                                                {header.isPlaceholder
                                                    ? null
                                                    : flexRender(
                                                        header.column.columnDef.header,
                                                        header.getContext()
                                                    )}
                                            </th>
                                        ))}
                                    </tr>
                                ))}
                            </thead>
                            <tbody>
                                {table.getRowModel().rows.map((row) => (
                                    <tr
                                        key={row.id}
                                        className="border-b border-border hover:bg-muted/50 transition-colors"
                                    >
                                        {row.getVisibleCells().map((cell) => (
                                            <td key={cell.id} className="px-4 py-3 text-sm">
                                                {flexRender(cell.column.columnDef.cell, cell.getContext())}
                                            </td>
                                        ))}
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    </div>

                    {/* Pagination */}
                    <div className="flex items-center justify-between px-4 py-3 border-t border-border bg-muted/30">
                        <div className="text-sm text-muted-foreground">
                            Page {table.getState().pagination.pageIndex + 1} of{" "}
                            {table.getPageCount()} • {data.length} rows
                        </div>
                        <div className="flex items-center gap-2">
                            <Button
                                variant="outline"
                                size="sm"
                                onClick={() => table.previousPage()}
                                disabled={!table.getCanPreviousPage()}
                            >
                                Previous
                            </Button>
                            <Button
                                variant="outline"
                                size="sm"
                                onClick={() => table.nextPage()}
                                disabled={!table.getCanNextPage()}
                            >
                                Next
                            </Button>
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
}
