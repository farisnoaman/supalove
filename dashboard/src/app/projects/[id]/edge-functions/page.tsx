"use client";

import { useEffect, useState } from "react";
import { useParams } from "next/navigation";
import { Code2, Plus, Play, Trash2, RefreshCw } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Breadcrumb } from "@/components/ui/breadcrumb";
import { EmptyState } from "@/components/EmptyState";
import { Skeleton } from "@/components/ui/skeleton";
import { Toaster, toast } from "sonner";
import { Modal, ModalContent, ModalHeader, ModalTitle, ModalFooter } from "@/components/ui/modal";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";

export default function EdgeFunctionsPage() {
    const params = useParams();
    const projectId = params.id as string;

    const [functions, setFunctions] = useState<any[]>([]);
    const [loading, setLoading] = useState(true);
    const [showEditor, setShowEditor] = useState(false);
    const [editingFunction, setEditingFunction] = useState<any | null>(null);
    const [functionName, setFunctionName] = useState("");
    const [functionCode, setFunctionCode] = useState("");
    const [saving, setSaving] = useState(false);
    const [functionToDelete, setFunctionToDelete] = useState<string | null>(null);
    const [deleting, setDeleting] = useState(false);

    const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

    useEffect(() => {
        fetchFunctions();
    }, [projectId]);

    const fetchFunctions = async () => {
        setLoading(true);
        try {
            const resp = await fetch(`${API_URL}/api/v1/projects/${projectId}/functions`);
            const data = await resp.json();
            setFunctions(Array.isArray(data) ? data : []);
        } catch (err) {
            console.error("Failed to fetch functions", err);
            toast.error("Failed to load functions");
        } finally {
            setLoading(false);
        }
    };

    const openEditor = (func?: any) => {
        if (func) {
            setEditingFunction(func);
            setFunctionName(func.name);
            setFunctionCode(func.code || "");
        } else {
            setEditingFunction(null);
            setFunctionName("");
            setFunctionCode(`Deno.serve(async (req) => {
  return new Response(
    JSON.stringify({ message: "Hello from edge function!" }),
    { 
      headers: { "Content-Type": "application/json" },
    },
  );
});`);
        }
        setShowEditor(true);
    };

    const handleSave = async () => {
        if (!functionName.trim()) {
            toast.error("Function name is required");
            return;
        }

        setSaving(true);
        try {
            const url = editingFunction
                ? `${API_URL}/api/v1/projects/${projectId}/functions/${editingFunction.name}`
                : `${API_URL}/api/v1/projects/${projectId}/functions`;

            const method = editingFunction ? "PUT" : "POST";

            const resp = await fetch(url, {
                method,
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    name: functionName,
                    code: functionCode,
                }),
            });

            const result = await resp.json();

            if (resp.ok) {
                toast.success(editingFunction ? "Function updated" : "Function created");
                setShowEditor(false);
                fetchFunctions();
            } else {
                toast.error(result.detail || "Failed to save function");
            }
        } catch (err) {
            toast.error("Network error while saving function");
        } finally {
            setSaving(false);
        }
    };

    const handleDelete = async () => {
        if (!functionToDelete) return;

        setDeleting(true);
        try {
            const resp = await fetch(
                `${API_URL}/api/v1/projects/${projectId}/functions/${functionToDelete}`,
                { method: "DELETE" }
            );

            if (resp.ok) {
                toast.success("Function deleted");
                fetchFunctions();
            } else {
                toast.error("Failed to delete function");
            }
        } catch (err) {
            toast.error("Network error while deleting function");
        } finally {
            setDeleting(false);
            setFunctionToDelete(null);
        }
    };

    return (
        <div className="space-y-8 animate-in fade-in slide-in-from-bottom-4 duration-700">
            <Breadcrumb
                items={[
                    { label: "Overview", href: `/projects/${projectId}` },
                    { label: "Edge Functions" },
                ]}
            />

            <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
                <div>
                    <h2 className="text-3xl font-bold tracking-tight text-gradient">Edge Functions</h2>
                    <p className="text-sm text-muted-foreground mt-1">
                        Deploy serverless functions with Deno runtime.
                    </p>
                </div>
                <Button
                    className="gap-2 primary-gradient shadow-lg shadow-emerald-500/20 hover:scale-105 transition-all"
                    onClick={() => openEditor()}
                >
                    <Plus size={18} />
                    Create Function
                </Button>
            </div>

            {loading ? (
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    {[...Array(3)].map((_, i) => (
                        <Skeleton key={i} className="h-32 rounded-xl" />
                    ))}
                </div>
            ) : functions.length === 0 ? (
                <EmptyState
                    icon={<Code2 size={48} className="text-muted-foreground/40" />}
                    title="No edge functions yet"
                    description="Create your first serverless function to get started."
                    action={
                        <Button className="gap-2 primary-gradient" onClick={() => openEditor()}>
                            <Plus size={16} />
                            Create Function
                        </Button>
                    }
                />
            ) : (
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    {functions.map((func) => (
                        <div
                            key={func.id}
                            className="group relative flex flex-col p-6 bg-card border border-border/40 rounded-xl hover:border-primary/40 hover:shadow-xl hover:shadow-primary/5 transition-all glass"
                        >
                            <div className="flex items-start justify-between mb-4">
                                <div className="p-2.5 bg-blue-50 dark:bg-blue-500/10 rounded-lg group-hover:scale-110 transition-transform duration-300">
                                    <Code2 size={22} className="text-blue-600 dark:text-blue-400" />
                                </div>
                                <div className="flex items-center gap-2">
                                    <Button
                                        variant="ghost"
                                        size="icon"
                                        onClick={() => openEditor(func)}
                                        className="h-7 w-7 text-muted-foreground hover:text-primary opacity-0 group-hover:opacity-100 transition-all"
                                    >
                                        <RefreshCw size={14} />
                                    </Button>
                                    <Button
                                        variant="ghost"
                                        size="icon"
                                        onClick={() => setFunctionToDelete(func.name)}
                                        className="h-7 w-7 text-muted-foreground hover:text-destructive opacity-0 group group-hover:opacity-100 transition-all"
                                    >
                                        <Trash2 size={14} />
                                    </Button>
                                </div>
                            </div>
                            <div>
                                <h3 className="text-lg font-bold text-foreground mb-1">{func.name}</h3>
                                <p className="text-sm text-muted-foreground">
                                    Runtime: <span className="font-mono">{func.runtime}</span>
                                </p>
                            </div>
                            <div className="mt-4 pt-4 border-t border-border/30 flex items-center justify-between text-xs text-muted-foreground">
                                <span>v{func.version}</span>
                                <div className="flex items-center gap-1">
                                    <div className="w-1.5 h-1.5 rounded-full bg-emerald-400" />
                                    <span>Active</span>
                                </div>
                            </div>
                        </div>
                    ))}
                </div>
            )}

            {/* Function Editor Modal */}
            <Modal open={showEditor} onOpenChange={setShowEditor}>
                <ModalContent className="max-w-4xl bg-card border-border/40 shadow-2xl glass rounded-2xl p-6 max-h-[90vh] overflow-y-auto">
                    <ModalHeader className="mb-4">
                        <ModalTitle className="text-xl font-bold">
                            {editingFunction ? "Edit Function" : "Create Function"}
                        </ModalTitle>
                    </ModalHeader>
                    <div className="space-y-4">
                        <div>
                            <Label htmlFor="functionName">Function Name</Label>
                            <Input
                                id="functionName"
                                value={functionName}
                                onChange={(e) => setFunctionName(e.target.value)}
                                placeholder="my-function"
                                disabled={!!editingFunction}
                                className="mt-2"
                            />
                        </div>
                        <div>
                            <Label htmlFor="functionCode">Function Code</Label>
                            <textarea
                                id="functionCode"
                                value={functionCode}
                                onChange={(e) => setFunctionCode(e.target.value)}
                                className="w-full h-96 mt-2 px-3 py-2 bg-background border border-border/50 rounded-lg font-mono text-sm resize-none focus:outline-none focus:ring-2 focus:ring-primary/50"
                            />
                        </div>
                    </div>
                    <ModalFooter className="flex items-center justify-end gap-3 mt-6">
                        <Button variant="ghost" onClick={() => setShowEditor(false)} disabled={saving}>
                            Cancel
                        </Button>
                        <Button onClick={handleSave} disabled={saving} className="primary-gradient">
                            {saving ? "Saving..." : editingFunction ? "Update" : "Create"}
                        </Button>
                    </ModalFooter>
                </ModalContent>
            </Modal>

            {/* Delete Confirmation Modal */}
            <Modal open={!!functionToDelete} onOpenChange={(open) => !open && setFunctionToDelete(null)}>
                <ModalContent className="max-w-md bg-card border-border/40 shadow-2xl glass rounded-2xl p-6">
                    <ModalHeader className="mb-4">
                        <ModalTitle className="text-xl font-bold text-destructive">Delete Function</ModalTitle>
                    </ModalHeader>
                    <p className="text-sm text-muted-foreground">
                        Are you sure you want to delete <span className="font-mono font-bold">{functionToDelete}</span>?
                        This action cannot be undone.
                    </p>
                    <ModalFooter className="flex items-center justify-end gap-3 mt-6">
                        <Button variant="ghost" onClick={() => setFunctionToDelete(null)} disabled={deleting}>
                            Cancel
                        </Button>
                        <Button
                            onClick={handleDelete}
                            disabled={deleting}
                            className="bg-destructive text-destructive-foreground hover:bg-destructive/90"
                        >
                            {deleting ? "Deleting..." : "Delete"}
                        </Button>
                    </ModalFooter>
                </ModalContent>
            </Modal>

            <Toaster position="top-right" />
        </div>
    );
}
