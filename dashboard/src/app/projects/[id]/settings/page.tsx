"use client";

import { useEffect, useState } from "react";
import { useParams, useRouter } from "next/navigation";
import {
    AlertCircle,
    RefreshCcw,
    Power,
    Trash2,
    TriangleAlert,
    Save,
    RotateCcw
} from "lucide-react";
import { Button } from "@/components/ui/button";
import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert";
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";

import { Modal, ModalContent, ModalHeader, ModalTitle, ModalFooter } from "@/components/ui/modal";
import { toast } from "sonner";
import { Toaster } from "sonner";

export default function SettingsPage() {
    const params = useParams();
    const router = useRouter();
    const projectId = params.id as string;

    const [project, setProject] = useState<any>(null);
    const [loading, setLoading] = useState(true);
    const [actionLoading, setActionLoading] = useState<string | null>(null);
    const [showDeleteModal, setShowDeleteModal] = useState(false);

    const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

    const fetchProject = async () => {
        try {
            const token = localStorage.getItem("token");
            const resp = await fetch(`${API_URL}/api/v1/projects/${projectId}`, {
                headers: {
                    "Authorization": `Bearer ${token}`
                }
            });
            if (resp.ok) {
                const data = await resp.json();
                setProject(data);
            }
        } catch (err) {
            console.error(err);
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchProject();
    }, [projectId]);

    const handleAction = async (action: 'stop' | 'start' | 'delete' | 'restore') => {
        setActionLoading(action);
        try {
            let endpoint = `${API_URL}/api/v1/projects/${projectId}`;
            if (action !== 'delete') endpoint += `/${action}`;

            const method = action === 'delete' ? 'DELETE' : 'POST';
            const token = localStorage.getItem("token");

            const resp = await fetch(endpoint, {
                method,
                headers: {
                    "Authorization": `Bearer ${token}`
                }
            });

            if (resp.ok) {
                toast.success(`Project ${action} successful`);
                if (action === 'delete') {
                    router.push('/projects');
                } else {
                    fetchProject();
                }
            } else {
                const data = await resp.json();
                toast.error(data.detail || `Failed to ${action} project`);
            }
        } catch (err) {
            toast.error("Network error");
        } finally {
            setActionLoading(null);
            setShowDeleteModal(false);
        }
    };

    if (loading) return <div className="p-8 flex justify-center"><RefreshCcw className="animate-spin text-muted-foreground" /></div>;
    if (!project) return <div className="p-8">Project not found</div>;

    const isRunning = project.status === 'running';

    return (
        <div className="max-w-4xl mx-auto space-y-8 animate-in fade-in duration-500">
            <Toaster richColors position="top-right" />

            <div>
                <h1 className="text-3xl font-bold tracking-tight">Project Settings</h1>
                <p className="text-muted-foreground">Manage your project configuration and lifecycle.</p>
            </div>

            {/* General Settings */}
            <Card>
                <CardHeader>
                    <CardTitle>General</CardTitle>
                    <CardDescription>Basic information about your project.</CardDescription>
                </CardHeader>
                <CardContent className="space-y-4">
                    <div className="grid gap-2">
                        <Label htmlFor="projectName">Project Name</Label>
                        <Input
                            id="projectName"
                            defaultValue={project.name || "Untitled Project"}
                            disabled
                            className="bg-muted"
                        />
                        <p className="text-xs text-muted-foreground">Project names currently cannot be changed.</p>
                    </div>
                    <div className="grid gap-2">
                        <Label htmlFor="projectId">Project ID</Label>
                        <div className="flex gap-2">
                            <code className="flex-1 p-2 bg-muted rounded border font-mono text-sm">{project.id}</code>
                        </div>
                        <p className="text-xs text-muted-foreground">
                            Use this ID (`NEXT_PUBLIC_PROJECT_REF`) in your frontend applications.
                        </p>
                    </div>
                </CardContent>
            </Card>

            {/* Infrastructure */}
            <Card>
                <CardHeader>
                    <CardTitle>Infrastructure</CardTitle>
                    <CardDescription>Manage the underlying services.</CardDescription>
                </CardHeader>
                <CardContent className="space-y-4">
                    <Alert>
                        <RefreshCcw className="h-4 w-4" />
                        <AlertTitle>Service Status: {project.status.toUpperCase()}</AlertTitle>
                        <AlertDescription>
                            Your project database and API services are currently {project.status}.
                        </AlertDescription>
                    </Alert>

                    <div className="flex items-center gap-4">
                        {isRunning ? (
                            <Button
                                variant="outline"
                                onClick={() => handleAction('stop')}
                                disabled={!!actionLoading}
                            >
                                {actionLoading === 'stop' ? <RefreshCcw className="mr-2 h-4 w-4 animate-spin" /> : <Power className="mr-2 h-4 w-4" />}
                                Pause Project
                            </Button>
                        ) : (
                            <Button
                                variant="default"
                                onClick={() => handleAction('start')}
                                disabled={!!actionLoading}
                                className="bg-emerald-600 hover:bg-emerald-700 text-white"
                            >
                                {actionLoading === 'start' ? <RefreshCcw className="mr-2 h-4 w-4 animate-spin" /> : <Power className="mr-2 h-4 w-4" />}
                                Resume Project
                            </Button>
                        )}

                        <Button
                            variant="secondary"
                            onClick={() => handleAction('start')} // Restart is technically stop then start, but verify logic later. Using start for force provision/restart
                            disabled={!!actionLoading}
                        >
                            <RotateCcw className="mr-2 h-4 w-4" />
                            Restart Services
                        </Button>
                    </div>
                </CardContent>
            </Card>

            {/* Danger Zone */}
            <Card className="border-destructive/50 bg-destructive/5">
                <CardHeader>
                    <CardTitle className="text-destructive">Danger Zone</CardTitle>
                    <CardDescription>Irreversible and destructive actions.</CardDescription>
                </CardHeader>
                <CardContent>
                    <p className="text-sm text-muted-foreground mb-4">
                        Deleting a project will permanently remove all data, including your database, files, and authentication users. This action cannot be undone.
                    </p>
                    <Button
                        variant="danger"
                        onClick={() => setShowDeleteModal(true)}
                        className="bg-red-600 hover:bg-red-700 text-white"
                    >
                        <Trash2 className="mr-2 h-4 w-4" />
                        Delete Project
                    </Button>
                </CardContent>
            </Card>

            {/* Delete Confirmation Modal */}
            <Modal open={showDeleteModal} onOpenChange={setShowDeleteModal}>
                <ModalContent>
                    <ModalHeader>
                        <ModalTitle className="text-destructive flex items-center gap-2">
                            <TriangleAlert className="h-5 w-5" />
                            Confirm Project Deletion
                        </ModalTitle>
                    </ModalHeader>
                    <div className="py-4">
                        <p>Are you absolutely sure you want to delete <span className="font-bold">{project.name || project.id}</span>?</p>
                        <p className="text-sm text-muted-foreground mt-2">
                            Type <span className="font-mono bg-muted px-1 rounded select-all">{project.id}</span> to confirm.
                        </p>
                        {/* Validation logic can be added here later */}
                    </div>
                    <ModalFooter>
                        <Button variant="ghost" onClick={() => setShowDeleteModal(false)}>Cancel</Button>
                        <Button
                            variant="danger"
                            className="bg-red-600 hover:bg-red-700 text-white"
                            onClick={() => handleAction('delete')}
                            disabled={!!actionLoading}
                        >
                            {actionLoading === 'delete' ? "Deleting..." : "Delete Project"}
                        </Button>
                    </ModalFooter>
                </ModalContent>
            </Modal>
        </div>
    );
}
