"use client";

import { useParams } from "next/navigation";
import { useState, useEffect } from "react";
import { Download, Clock, Database, HardDrive, RefreshCw, Shield, ArrowRight, Zap } from "lucide-react";
import { toast } from "sonner";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Skeleton } from "@/components/ui/skeleton";
import { cn } from "@/lib/utils";

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

    const API_URL = (process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000").replace(/\/$/, "");

    const fetchBackups = async () => {
        try {
            const res = await fetch(`${API_URL}/api/v1/projects/${projectId}/backups`);
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
            const res = await fetch(`${API_URL}/api/v1/projects/${projectId}/backups`, {
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
        <div className="space-y-10 animate-in fade-in slide-in-from-bottom-4 duration-700 max-w-5xl">
            {/* Hero Section */}
            <div className="relative p-8 rounded-3xl bg-card border border-border/40 overflow-hidden shadow-2xl glass">
                <div className="absolute top-0 right-0 w-64 h-64 bg-primary/5 rounded-full -translate-y-1/2 translate-x-1/2 blur-3xl" />
                <div className="relative z-10 flex flex-col md:flex-row md:items-center justify-between gap-6">
                    <div>
                        <Badge variant="success" className="mb-4">
                            <Shield size={12} className="mr-1.5 fill-emerald-500" />
                            Data Protected
                        </Badge>
                        <h1 className="text-4xl font-black tracking-tight text-gradient">Backups</h1>
                        <p className="text-muted-foreground mt-2 max-w-md">
                            Manage database and storage backups for your project. Create point-in-time snapshots of your entire infrastructure.
                        </p>
                    </div>
                    <div className="flex items-center gap-3">
                        <Button
                            onClick={createBackup}
                            disabled={creating}
                            className="primary-gradient shadow-lg shadow-emerald-500/20 min-w-[140px]"
                        >
                            {creating ? (
                                <RefreshCw className="h-4 w-4 animate-spin mr-2" />
                            ) : (
                                <RefreshCw className="h-4 w-4 mr-2" />
                            )}
                            {creating ? "Creating..." : "Create Backup"}
                        </Button>
                    </div>
                </div>
            </div>

            {/* Stats Cards */}
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                {[
                    { label: "Database Backups", icon: Database, color: "text-blue-500", bg: "bg-blue-50 dark:bg-blue-500/10", count: backups.filter((b) => getBackupType(b.name) === "database").length },
                    { label: "Storage Backups", icon: HardDrive, color: "text-purple-500", bg: "bg-purple-50 dark:bg-purple-500/10", count: backups.filter((b) => getBackupType(b.name) === "storage").length },
                    { label: "Total Backups", icon: Clock, color: "text-emerald-500", bg: "bg-emerald-50 dark:bg-emerald-500/10", count: backups.length }
                ].map((stat, i) => (
                    <div key={i} className="bg-card border border-border/40 rounded-2xl p-6 shadow-sm hover:shadow-md transition-all">
                        <div className="flex items-center gap-4">
                            <div className={cn("p-3 rounded-xl", stat.bg)}>
                                <stat.icon className={cn("h-6 w-6", stat.color)} />
                            </div>
                            <div>
                                <p className="text-muted-foreground text-xs font-bold uppercase tracking-wider">{stat.label}</p>
                                <p className="text-2xl font-black text-foreground">{stat.count}</p>
                            </div>
                        </div>
                    </div>
                ))}
            </div>

            {/* Backups List */}
            <div className="bg-card border border-border/40 rounded-2xl overflow-hidden shadow-sm">
                <div className="p-6 border-b border-border/20 bg-muted/30 flex items-center justify-between">
                    <h2 className="text-lg font-bold">Backup History</h2>
                    <Badge variant="outline" className="bg-background">
                        {backups.length} archived
                    </Badge>
                </div>

                {loading ? (
                    <div className="p-12 space-y-4">
                        <Skeleton className="h-8 w-full" />
                        <Skeleton className="h-20 w-full" />
                    </div>
                ) : backups.length === 0 ? (
                    <div className="p-20 text-center flex flex-col items-center">
                        <div className="w-16 h-16 rounded-full bg-muted flex items-center justify-center mb-4">
                            <Download className="h-8 w-8 text-muted-foreground" />
                        </div>
                        <h3 className="text-sm font-bold">No backups created yet</h3>
                        <p className="text-xs text-muted-foreground mt-2 max-w-[240px]">
                            Create your first snapshot to secure your project's data and storage assets.
                        </p>
                    </div>
                ) : (
                    <div className="overflow-x-auto">
                        <table className="w-full text-left">
                            <thead className="bg-muted/50 border-b border-border/20">
                                <tr>
                                    <th className="px-6 py-4 text-[10px] font-bold text-muted-foreground uppercase tracking-widest">Type</th>
                                    <th className="px-6 py-4 text-[10px] font-bold text-muted-foreground uppercase tracking-widest">Snapshot Name</th>
                                    <th className="px-6 py-4 text-[10px] font-bold text-muted-foreground uppercase tracking-widest text-right">Size</th>
                                    <th className="px-6 py-4 text-[10px] font-bold text-muted-foreground uppercase tracking-widest text-right">Created At</th>
                                </tr>
                            </thead>
                            <tbody className="divide-y divide-border/10">
                                {backups.map((backup, idx) => {
                                    const type = getBackupType(backup.name);
                                    return (
                                        <tr key={idx} className="hover:bg-muted/30 transition-colors group">
                                            <td className="px-6 py-4 whitespace-nowrap">
                                                <div className="flex items-center gap-2">
                                                    {type === "database" ? (
                                                        <Database className="h-4 w-4 text-blue-500" />
                                                    ) : (
                                                        <HardDrive className="h-4 w-4 text-purple-500" />
                                                    )}
                                                    <span className="text-xs font-semibold capitalize text-foreground">
                                                        {type}
                                                    </span>
                                                </div>
                                            </td>
                                            <td className="px-6 py-4">
                                                <code className="text-[11px] text-muted-foreground font-mono bg-muted/50 px-1.5 py-0.5 rounded">
                                                    {backup.name.split('/').pop()}
                                                </code>
                                            </td>
                                            <td className="px-6 py-4 whitespace-nowrap text-xs text-right font-medium text-foreground">
                                                {formatSize(backup.size)}
                                            </td>
                                            <td className="px-6 py-4 whitespace-nowrap text-xs text-right text-muted-foreground">
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
            <div className="bg-emerald-500/5 border border-emerald-500/10 rounded-2xl p-6 flex gap-4">
                <div className="p-2 bg-emerald-500/10 rounded-lg h-fit">
                    <Zap className="h-5 w-5 text-emerald-500 fill-emerald-500" />
                </div>
                <div>
                    <h4 className="text-sm font-bold text-foreground">Automated Maintenance</h4>
                    <p className="text-xs text-muted-foreground mt-1 leading-relaxed max-w-2xl">
                        Your project is protected with daily automated snapshots at 3:00 AM UTC.
                        Each snapshot includes the full PostgreSQL schema and MinIO storage volumes.
                    </p>
                </div>
            </div>
        </div>
    );
}

