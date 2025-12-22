"use client";

import { useEffect, useState } from "react";
import { useParams } from "next/navigation";
import {
    Folder,
    File,
    Upload,
    Trash2,
    Search,
    RefreshCw,
    HardDrive,
    ChevronRight,
    MoreHorizontal,
    Plus,
    FileIcon,
    FileText,
    Image as ImageIcon,
    FileJson,
    FolderPlus
} from "lucide-react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Breadcrumb } from "@/components/ui/breadcrumb";
import { Skeleton } from "@/components/ui/skeleton";
import { Badge } from "@/components/ui/badge";
import { Modal, ModalContent, ModalHeader, ModalTitle, ModalFooter } from "@/components/ui/modal";
import { Toaster, toast } from "sonner";
import { cn } from "@/lib/utils";

interface StorageObject {
    name: string;
    size: number;
    last_modified: string;
    is_dir: boolean;
    content_type?: string;
}

export default function StoragePage() {
    const params = useParams();
    const projectId = params.id as string;

    const [buckets, setBuckets] = useState<string[]>([]);
    const [selectedBucket, setSelectedBucket] = useState<string | null>(null);
    const [objects, setObjects] = useState<StorageObject[]>([]);
    const [loading, setLoading] = useState(true);
    const [searchQuery, setSearchQuery] = useState("");
    const [uploading, setUploading] = useState(false);
    const [objectToDelete, setObjectToDelete] = useState<string | null>(null);
    const [isDeleting, setIsDeleting] = useState(false);

    const API_URL = (process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000").replace(/\/$/, "");

    useEffect(() => {
        if (projectId) fetchBuckets();
    }, [projectId]);

    useEffect(() => {
        if (selectedBucket) {
            fetchObjects(selectedBucket);
        }
    }, [selectedBucket]);

    const fetchBuckets = async () => {
        setLoading(true);
        try {
            console.log(`Fetching buckets for project ${projectId} from ${API_URL}`);
            const token = localStorage.getItem("token");
            const resp = await fetch(`${API_URL}/api/v1/projects/${projectId}/storage/buckets`, {
                headers: {
                    "Authorization": `Bearer ${token}`
                }
            });
            if (!resp.ok) throw new Error("Failed to fetch buckets");
            const data = await resp.json();
            const bucketsList = Array.isArray(data) ? data : [];
            setBuckets(bucketsList);
            if (bucketsList.length > 0) {
                setSelectedBucket(bucketsList[0]);
            } else {
                setLoading(false);
            }
        } catch (err) {
            console.error("Storage fetch buckets error:", err);
            toast.error("Failed to load buckets");
            setLoading(false);
        }
    };

    const fetchObjects = async (bucketName: string) => {
        setLoading(true);
        try {
            console.log(`Fetching objects for bucket ${bucketName} from ${API_URL}`);
            const token = localStorage.getItem("token");
            const resp = await fetch(`${API_URL}/api/v1/projects/${projectId}/storage/buckets/${bucketName}/objects`, {
                headers: {
                    "Authorization": `Bearer ${token}`
                }
            });
            if (!resp.ok) throw new Error("Failed to fetch objects");
            const data = await resp.json();
            setObjects(Array.isArray(data) ? data : []);
        } catch (err) {
            console.error("Storage fetch objects error:", err);
            toast.error("Failed to load objects");
        } finally {
            setLoading(false);
        }
    };

    const handleUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
        const file = e.target.files?.[0];
        if (!file || !selectedBucket) return;

        setUploading(true);
        const formData = new FormData();
        formData.append("file", file);

        try {
            const token = localStorage.getItem("token");
            const resp = await fetch(`${API_URL}/api/v1/projects/${projectId}/storage/buckets/${selectedBucket}/objects`, {
                method: "POST",
                headers: {
                    "Authorization": `Bearer ${token}`
                },
                body: formData,
            });

            if (resp.ok) {
                toast.success("File uploaded successfully");
                fetchObjects(selectedBucket);
            } else {
                const errData = await resp.json();
                toast.error(`Upload failed: ${errData.detail || "Unknown error"}`);
            }
        } catch (err) {
            console.error("Upload error:", err);
            toast.error("Network error during upload");
        } finally {
            setUploading(false);
            // Reset input
            e.target.value = "";
        }
    };

    const handleDeleteObject = async () => {
        if (!objectToDelete || !selectedBucket) return;
        setIsDeleting(true);

        try {
            const token = localStorage.getItem("token");
            const resp = await fetch(`${API_URL}/api/v1/projects/${projectId}/storage/buckets/${selectedBucket}/objects/${encodeURIComponent(objectToDelete)}`, {
                method: "DELETE",
                headers: {
                    "Authorization": `Bearer ${token}`
                }
            });
            if (resp.ok) {
                toast.success("File deleted");
                fetchObjects(selectedBucket);
            } else {
                toast.error("Failed to delete file");
            }
        } catch (err) {
            toast.error("Network error");
        } finally {
            setIsDeleting(false);
            setObjectToDelete(null);
        }
    };

    const formatSize = (bytes: number) => {
        if (bytes === 0) return '0 B';
        const k = 1024;
        const sizes = ['B', 'KB', 'MB', 'GB'];
        const i = Math.floor(Math.log(bytes) / Math.log(k));
        return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
    };

    const getFileIcon = (name: string, isDir: boolean) => {
        if (isDir) return <Folder className="text-blue-500 fill-blue-500/10" size={18} />;
        const ext = name.split('.').pop()?.toLowerCase();
        if (['jpg', 'jpeg', 'png', 'svg', 'gif'].includes(ext!)) return <ImageIcon className="text-purple-500" size={18} />;
        if (ext === 'json') return <FileJson className="text-amber-500" size={18} />;
        if (ext === 'txt') return <FileText className="text-slate-500" size={18} />;
        return <File className="text-slate-400" size={18} />;
    };

    const filteredObjects = objects.filter(obj =>
        obj.name.toLowerCase().includes(searchQuery.toLowerCase())
    );

    return (
        <div className="space-y-8 animate-in fade-in slide-in-from-bottom-4 duration-700 h-full flex flex-col">
            <Breadcrumb
                items={[
                    { label: "Overview", href: `/projects/${projectId}` },
                    { label: "Storage" },
                ]}
            />

            <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
                <div>
                    <h2 className="text-3xl font-bold tracking-tight text-gradient">Storage</h2>
                    <p className="text-sm text-muted-foreground mt-1">
                        Manage files, assets, and storage buckets for your media.
                    </p>
                </div>
                <div className="flex items-center gap-2">
                    <Button variant="outline" className="gap-2 border-border/40 rounded-xl h-10">
                        <FolderPlus size={18} />
                        New Bucket
                    </Button>
                    <input
                        type="file"
                        id="file-upload"
                        className="hidden"
                        onChange={handleUpload}
                    />
                    <Button
                        onClick={() => document.getElementById('file-upload')?.click()}
                        disabled={uploading || !selectedBucket}
                        className="gap-2 primary-gradient shadow-lg shadow-emerald-500/20 hover:scale-105 transition-all h-10 px-6 rounded-xl"
                    >
                        <Upload size={18} className={cn(uploading && "animate-bounce")} />
                        {uploading ? "Uploading..." : "Upload File"}
                    </Button>
                </div>
            </div>

            <div className="flex-1 flex flex-col lg:flex-row gap-4 lg:gap-6 min-h-0 overflow-hidden">
                {/* Buckets Sidebar */}
                <div className="lg:w-64 flex flex-col gap-4">
                    <div className="p-4 bg-card border border-border/40 rounded-2xl glass">
                        <h3 className="text-[10px] font-bold uppercase tracking-widest text-muted-foreground mb-4 pl-1">Buckets</h3>
                        <div className="flex lg:flex-col gap-2 overflow-x-auto lg:overflow-x-visible pb-2 lg:pb-0">
                            {loading && buckets.length === 0 ? (
                                [...Array(3)].map((_, i) => <Skeleton key={i} className="h-10 w-24 lg:w-full flex-shrink-0 rounded-xl" />)
                            ) : buckets.length === 0 ? (
                                <p className="text-xs text-muted-foreground text-center py-4">No buckets found</p>
                            ) : (
                                buckets.map(bucket => (
                                    <button
                                        key={bucket}
                                        onClick={() => setSelectedBucket(bucket)}
                                        className={cn(
                                            "flex items-center gap-2 lg:gap-3 px-3 py-2.5 rounded-xl text-sm transition-all group flex-shrink-0 lg:flex-shrink lg:w-full",
                                            selectedBucket === bucket
                                                ? "bg-primary/10 text-primary font-bold shadow-sm"
                                                : "text-muted-foreground hover:bg-muted/50 hover:text-foreground"
                                        )}
                                    >
                                        <HardDrive size={18} className={cn(selectedBucket === bucket ? "text-primary" : "text-muted-foreground/60")} />
                                        <span className="truncate">{bucket.replace(`project-${projectId}-`, '')}</span>
                                        {selectedBucket === bucket && <ChevronRight size={14} className="ml-auto opacity-50 hidden lg:block" />}
                                    </button>
                                ))
                            )}
                        </div>
                    </div>

                    <div className="hidden lg:flex mt-auto p-4 bg-muted/30 border border-border/20 rounded-2xl flex-col gap-2">
                        <div className="flex items-center justify-between text-[10px] uppercase font-bold tracking-widest text-muted-foreground/60">
                            <span>Usage</span>
                            <span className="text-foreground">33%</span>
                        </div>
                        <div className="h-2 w-full bg-border/30 rounded-full overflow-hidden">
                            <div className="h-full w-1/3 bg-emerald-500 rounded-full shadow-[0_0_8px_rgba(16,185,129,0.4)]" />
                        </div>
                        <p className="text-[10px] text-muted-foreground/60 mt-1">1.2 GB of 5 GB used</p>
                    </div>
                </div>

                {/* File Browser */}
                <div className="flex-1 flex flex-col bg-card border border-border/40 rounded-2xl shadow-xl glass overflow-hidden">
                    <div className="p-4 border-b border-border/40 flex items-center justify-between bg-muted/30 backdrop-blur-md">
                        <div className="relative w-72">
                            <Search className="absolute left-3 top-1/2 -translate-y-1/2 text-muted-foreground" size={14} />
                            <Input
                                placeholder="Search files..."
                                value={searchQuery}
                                onChange={(e) => setSearchQuery(e.target.value)}
                                className="pl-9 h-9 bg-card border-border/40 rounded-xl"
                            />
                        </div>
                        <div className="flex items-center gap-2">
                            <Button
                                variant="ghost"
                                size="icon"
                                onClick={() => selectedBucket && fetchObjects(selectedBucket)}
                                className="h-9 w-9 text-muted-foreground rounded-xl"
                            >
                                <RefreshCw className={cn(loading && "animate-spin")} size={16} />
                            </Button>
                        </div>
                    </div>

                    <div className="flex-1 overflow-y-auto">
                        <table className="w-full text-left">
                            <thead className="bg-muted/50 border-b border-border/40 sticky top-0 z-10 backdrop-blur-md hidden md:table-header-group">
                                <tr>
                                    <th className="px-4 md:px-6 py-3 text-[10px] font-bold uppercase tracking-widest text-muted-foreground">Name</th>
                                    <th className="px-4 md:px-6 py-3 text-[10px] font-bold uppercase tracking-widest text-muted-foreground">Size</th>
                                    <th className="px-4 md:px-6 py-3 text-[10px] font-bold uppercase tracking-widest text-muted-foreground hidden lg:table-cell">Last Modified</th>
                                    <th className="px-4 md:px-6 py-3 text-right"></th>
                                </tr>
                            </thead>
                            <tbody className="divide-y divide-border/20">
                                {loading ? (
                                    [...Array(6)].map((_, i) => (
                                        <tr key={i}>
                                            <td className="px-6 py-4"><Skeleton className="h-10 w-64 rounded-lg" /></td>
                                            <td className="px-6 py-4"><Skeleton className="h-4 w-16" /></td>
                                            <td className="px-6 py-4"><Skeleton className="h-4 w-32" /></td>
                                            <td className="px-6 py-4"></td>
                                        </tr>
                                    ))
                                ) : filteredObjects.length === 0 ? (
                                    <tr>
                                        <td colSpan={4} className="px-6 py-32 text-center">
                                            <div className="flex flex-col items-center">
                                                <div className="w-16 h-16 rounded-full bg-muted/50 flex items-center justify-center mb-4">
                                                    <Folder size={32} className="text-muted-foreground/30" />
                                                </div>
                                                <h3 className="text-lg font-bold">This bucket is empty</h3>
                                                <p className="text-sm text-muted-foreground mt-1 mb-6 max-w-xs">
                                                    Drag and drop files here to upload your first asset.
                                                </p>
                                                <Button
                                                    size="sm"
                                                    onClick={() => document.getElementById('file-upload')?.click()}
                                                    disabled={uploading || !selectedBucket}
                                                    className="primary-gradient px-8 rounded-xl"
                                                >
                                                    <Upload size={14} className={cn("mr-2", uploading && "animate-bounce")} />
                                                    {uploading ? "Uploading..." : "Upload Now"}
                                                </Button>
                                            </div>
                                        </td>
                                    </tr>
                                ) : (
                                    filteredObjects.map((obj) => (
                                        <tr key={obj.name} className="hover:bg-emerald-50/20 dark:hover:bg-emerald-500/5 transition-colors group cursor-pointer flex flex-col md:table-row p-3 md:p-0 border-b md:border-0 border-border/20">
                                            <td className="px-2 md:px-4 lg:px-6 py-2 md:py-4 text-sm font-medium">
                                                <div className="flex items-center gap-3">
                                                    {getFileIcon(obj.name, obj.is_dir)}
                                                    <span className="group-hover:text-primary transition-colors truncate max-w-[200px] md:max-w-[300px]">
                                                        {obj.name}
                                                    </span>
                                                </div>
                                            </td>
                                            <td className="px-2 md:px-4 lg:px-6 py-1 md:py-4 text-xs font-mono text-muted-foreground">
                                                <span className="md:hidden text-muted-foreground/60 mr-2">Size:</span>
                                                {obj.is_dir ? '-' : formatSize(obj.size)}
                                            </td>
                                            <td className="px-2 md:px-4 lg:px-6 py-1 md:py-4 text-xs text-muted-foreground hidden lg:table-cell">
                                                {new Date(obj.last_modified).toLocaleString()}
                                            </td>
                                            <td className="px-2 md:px-4 lg:px-6 py-2 md:py-4 text-right">
                                                <div className="flex items-center justify-end gap-1">
                                                    <Button
                                                        variant="ghost"
                                                        size="icon"
                                                        className="h-8 w-8 text-muted-foreground md:opacity-0 group-hover:opacity-100 transition-opacity rounded-lg"
                                                    >
                                                        <MoreHorizontal size={14} />
                                                    </Button>
                                                    <Button
                                                        variant="ghost"
                                                        size="icon"
                                                        onClick={(e) => {
                                                            e.stopPropagation();
                                                            setObjectToDelete(obj.name);
                                                        }}
                                                        className="h-8 w-8 text-muted-foreground hover:text-destructive md:opacity-0 group-hover:opacity-100 transition-opacity rounded-lg"
                                                    >
                                                        <Trash2 size={14} />
                                                    </Button>
                                                </div>
                                            </td>
                                        </tr>
                                    ))
                                )}
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
            {/* Delete Confirmation Modal */}
            <Modal open={!!objectToDelete} onOpenChange={(open) => !open && setObjectToDelete(null)}>
                <ModalContent className="max-w-md bg-card border-border/40 shadow-2xl glass rounded-2xl p-6">
                    <ModalHeader className="mb-4">
                        <ModalTitle className="text-xl font-bold text-destructive">Delete File</ModalTitle>
                    </ModalHeader>
                    <div className="space-y-4">
                        <p className="text-sm text-muted-foreground">
                            Are you sure you want to delete <span className="font-mono font-bold text-foreground">"{objectToDelete}"</span>? This action cannot be undone.
                        </p>
                        <ModalFooter className="flex items-center justify-end gap-3 mt-8">
                            <Button variant="ghost" onClick={() => setObjectToDelete(null)} disabled={isDeleting} className="rounded-xl">
                                Cancel
                            </Button>
                            <Button
                                onClick={handleDeleteObject}
                                disabled={isDeleting}
                                className="bg-destructive text-destructive-foreground hover:bg-destructive/90 px-6 rounded-xl shadow-lg shadow-destructive/20"
                            >
                                {isDeleting ? "Deleting..." : "Delete File"}
                            </Button>
                        </ModalFooter>
                    </div>
                </ModalContent>
            </Modal>

            <Toaster position="top-right" />
        </div>
    );
}
