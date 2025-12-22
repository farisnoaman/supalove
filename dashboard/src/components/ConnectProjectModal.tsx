"use client";

import { useEffect, useState } from "react";
import { Copy, Check, Eye, EyeOff, Terminal, Code2, Shield } from "lucide-react";
import {
    Dialog,
    DialogContent,
    DialogHeader,
    DialogTitle,
    DialogDescription,
} from "@/components/ui/dialog";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { useParams } from "next/navigation";

interface ProjectConfig {
    api_url: string;
    db_url: string;
    db_host: string;
    db_port: string;
    db_user: string;
    db_pass: string;
    anon_key: string;
    service_role_key: string;
}

interface ConnectProjectModalProps {
    open: boolean;
    onOpenChange: (open: boolean) => void;
}

export function ConnectProjectModal({ open, onOpenChange }: ConnectProjectModalProps) {
    const params = useParams();
    const projectId = params.id as string;
    const [config, setConfig] = useState<ProjectConfig | null>(null);
    const [loading, setLoading] = useState(false);
    const [showPassword, setShowPassword] = useState(false);
    const [copiedField, setCopiedField] = useState<string | null>(null);

    const API_URL = (process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000").replace(/\/$/, "");

    useEffect(() => {
        if (open && !config) {
            setLoading(true);
            const token = localStorage.getItem("token");
            fetch(`${API_URL}/api/v1/projects/${projectId}/config`, {
                headers: {
                    "Authorization": `Bearer ${token}`
                }
            })
                .then(res => res.json())
                .then(data => {
                    setConfig(data);
                    setLoading(false);
                })
                .catch(err => {
                    console.error(err);
                    setLoading(false);
                });
        }
    }, [open, projectId, config, API_URL]);

    const handleCopy = (text: string, field: string) => {
        navigator.clipboard.writeText(text);
        setCopiedField(field);
        setTimeout(() => setCopiedField(null), 2000);
    };

    return (
        <Dialog open={open} onOpenChange={onOpenChange}>
            <DialogContent className="sm:max-w-[600px] h-[500px] flex flex-col p-0 gap-0 overflow-hidden">
                <DialogHeader className="px-6 py-4 border-b border-border bg-muted/20">
                    <DialogTitle>Connect to your project</DialogTitle>
                    <DialogDescription>
                        Get the connection strings and environment variables for your app.
                    </DialogDescription>
                </DialogHeader>

                <div className="flex-1 overflow-y-auto">
                    {loading ? (
                        <div className="flex items-center justify-center h-full">
                            <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-primary"></div>
                        </div>
                    ) : !config ? (
                        <div className="p-6 text-center text-muted-foreground">
                            Failed to load configuration.
                        </div>
                    ) : (
                        <Tabs defaultValue="connection-string" className="w-full h-full flex flex-col">
                            <div className="px-6 pt-4">
                                <TabsList className="w-full justify-start border-b border-border bg-transparent p-0 h-auto rounded-none space-x-6">
                                    <TabsTrigger
                                        value="connection-string"
                                        className="rounded-none border-b-2 border-transparent data-[state=active]:border-emerald-500 data-[state=active]:text-foreground bg-transparent px-0 py-2 shadow-none transition-none"
                                    >
                                        Connection String
                                    </TabsTrigger>
                                    <TabsTrigger
                                        value="frameworks"
                                        className="rounded-none border-b-2 border-transparent data-[state=active]:border-emerald-500 data-[state=active]:text-foreground bg-transparent px-0 py-2 shadow-none transition-none"
                                    >
                                        App Frameworks
                                    </TabsTrigger>
                                </TabsList>
                            </div>

                            <TabsContent value="connection-string" className="flex-1 p-6 space-y-6 outline-none">
                                <div className="space-y-4">
                                    <div className="space-y-2">
                                        <Label>Direct Connection</Label>
                                        <div className="relative group">
                                            <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                                                <Terminal size={16} className="text-muted-foreground" />
                                            </div>
                                            <Input
                                                value={config.db_url.replace("[YOUR-PASSWORD]", showPassword ? config.db_pass : "[YOUR-PASSWORD]")}
                                                readOnly
                                                className="pl-9 pr-24 font-mono text-sm bg-muted/50"
                                            />
                                            <div className="absolute inset-y-0 right-0 flex items-center pr-1 gap-1">
                                                <Button
                                                    variant="ghost"
                                                    size="icon"
                                                    className="h-7 w-7"
                                                    onClick={() => setShowPassword(!showPassword)}
                                                >
                                                    {showPassword ? <EyeOff size={14} /> : <Eye size={14} />}
                                                </Button>
                                                <Button
                                                    variant="ghost"
                                                    size="sm"
                                                    className="h-7 px-2 text-xs font-medium"
                                                    onClick={() => handleCopy(config.db_url.replace("[YOUR-PASSWORD]", config.db_pass), "db_url")}
                                                >
                                                    {copiedField === "db_url" ? <Check size={14} /> : <Copy size={14} />}
                                                </Button>
                                            </div>
                                        </div>
                                        <p className="text-xs text-muted-foreground">
                                            Connect directly to your Postgres database. Ideal for long-running servers and VMs.
                                        </p>
                                    </div>

                                    <Separator />

                                    <div className="grid grid-cols-2 gap-4">
                                        <div className="space-y-1">
                                            <Label className="text-xs">Host</Label>
                                            <div className="flex items-center gap-2">
                                                <code className="text-sm bg-muted px-2 py-1 rounded flex-1">{config.db_host}</code>
                                                <Button variant="ghost" size="icon" className="h-6 w-6" onClick={() => handleCopy(config.db_host, "host")}>
                                                    {copiedField === "host" ? <Check size={12} /> : <Copy size={12} />}
                                                </Button>
                                            </div>
                                        </div>
                                        <div className="space-y-1">
                                            <Label className="text-xs">Port</Label>
                                            <div className="flex items-center gap-2">
                                                <code className="text-sm bg-muted px-2 py-1 rounded flex-1">{config.db_port}</code>
                                                <Button variant="ghost" size="icon" className="h-6 w-6" onClick={() => handleCopy(config.db_port, "port")}>
                                                    {copiedField === "port" ? <Check size={12} /> : <Copy size={12} />}
                                                </Button>
                                            </div>
                                        </div>
                                        <div className="space-y-1">
                                            <Label className="text-xs">User</Label>
                                            <div className="flex items-center gap-2">
                                                <code className="text-sm bg-muted px-2 py-1 rounded flex-1">{config.db_user}</code>
                                                <Button variant="ghost" size="icon" className="h-6 w-6" onClick={() => handleCopy(config.db_user, "user")}>
                                                    {copiedField === "user" ? <Check size={12} /> : <Copy size={12} />}
                                                </Button>
                                            </div>
                                        </div>
                                        <div className="space-y-1">
                                            <Label className="text-xs">Password</Label>
                                            <div className="flex items-center gap-2">
                                                <code className="text-sm bg-muted px-2 py-1 rounded flex-1 truncate">
                                                    {showPassword ? config.db_pass : "••••••••"}
                                                </code>
                                                <Button variant="ghost" size="icon" className="h-6 w-6" onClick={() => handleCopy(config.db_pass, "pass")}>
                                                    {copiedField === "pass" ? <Check size={12} /> : <Copy size={12} />}
                                                </Button>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </TabsContent>

                            <TabsContent value="frameworks" className="flex-1 p-6 space-y-6 outline-none">
                                <div className="space-y-4">
                                    <div className="space-y-2">
                                        <Label>Project URL</Label>
                                        <div className="relative">
                                            <Input value={config.api_url} readOnly className="pr-10 font-mono text-sm bg-muted/50" />
                                            <Button
                                                variant="ghost"
                                                size="icon"
                                                className="absolute right-1 top-1 h-7 w-7"
                                                onClick={() => handleCopy(config.api_url, "api_url")}
                                            >
                                                {copiedField === "api_url" ? <Check size={14} /> : <Copy size={14} />}
                                            </Button>
                                        </div>
                                        <p className="text-xs text-muted-foreground">
                                            REST API endpoint for your project.
                                        </p>
                                    </div>

                                    <div className="space-y-2">
                                        <Label>Anon Key (Public)</Label>
                                        <div className="relative">
                                            <Input value={config.anon_key} readOnly className="pr-10 font-mono text-sm bg-muted/50 truncate" />
                                            <Button
                                                variant="ghost"
                                                size="icon"
                                                className="absolute right-1 top-1 h-7 w-7"
                                                onClick={() => handleCopy(config.anon_key, "anon_key")}
                                            >
                                                {copiedField === "anon_key" ? <Check size={14} /> : <Copy size={14} />}
                                            </Button>
                                        </div>
                                        <p className="text-xs text-muted-foreground">
                                            Safe to use in browsers and client-side code.
                                        </p>
                                    </div>

                                    <div className="space-y-2">
                                        <Label>Service Role Key (Secret)</Label>
                                        <div className="relative">
                                            <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none z-10">
                                                <Shield size={14} className="text-amber-500" />
                                            </div>
                                            <Input
                                                value={showPassword ? config.service_role_key : "•".repeat(64)}
                                                readOnly
                                                className="pl-9 pr-24 font-mono text-sm bg-muted/50 truncate"
                                            />
                                            <div className="absolute inset-y-0 right-0 flex items-center pr-1 gap-1">
                                                <Button
                                                    variant="ghost"
                                                    size="icon"
                                                    className="h-7 w-7"
                                                    onClick={() => setShowPassword(!showPassword)}
                                                >
                                                    {showPassword ? <EyeOff size={14} /> : <Eye size={14} />}
                                                </Button>
                                                <Button
                                                    variant="ghost"
                                                    size="icon"
                                                    className="h-7 w-7"
                                                    onClick={() => handleCopy(config.service_role_key, "service_key")}
                                                >
                                                    {copiedField === "service_key" ? <Check size={14} /> : <Copy size={14} />}
                                                </Button>
                                            </div>
                                        </div>
                                        <p className="text-xs text-muted-foreground text-amber-600 dark:text-amber-500">
                                            Full access to your database. Never share this key or use it in the browser.
                                        </p>
                                    </div>
                                </div>
                            </TabsContent>
                        </Tabs>
                    )}
                </div>
            </DialogContent>
        </Dialog>
    );
}

function Separator() {
    return <div className="h-[1px] w-full bg-border" />;
}
