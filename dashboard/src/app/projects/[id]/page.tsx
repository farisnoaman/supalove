"use client";

import { useEffect, useState } from "react";
import { useParams, useRouter } from "next/navigation";
import { Table as TableIcon, Settings } from "lucide-react";
import { Button } from "@/components/ui/button";

export default function ProjectOverviewPage() {
    const params = useParams();
    const router = useRouter();
    const projectId = params.id as string;

    const [tables, setTables] = useState<any[]>([]);
    const [loading, setLoading] = useState(true);

    const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

    useEffect(() => {
        fetchTables();
    }, [projectId]);

    const fetchTables = async () => {
        setLoading(true);
        try {
            const resp = await fetch(`${API_URL}/v1/projects/${projectId}/tables`);
            const data = await resp.json();
            // Fetch row counts for each table
            const tablesWithCounts = await Promise.all(
                data.map(async (table: any) => {
                    try {
                        const dataResp = await fetch(
                            `${API_URL}/v1/projects/${projectId}/tables/${table.table_name}/data`
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
        } finally {
            setLoading(false);
        }
    };

    const topTables = tables.slice(0, 3);

    return (
        <div className="space-y-6 max-w-4xl">
            {/* Database Section */}
            <div className="bg-white border border-gray-200 rounded-lg">
                <div className="p-6 border-b border-gray-200">
                    <div className="flex items-start justify-between">
                        <div>
                            <h2 className="text-lg font-semibold text-gray-900">Database</h2>
                            <p className="text-sm text-gray-600 mt-0.5">
                                View tables and edit data
                            </p>
                        </div>
                        <span className="text-sm text-gray-600">{tables.length} Tables</span>
                    </div>
                </div>
                <div className="p-6">
                    {loading ? (
                        <div className="text-center py-8 text-gray-500">Loading...</div>
                    ) : tables.length === 0 ? (
                        <div className="text-center py-8 text-gray-500">
                            No tables found. Create your first table in the database view.
                        </div>
                    ) : (
                        <>
                            <div className="space-y-0">
                                {topTables.map((table, index) => (
                                    <button
                                        key={table.table_name}
                                        onClick={() =>
                                            router.push(`/projects/${projectId}/database/${table.table_name}`)
                                        }
                                        className={cn(
                                            "w-full flex items-center justify-between px-4 py-3 hover:bg-gray-50 transition-colors text-left",
                                            index < topTables.length - 1 && "border-b border-gray-100"
                                        )}
                                    >
                                        <div className="flex items-center gap-3">
                                            <TableIcon size={16} className="text-gray-400" />
                                            <span className="text-sm font-medium text-gray-900">
                                                {table.table_name}
                                            </span>
                                        </div>
                                        <span className="text-sm text-gray-500">
                                            {table.rowCount} rows
                                        </span>
                                    </button>
                                ))}
                            </div>
                            {tables.length > 3 && (
                                <div className="mt-4 text-center">
                                    <button
                                        onClick={() => router.push(`/projects/${projectId}/database`)}
                                        className="text-sm text-gray-900 hover:underline font-medium"
                                    >
                                        View all
                                    </button>
                                </div>
                            )}
                        </>
                    )}
                </div>
            </div>

            {/* Users Section */}
            <div className="bg-white border border-gray-200 rounded-lg">
                <div className="p-6 border-b border-gray-200">
                    <div className="flex items-start justify-between">
                        <div>
                            <h2 className="text-lg font-semibold text-gray-900">Users</h2>
                            <p className="text-sm text-gray-600 mt-0.5">
                                View user data and configure how users sign up
                            </p>
                        </div>
                        <span className="text-sm text-gray-600">1 Signup</span>
                    </div>
                </div>
                <div className="p-6">
                    <Button variant="outline" className="w-full justify-start gap-2 bg-gray-50 border-gray-200 hover:bg-gray-100">
                        <Settings size={16} />
                        Auth settings
                    </Button>
                </div>
            </div>

            {/* Storage Section */}
            <div className="bg-white border border-gray-200 rounded-lg">
                <div className="p-6 border-b border-gray-200">
                    <div className="flex items-start justify-between">
                        <div>
                            <h2 className="text-lg font-semibold text-gray-900">Storage</h2>
                            <p className="text-sm text-gray-600 mt-0.5">
                                View and manage files, images, and documents
                            </p>
                        </div>
                        <span className="text-sm text-gray-600">1 Bucket</span>
                    </div>
                </div>
                <div className="p-6">
                    <button className="w-full flex items-center gap-3 px-4 py-3 hover:bg-gray-50 transition-colors text-left bg-gray-50 rounded">
                        <span className="text-sm font-medium text-gray-900">product-images</span>
                    </button>
                </div>
            </div>

            {/* Edge Functions Section */}
            <div className="bg-white border border-gray-200 rounded-lg">
                <div className="p-6 border-b border-gray-200">
                    <div className="flex items-start justify-between">
                        <div>
                            <h2 className="text-lg font-semibold text-gray-900">Edge functions</h2>
                            <p className="text-sm text-gray-600 mt-0.5">
                                Configure functions executed in your app
                            </p>
                        </div>
                        <span className="text-sm text-gray-600">0 Functions</span>
                    </div>
                </div>
                <div className="p-6">
                    <div className="text-center py-12">
                        <div className="inline-flex items-center justify-center w-12 h-12 rounded-full bg-gray-100 mb-3">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" className="text-gray-400">
                                <path d="M9 3L3 9L9 15" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
                                <path d="M15 9L21 15L15 21" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
                            </svg>
                        </div>
                        <p className="text-sm text-gray-500">
                            Edge functions will appear when<br />adding custom background actions
                        </p>
                    </div>
                </div>
            </div>
        </div>
    );
}

function cn(...classes: any[]) {
    return classes.filter(Boolean).join(' ');
}
