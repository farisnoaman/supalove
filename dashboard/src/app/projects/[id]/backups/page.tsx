"use client";

import { useParams } from "next/navigation";
import { useState, useEffect } from "react";
import { Download, Clock, Database, HardDrive, RefreshCw } from "lucide-react";
import { toast } from "sonner";

interface Backup {
    name: string;
    size: number;
    last_modified: string;
}

export default function BackupsPage() {
    const params = useParams();
    const projectId = params.id as string;
    const [backups, setBackups] = useState<Backup[]>([]);
    const [loading, setLoading] = useState(true);
    const [creating, setCreating] = useState(false);

    const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000";

    const fetchBackups = async () => {
        try {
            const res = await fetch(`${API_URL}/v1/projects/${projectId}/backups`);
            if (res.ok) {
                const data = await res.json();
                setBackups(data);
            }
        } catch (error) {
            console.error("Failed to fetch backups:", error);
        } finally {
            setLoading(false);
        }
    };

    const createBackup = async () => {
        setCreating(true);
        try {
            const res = await fetch(`${API_URL}/v1/projects/${projectId}/backups`, {
                method: "POST",
            });
            if (res.ok) {
                toast.success("Backup created successfully");
                fetchBackups();
            } else {
                toast.error("Failed to create backup");
            }
        } catch (error) {
            toast.error("Failed to create backup");
        } finally {
            setCreating(false);
        }
    };

    useEffect(() => {
        fetchBackups();
    }, [projectId]);

    const formatSize = (bytes: number) => {
        if (bytes < 1024) return bytes + " B";
        if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(2) + " KB";
        return (bytes / (1024 * 1024)).toFixed(2) + " MB";
    };

    const formatDate = (dateStr: string) => {
        return new Date(dateStr).toLocaleString();
    };

    const getBackupType = (name: string) => {
        if (name.includes("/db_")) return "database";
        if (name.includes("/storage_")) return "storage";
        return "unknown";
    };

    return (
        <div className="p-8 space-y-6">
            {/* Header */}
            <div className="flex items-center justify-between">
                <div>
                    <h1 className="text-3xl font-bold text-slate-100">Backups</h1>
                    <p className="text-slate-400 mt-1">
                        Manage database and storage backups for your project
                    </p>
                </div>
                <button
                    onClick={createBackup}
                    disabled={creating}
                    className="px-4 py-2 bg-emerald-600 hover:bg-emerald-700 disabled:bg-slate-700 disabled:cursor-not-allowed text-white rounded-lg font-medium transition-colors flex items-center gap-2"
                >
                    <RefreshCw className={`h-4 w-4 ${creating ? "animate-spin" : ""}`} />
                    {creating ? "Creating..." : "Create Backup"}
                </button>
            </div>

            {/* Stats Cards */}
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                <div className="bg-slate-800/50 backdrop-blur-sm border border-slate-700/50 rounded-lg p-6">
                    <div className="flex items-center gap-3">
                        <div className="p-3 bg-blue-500/10 rounded-lg">
                            <Database className="h-6 w-6 text-blue-400" />
                        </div>
                        <div>
                            <p className="text-slate-400 text-sm">Database Backups</p>
                            <p className="text-2xl font-bold text-slate-100">
                                {backups.filter((b) => getBackupType(b.name) === "database").length}
                            </p>
                        </div>
                    </div>
                </div>

                <div className="bg-slate-800/50 backdrop-blur-sm border border-slate-700/50 rounded-lg p-6">
                    <div className="flex items-center gap-3">
                        <div className="p-3 bg-purple-500/10 rounded-lg">
                            <HardDrive className="h-6 w-6 text-purple-400" />
                        </div>
                        <div>
                            <p className="text-slate-400 text-sm">Storage Backups</p>
                            <p className="text-2xl font-bold text-slate-100">
                                {backups.filter((b) => getBackupType(b.name) === "storage").length}
                            </p>
                        </div>
                    </div>
                </div>

                <div className="bg-slate-800/50 backdrop-blur-sm border border-slate-700/50 rounded-lg p-6">
                    <div className="flex items-center gap-3">
                        <div className="p-3 bg-emerald-500/10 rounded-lg">
                            <Clock className="h-6 w-6 text-emerald-400" />
                        </div>
                        <div>
                            <p className="text-slate-400 text-sm">Total Backups</p>
                            <p className="text-2xl font-bold text-slate-100">{backups.length}</p>
                        </div>
                    </div>
                </div>
            </div>

            {/* Backups List */}
            <div className="bg-slate-800/50 backdrop-blur-sm border border-slate-700/50 rounded-lg overflow-hidden">
                <div className="p-6 border-b border-slate-700/50">
                    <h2 className="text-xl font-semibold text-slate-100">Backup History</h2>
                </div>

                {loading ? (
                    <div className="p-12 text-center text-slate-400">Loading backups...</div>
                ) : backups.length === 0 ? (
                    <div className="p-12 text-center">
                        <div className="inline-block p-4 bg-slate-700/30 rounded-full mb-4">
                            <Download className="h-8 w-8 text-slate-500" />
                        </div>
                        <p className="text-slate-400 mb-2">No backups yet</p>
                        <p className="text-slate-500 text-sm">
                            Create your first backup to get started
                        </p>
                    </div>
                ) : (
                    <div className="overflow-x-auto">
                        <table className="w-full">
                            <thead className="bg-slate-900/50 border-b border-slate-700/50">
                                <tr>
                                    <th className="px-6 py-3 text-left text-xs font-medium text-slate-400 uppercase tracking-wider">
                                        Type
                                    </th>
                                    <th className="px-6 py-3 text-left text-xs font-medium text-slate-400 uppercase tracking-wider">
                                        Name
                                    </th>
                                    <th className="px-6 py-3 text-left text-xs font-medium text-slate-400 uppercase tracking-wider">
                                        Size
                                    </th>
                                    <th className="px-6 py-3 text-left text-xs font-medium text-slate-400 uppercase tracking-wider">
                                        Created
                                    </th>
                                </tr>
                            </thead>
                            <tbody className="divide-y divide-slate-700/50">
                                {backups.map((backup, idx) => {
                                    const type = getBackupType(backup.name);
                                    return (
                                        <tr
                                            key={idx}
                                            className="hover:bg-slate-700/20 transition-colors"
                                        >
                                            <td className="px-6 py-4 whitespace-nowrap">
                                                <div className="flex items-center gap-2">
                                                    {type === "database" ? (
                                                        <Database className="h-4 w-4 text-blue-400" />
                                                    ) : (
                                                        <HardDrive className="h-4 w-4 text-purple-400" />
                                                    )}
                                                    <span className="text-sm font-medium text-slate-300 capitalize">
                                                        {type}
                                                    </span>
                                                </div>
                                            </td>
                                            <td className="px-6 py-4">
                                                <code className="text-sm text-slate-400 font-mono">
                                                    {backup.name}
                                                </code>
                                            </td>
                                            <td className="px-6 py-4 whitespace-nowrap text-sm text-slate-400">
                                                {formatSize(backup.size)}
                                            </td>
                                            <td className="px-6 py-4 whitespace-nowrap text-sm text-slate-400">
                                                {formatDate(backup.last_modified)}
                                            </td>
                                        </tr>
                                    );
                                })}
                            </tbody>
                        </table>
                    </div>
                )}
            </div>

            {/* Info Banner */}
            <div className="bg-blue-500/10 border border-blue-500/20 rounded-lg p-4">
                <div className="flex gap-3">
                    <Clock className="h-5 w-5 text-blue-400 flex-shrink-0 mt-0.5" />
                    <div>
                        <p className="text-blue-300 font-medium">Automated Backups</p>
                        <p className="text-blue-200/70 text-sm mt-1">
                            Backups are automatically created daily at 3:00 AM. You can also create
                            manual backups anytime using the button above.
                        </p>
                    </div>
                </div>
            </div>
        </div>
    );
}
