"use client";

import { useEffect, useState } from "react";
import { useParams } from "next/navigation";
import { Plus, RefreshCcw, ExternalLink, AlertCircle, Trash2, RotateCcw } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Alert, AlertDescription } from "@/components/ui/alert";
import { Modal, ModalContent, ModalHeader, ModalTitle, ModalFooter } from "@/components/ui/modal";
import { toast } from "sonner";
import { useOrg } from "@/components/providers/org-provider";

interface Project {
    id: string;
    name: string;
    org_id?: string;
    status: string;
    api_url?: string;
    db_url?: string;
    realtime_url?: string;
    created_at: string;
}

export default function OrgProjectsPage() {
    const params = useParams();
    const orgId = params.orgId as string;
    const { currentOrg } = useOrg();

    const [projects, setProjects] = useState<Project[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);
    const [projectToDelete, setProjectToDelete] = useState<Project | null>(null);
    const [actionLoading, setActionLoading] = useState<string | null>(null);

    const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

    const fetchProjects = async () => {
        setLoading(true);
        setError(null);
        try {
            const token = localStorage.getItem("token");
            if (!token) {
                setError("Not authenticated. Please log in.");
                setLoading(false);
                return;
            }

            const response = await fetch(`${API_URL}/api/v1/projects?org_id=${orgId}`, {
                headers: {
                    "Authorization": `Bearer ${token}`
                }
            });
            if (!response.ok) throw new Error("Failed to fetch projects");
            const data: Project[] = await response.json();

            // Set projects directly (backend handles filtering)
            setProjects(Array.isArray(data) ? data : []);
        } catch (err: any) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        if (orgId) {
            fetchProjects();
        }
    }, [orgId]);

    const handleDelete = async () => {
        if (!projectToDelete) return;
        setActionLoading(projectToDelete.id);
        try {
            const token = localStorage.getItem("token");
            const resp = await fetch(`${API_URL}/api/v1/projects/${projectToDelete.id}`, {
                method: "DELETE",
                headers: {
                    "Authorization": `Bearer ${token}`
                }
            });
            if (resp.ok) {
                toast.success("Project deleted successfully");
                setProjects(projects.filter(p => p.id !== projectToDelete.id));
            } else {
                const res = await resp.json();
                toast.error(res.detail || "Failed to delete project");
            }
        } catch (err) {
            toast.error("Network error");
        } finally {
            setActionLoading(null);
            setProjectToDelete(null);
        }
    };

    const handleRestore = async (project: Project) => {
        setActionLoading(project.id);
        try {
            const token = localStorage.getItem("token");
            const resp = await fetch(`${API_URL}/api/v1/projects/${project.id}/restore`, {
                method: "POST",
                headers: {
                    "Authorization": `Bearer ${token}`
                }
            });
            if (resp.ok) {
                toast.success("Project restored");
                fetchProjects(); // Refresh to get updated status
            } else {
                const res = await resp.json();
                toast.error(res.detail || "Failed to restore project");
            }
        } catch (err) {
            toast.error("Network error");
        } finally {
            setActionLoading(null);
        }
    };

    const getStatusColor = (status: string) => {
        switch (status) {
            case "running": return "bg-emerald-100 text-emerald-700 dark:bg-emerald-500/20 dark:text-emerald-400";
            case "stopped": return "bg-slate-100 text-slate-700 dark:bg-slate-800 dark:text-slate-400";
            case "failed": return "bg-red-100 text-red-700 dark:bg-red-500/20 dark:text-red-400";
            case "provisioning": return "bg-amber-100 text-amber-700 dark:bg-amber-500/20 dark:text-amber-400";
            default: return "bg-slate-100 text-slate-600";
        }
    };

    return (
        <div className="container mx-auto px-4 md:px-8 py-8 space-y-8 animate-in fade-in duration-500">
            <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
                <div>
                    <h2 className="text-2xl md:text-3xl font-bold tracking-tight">Projects</h2>
                    <p className="text-sm text-muted-foreground">Manage your Supabase instances in {currentOrg?.name}.</p>
                </div>
                <button
                    onClick={() => window.location.href = `/org/${orgId}/projects/new`}
                    className="bg-primary text-primary-foreground px-4 py-2 rounded-lg font-medium flex items-center justify-center gap-2 hover:opacity-90 transition-all shadow-lg hover:shadow-primary/20 w-full sm:w-auto"
                >
                    <Plus size={18} />
                    New Project
                </button>
            </div>

            {loading ? (
                <div className="flex justify-center p-12">
                    <RefreshCcw className="animate-spin text-muted-foreground" />
                </div>
            ) : error ? (
                <Alert variant="destructive">
                    <AlertCircle className="h-4 w-4" />
                    <AlertDescription className="flex items-center justify-between">
                        <span>{error}</span>
                        <Button variant="outline" size="sm" onClick={fetchProjects} className="ml-4">
                            <RefreshCcw className="h-4 w-4 mr-2" /> Retry
                        </Button>
                    </AlertDescription>
                </Alert>
            ) : projects.length === 0 ? (
                <div className="bg-card border border-dashed border-border/60 rounded-xl p-16 text-center space-y-4">
                    <div className="text-muted-foreground">No projects found in this organization.</div>
                    <Button variant="ghost" className="text-primary hover:underline hover:bg-transparent p-0 h-auto" onClick={() => window.location.href = `/org/${orgId}/projects/new`}>
                        Create your first project
                    </Button>
                </div>
            ) : (
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    {projects.map((project) => (
                        <div key={project.id} className="bg-card/80 dark:bg-card border-2 border-border rounded-xl p-5 md:p-6 hover:border-primary/50 hover:shadow-lg transition-all group flex flex-col h-full shadow-md">
                            <div className="flex justify-between items-start mb-4">
                                <div className="space-y-1">
                                    <h3 className="font-bold text-lg leading-none tracking-tight">
                                        {project.name || "Untitled Project"}
                                    </h3>
                                    <p className="text-xs font-mono text-muted-foreground">ID: {project.id.substring(0, 8)}</p>
                                </div>
                                <span className={`px-2.5 py-0.5 rounded-full text-[10px] font-bold uppercase tracking-wider ${getStatusColor(project.status)}`}>
                                    {project.status}
                                </span>
                            </div>

                            <div className="space-y-4 flex-1">
                                {project.api_url && (
                                    <div className="flex items-center justify-between p-2 bg-muted/40 rounded-md border border-border/20">
                                        <span className="text-xs font-medium text-muted-foreground">API Endpoint</span>
                                        <a href={project.api_url} target="_blank" className="text-xs text-primary hover:underline flex items-center gap-1">
                                            Open <ExternalLink size={10} />
                                        </a>
                                    </div>
                                )}
                            </div>

                            <div className="mt-6 flex items-center gap-2 pt-4 border-t border-border/40">
                                <Button
                                    className="flex-1 bg-muted/50 hover:bg-muted text-foreground border-border/40"
                                    variant="outline"
                                    onClick={() => window.location.href = `/projects/${project.id}`}
                                >
                                    Manage
                                </Button>

                                {project.status === "deleted" ? (
                                    <Button
                                        size="icon"
                                        variant="outline"
                                        onClick={() => handleRestore(project)}
                                        disabled={actionLoading === project.id}
                                        title="Restore Project"
                                        className="text-amber-600 hover:bg-amber-50 dark:hover:bg-amber-900/20"
                                    >
                                        {actionLoading === project.id ? <RefreshCcw size={16} className="animate-spin" /> : <RotateCcw size={16} />}
                                    </Button>
                                ) : (
                                    <Button
                                        size="icon"
                                        variant="ghost"
                                        onClick={() => setProjectToDelete(project)}
                                        title="Delete Project"
                                        className="text-muted-foreground hover:text-destructive hover:bg-destructive/10"
                                    >
                                        <Trash2 size={16} />
                                    </Button>
                                )}
                            </div>
                        </div>
                    ))}
                </div>
            )}

            {/* Delete Confirmation Modal */}
            <Modal open={!!projectToDelete} onOpenChange={(open) => !open && setProjectToDelete(null)}>
                <ModalContent className="max-w-md">
                    <ModalHeader>
                        <ModalTitle className="text-destructive flex items-center gap-2">
                            <AlertCircle size={20} />
                            Delete Project
                        </ModalTitle>
                    </ModalHeader>
                    <div className="py-4">
                        <p className="text-sm text-muted-foreground">
                            Are you sure you want to delete <span className="font-bold text-foreground">{projectToDelete?.name || "this project"}</span>?
                        </p>
                        <p className="text-xs text-red-500 mt-2 font-medium">
                            This action is destructive and will remove all data associated with this project.
                        </p>
                    </div>
                    <ModalFooter className="gap-2">
                        <Button variant="ghost" onClick={() => setProjectToDelete(null)} disabled={!!actionLoading}>
                            Cancel
                        </Button>
                        <Button
                            variant="danger"
                            onClick={handleDelete}
                            disabled={!!actionLoading}
                            className="bg-destructive hover:bg-destructive/90 text-destructive-foreground"
                        >
                            {actionLoading === projectToDelete?.id ? "Deleting..." : "Delete Project"}
                        </Button>
                    </ModalFooter>
                </ModalContent>
            </Modal>
        </div>
    );
}
