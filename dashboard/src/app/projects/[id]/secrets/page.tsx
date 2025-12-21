"use client";

import { useEffect, useState } from "react";
import { useParams } from "next/navigation";
import {
    Key,
    Plus,
    Trash2,
    Eye,
    EyeOff,
    AlertCircle,
    Copy,
    Check,
    Lock
} from "lucide-react";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert";
import { Modal, ModalContent, ModalHeader, ModalTitle, ModalFooter } from "@/components/ui/modal";
import { toast } from "sonner";
import { Toaster } from "sonner";
import { cn } from "@/lib/utils";

interface Secret {
    key: string;
    value: string;
}

export default function SecretsPage() {
    const params = useParams();
    const projectId = params.id as string;

    const [secrets, setSecrets] = useState<Record<string, string>>({});
    const [loading, setLoading] = useState(true);
    const [showAddModal, setShowAddModal] = useState(false);
    const [newKey, setNewKey] = useState("");
    const [newValue, setNewValue] = useState("");
    const [adding, setAdding] = useState(false);
    const [revealed, setRevealed] = useState<Record<string, boolean>>({});
    const [copied, setCopied] = useState<string | null>(null);

    const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

    const fetchSecrets = async () => {
        try {
            const resp = await fetch(`${API_URL}/api/v1/projects/${projectId}/secrets`);
            if (resp.ok) {
                const data = await resp.json();
                setSecrets(data);
            }
        } catch (err) {
            toast.error("Failed to load secrets");
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchSecrets();
    }, [projectId]);

    const handleCopy = (value: string, key: string) => {
        navigator.clipboard.writeText(value);
        setCopied(key);
        setTimeout(() => setCopied(null), 2000);
        toast.success("Secret copied to clipboard");
    };

    const toggleReveal = (key: string) => {
        setRevealed(prev => ({ ...prev, [key]: !prev[key] }));
    };

    const handleAddSecret = async () => {
        if (!newKey || !newValue) {
            toast.error("Key and Value are required");
            return;
        }

        setAdding(true);
        try {
            const resp = await fetch(`${API_URL}/api/v1/projects/${projectId}/secrets`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ key: newKey.toUpperCase(), value: newValue }),
            });

            if (resp.ok) {
                toast.success("Secret added successfully");
                fetchSecrets();
                setShowAddModal(false);
                setNewKey("");
                setNewValue("");
            } else {
                const data = await resp.json();
                toast.error(data.detail || "Failed to add secret");
            }
        } catch (err) {
            toast.error("Network error");
        } finally {
            setAdding(false);
        }
    };

    const handleDeleteSecret = async (key: string) => {
        if (!confirm(`Are you sure you want to delete ${key}? This might break your application.`)) return;

        try {
            const resp = await fetch(`${API_URL}/api/v1/projects/${projectId}/secrets/${key}`, {
                method: "DELETE",
            });

            if (resp.ok) {
                toast.success("Secret deleted");
                fetchSecrets();
            } else {
                toast.error("Failed to delete secret");
            }
        } catch (err) {
            toast.error("Network error");
        }
    };

    return (
        <div className="max-w-5xl mx-auto space-y-8 animate-in fade-in duration-500">
            <Toaster richColors position="top-right" />

            <div className="flex justify-between items-start">
                <div>
                    <h1 className="text-3xl font-bold tracking-tight">Secrets & Environment Variables</h1>
                    <p className="text-muted-foreground mt-1">
                        Securely manage API keys and configuration for your project.
                    </p>
                </div>
                <Button onClick={() => setShowAddModal(true)} className="gap-2">
                    <Plus size={16} />
                    Add Secret
                </Button>
            </div>

            <Alert className="bg-amber-500/10 border-amber-500/50 text-amber-700 dark:text-amber-400">
                <AlertCircle className="h-4 w-4" />
                <AlertTitle>Restart Required</AlertTitle>
                <AlertDescription>
                    Changes to environment variables require a project restart to take effect.
                    Go to <a href={`/projects/${projectId}/settings`} className="font-bold hover:underline">Settings</a> to restart.
                </AlertDescription>
            </Alert>

            <Card>
                <CardHeader>
                    <CardTitle className="text-sm font-medium uppercase tracking-wider text-muted-foreground">
                        Project Secrets
                    </CardTitle>
                </CardHeader>
                <CardContent className="p-0">
                    {loading ? (
                        <div className="p-8 text-center text-muted-foreground">Loading secrets...</div>
                    ) : Object.keys(secrets).length === 0 ? (
                        <div className="p-16 text-center text-muted-foreground border-t border-border/40">
                            <Lock className="w-10 h-10 mx-auto mb-4 opacity-20" />
                            <p>No secrets defined yet.</p>
                        </div>
                    ) : (
                        <div className="divide-y divide-border/40">
                            {Object.entries(secrets).map(([key, value]) => (
                                <div key={key} className="flex items-center justify-between p-4 hover:bg-muted/30 transition-colors group">
                                    <div className="font-mono text-sm font-medium min-w-[200px] text-foreground/90">
                                        {key}
                                    </div>

                                    <div className="flex-1 mx-8 flex items-center bg-muted/50 rounded-md px-3 h-9 border border-border/20">
                                        <div className="flex-1 font-mono text-xs truncate mr-2 text-muted-foreground">
                                            {revealed[key] ? value : "••••••••••••••••••••••••••••••"}
                                        </div>
                                        <div className="flex items-center gap-1">
                                            <button
                                                onClick={() => toggleReveal(key)}
                                                className="p-1.5 hover:bg-background rounded-md text-muted-foreground hover:text-foreground transition-colors"
                                                title={revealed[key] ? "Hide" : "Show"}
                                            >
                                                {revealed[key] ? <EyeOff size={14} /> : <Eye size={14} />}
                                            </button>
                                            <button
                                                onClick={() => handleCopy(value, key)}
                                                className="p-1.5 hover:bg-background rounded-md text-muted-foreground hover:text-foreground transition-colors"
                                                title="Copy value"
                                            >
                                                {copied === key ? <Check size={14} className="text-emerald-500" /> : <Copy size={14} />}
                                            </button>
                                        </div>
                                    </div>

                                    <Button
                                        variant="ghost"
                                        size="icon"
                                        onClick={() => handleDeleteSecret(key)}
                                        className="text-muted-foreground hover:text-destructive hover:bg-destructive/10 opacity-0 group-hover:opacity-100 transition-all"
                                    >
                                        <Trash2 size={16} />
                                    </Button>
                                </div>
                            ))}
                        </div>
                    )}
                </CardContent>
            </Card>

            <Modal open={showAddModal} onOpenChange={setShowAddModal}>
                <ModalContent>
                    <ModalHeader>
                        <ModalTitle>Add New Secret</ModalTitle>
                    </ModalHeader>
                    <div className="space-y-4 py-4">
                        <div className="space-y-2">
                            <Label htmlFor="key">Name (Key)</Label>
                            <Input
                                id="key"
                                placeholder="MY_SECRET_KEY"
                                value={newKey}
                                onChange={(e) => setNewKey(e.target.value.toUpperCase())}
                                className="font-mono uppercase"
                            />
                            <p className="text-xs text-muted-foreground">
                                Keys are automatically converted to uppercase.
                            </p>
                        </div>
                        <div className="space-y-2">
                            <Label htmlFor="value">Value</Label>
                            <Input
                                id="value"
                                placeholder="secret_value_..."
                                value={newValue}
                                onChange={(e) => setNewValue(e.target.value)}
                                type="password"
                            />
                        </div>
                    </div>
                    <ModalFooter>
                        <Button variant="ghost" onClick={() => setShowAddModal(false)}>Cancel</Button>
                        <Button onClick={handleAddSecret} disabled={adding}>
                            {adding ? "Adding..." : "Add Secret"}
                        </Button>
                    </ModalFooter>
                </ModalContent>
            </Modal>
        </div>
    );
}
