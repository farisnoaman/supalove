"use client";

import { useEffect, useState } from "react";
import { useParams } from "next/navigation";
import {
    Cloud, Server, Globe, Shield, RefreshCw, CheckCircle, XCircle,
    AlertCircle, ExternalLink, Copy, Loader2
} from "lucide-react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Breadcrumb } from "@/components/ui/breadcrumb";
import { Badge } from "@/components/ui/badge";
import { toast, Toaster } from "sonner";
import { cn } from "@/lib/utils";

interface DeploymentConfig {
    environment: "local" | "coolify";
    coolify_connected: boolean;
    custom_domain?: string;
    ssl_enabled: boolean;
    deployment_url?: string;
    last_deploy?: string;
}

export default function DeploymentSettingsPage() {
    const params = useParams();
    const projectId = params.id as string;

    const [config, setConfig] = useState<DeploymentConfig | null>(null);
    const [loading, setLoading] = useState(true);
    const [saving, setSaving] = useState(false);
    const [customDomain, setCustomDomain] = useState("");

    const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

    useEffect(() => {
        fetchDeploymentConfig();
    }, [projectId]);

    const fetchDeploymentConfig = async () => {
        setLoading(true);
        try {
            const token = localStorage.getItem("token");
            const resp = await fetch(`${API_URL}/api/v1/projects/${projectId}/deployment`, {
                headers: { "Authorization": `Bearer ${token}` }
            });

            if (resp.ok) {
                const data = await resp.json();
                setConfig(data);
                setCustomDomain(data.custom_domain || "");
            } else {
                // Default to local if endpoint doesn't exist yet
                setConfig({
                    environment: "local",
                    coolify_connected: false,
                    ssl_enabled: false
                });
            }
        } catch (err) {
            console.error("Failed to fetch deployment config", err);
            setConfig({
                environment: "local",
                coolify_connected: false,
                ssl_enabled: false
            });
        } finally {
            setLoading(false);
        }
    };

    const saveCustomDomain = async () => {
        setSaving(true);
        try {
            const token = localStorage.getItem("token");
            const resp = await fetch(`${API_URL}/api/v1/projects/${projectId}/deployment/domain`, {
                method: "POST",
                headers: {
                    "Authorization": `Bearer ${token}`,
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ domain: customDomain })
            });

            if (resp.ok) {
                toast.success("Custom domain saved");
                fetchDeploymentConfig();
            } else {
                toast.error("Failed to save domain");
            }
        } catch (err) {
            toast.error("Network error");
        } finally {
            setSaving(false);
        }
    };

    const redeploy = async () => {
        setSaving(true);
        try {
            const token = localStorage.getItem("token");
            const resp = await fetch(`${API_URL}/api/v1/projects/${projectId}/deployment/redeploy`, {
                method: "POST",
                headers: { "Authorization": `Bearer ${token}` }
            });

            if (resp.ok) {
                toast.success("Redeployment started");
            } else {
                toast.error("Failed to trigger redeploy");
            }
        } catch (err) {
            toast.error("Network error");
        } finally {
            setSaving(false);
        }
    };

    if (loading) {
        return (
            <div className="flex items-center justify-center h-64">
                <Loader2 className="animate-spin" size={32} />
            </div>
        );
    }

    return (
        <div className="space-y-8 animate-in fade-in slide-in-from-bottom-4 duration-700">
            <Toaster richColors position="top-right" />

            <Breadcrumb
                items={[
                    { label: "Overview", href: `/projects/${projectId}` },
                    { label: "Settings", href: `/projects/${projectId}/settings` },
                    { label: "Deployment" },
                ]}
            />

            <div>
                <h1 className="text-3xl font-bold flex items-center gap-3">
                    <div className="p-2 bg-blue-500/10 rounded-xl">
                        <Cloud size={28} className="text-blue-500" />
                    </div>
                    Deployment Settings
                </h1>
                <p className="text-muted-foreground mt-1">
                    Configure production deployment and custom domains
                </p>
            </div>

            {/* Environment Status */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div className={cn(
                    "p-6 border rounded-2xl",
                    config?.environment === "local"
                        ? "bg-blue-500/5 border-blue-500/30"
                        : "bg-card border-border/40"
                )}>
                    <div className="flex items-center gap-3 mb-4">
                        <Server size={24} className="text-blue-500" />
                        <div>
                            <h3 className="font-bold">Local Docker</h3>
                            <p className="text-xs text-muted-foreground">Development environment</p>
                        </div>
                        {config?.environment === "local" && (
                            <Badge className="ml-auto bg-blue-500/10 text-blue-600">Active</Badge>
                        )}
                    </div>
                    <p className="text-sm text-muted-foreground">
                        Projects run locally using Docker Compose. Ideal for development and testing.
                    </p>
                </div>

                <div className={cn(
                    "p-6 border rounded-2xl",
                    config?.environment === "coolify"
                        ? "bg-green-500/5 border-green-500/30"
                        : "bg-card border-border/40"
                )}>
                    <div className="flex items-center gap-3 mb-4">
                        <Cloud size={24} className="text-green-500" />
                        <div>
                            <h3 className="font-bold">Coolify</h3>
                            <p className="text-xs text-muted-foreground">Production deployment</p>
                        </div>
                        {config?.environment === "coolify" && (
                            <Badge className="ml-auto bg-green-500/10 text-green-600">Active</Badge>
                        )}
                        {!config?.coolify_connected && (
                            <Badge className="ml-auto bg-yellow-500/10 text-yellow-600">Not Connected</Badge>
                        )}
                    </div>
                    <p className="text-sm text-muted-foreground">
                        Deploy to production with Coolify. Requires COOLIFY_API_URL and COOLIFY_API_TOKEN.
                    </p>
                </div>
            </div>

            {/* Custom Domain */}
            <div className="p-6 bg-card border border-border/40 rounded-2xl space-y-4">
                <div className="flex items-center gap-3">
                    <Globe size={20} className="text-purple-500" />
                    <h3 className="font-bold text-lg">Custom Domain</h3>
                </div>

                <div className="flex gap-3">
                    <Input
                        value={customDomain}
                        onChange={(e) => setCustomDomain(e.target.value)}
                        placeholder="myapp.example.com"
                        className="flex-1"
                    />
                    <Button onClick={saveCustomDomain} disabled={saving}>
                        {saving ? <Loader2 className="animate-spin mr-2" size={16} /> : null}
                        Save Domain
                    </Button>
                </div>

                {config?.custom_domain && (
                    <div className="flex items-center gap-2 p-3 bg-muted/50 rounded-lg">
                        <CheckCircle size={16} className="text-green-500" />
                        <span className="text-sm">Domain configured: </span>
                        <a
                            href={`https://${config.custom_domain}`}
                            target="_blank"
                            rel="noopener noreferrer"
                            className="text-sm font-mono text-primary hover:underline flex items-center gap-1"
                        >
                            {config.custom_domain}
                            <ExternalLink size={12} />
                        </a>
                    </div>
                )}

                <p className="text-xs text-muted-foreground">
                    Point your domain's DNS to your Coolify server. SSL certificates are managed automatically.
                </p>
            </div>

            {/* SSL Status */}
            <div className="p-6 bg-card border border-border/40 rounded-2xl">
                <div className="flex items-center justify-between">
                    <div className="flex items-center gap-3">
                        <Shield size={20} className="text-green-500" />
                        <div>
                            <h3 className="font-bold">SSL Certificate</h3>
                            <p className="text-sm text-muted-foreground">
                                {config?.ssl_enabled
                                    ? "SSL is enabled and managed by Coolify"
                                    : "SSL will be automatically provisioned when deploying to Coolify"}
                            </p>
                        </div>
                    </div>
                    <Badge
                        className={cn(
                            config?.ssl_enabled
                                ? "bg-green-500/10 text-green-600"
                                : "bg-gray-500/10 text-gray-600"
                        )}
                    >
                        {config?.ssl_enabled ? "Enabled" : "Pending"}
                    </Badge>
                </div>
            </div>

            {/* Deployment Actions */}
            {config?.environment === "coolify" && (
                <div className="p-6 bg-card border border-border/40 rounded-2xl">
                    <div className="flex items-center justify-between">
                        <div>
                            <h3 className="font-bold">Deployment Actions</h3>
                            {config.last_deploy && (
                                <p className="text-sm text-muted-foreground">
                                    Last deployed: {new Date(config.last_deploy).toLocaleString()}
                                </p>
                            )}
                        </div>
                        <Button onClick={redeploy} disabled={saving} variant="outline">
                            <RefreshCw size={16} className="mr-2" />
                            Redeploy
                        </Button>
                    </div>
                </div>
            )}

            {/* Connection Instructions */}
            {!config?.coolify_connected && (
                <div className="p-6 bg-amber-500/5 border border-amber-500/30 rounded-2xl">
                    <div className="flex items-start gap-3">
                        <AlertCircle size={20} className="text-amber-500 mt-0.5" />
                        <div>
                            <h3 className="font-bold text-amber-700 dark:text-amber-400">
                                Coolify Not Connected
                            </h3>
                            <p className="text-sm text-amber-700/80 dark:text-amber-400/80 mt-1">
                                To enable production deployment, set these environment variables on the control plane:
                            </p>
                            <pre className="mt-3 p-3 bg-background rounded-lg text-xs font-mono">
                                {`COOLIFY_API_URL=https://coolify.yourdomain.com
COOLIFY_API_TOKEN=your-api-token`}
                            </pre>
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
}
