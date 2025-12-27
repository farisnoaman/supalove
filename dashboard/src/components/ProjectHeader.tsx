"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { useParams } from "next/navigation";
import { Plug, Circle } from "lucide-react";
import { ConnectProjectModal } from "./ConnectProjectModal";
import { Button } from "./ui/button";
import { Badge } from "./ui/badge";
import { UserNav } from "./UserNav";

export function ProjectHeader() {
    const params = useParams();
    const projectId = params.id as string;
    const [status, setStatus] = useState<string>("loading");
    const [projectName, setProjectName] = useState<string>("");
    const [isConnectOpen, setIsConnectOpen] = useState(false);

    const API_URL = (process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000").replace(/\/$/, "");

    useEffect(() => {
        // Simple status fetch to show state badge in header
        const fetchStatus = async () => {
            try {
                const token = localStorage.getItem("token");
                const resp = await fetch(`${API_URL}/api/v1/projects/${projectId}`, {
                    headers: { "Authorization": `Bearer ${token}` }
                });
                if (resp.ok) {
                    const data = await resp.json();
                    setStatus(data.status);
                    setProjectName(data.name || "Unnamed Project");
                }
            } catch (e) {
                console.error(e);
            }
        };
        fetchStatus();
    }, [projectId, API_URL]);

    return (
        <>
            <header className="h-14 border-b border-border bg-card/30 backdrop-blur-sm flex items-center px-4 md:px-8 sticky top-0 z-10">
                {/* Spacer for mobile menu button which lives in sidebar */}
                <div className="w-10 lg:hidden" />

                <div className="flex items-center gap-3 flex-1 min-w-0">
                    <div className="flex flex-col min-w-0">
                        <div className="flex items-center gap-2">
                            <span className="font-semibold text-foreground truncate">
                                {projectName || projectId}
                            </span>
                            <Badge variant="outline" className="gap-1.5 hidden sm:inline-flex">
                                <Circle size={6} className={
                                    status === "running" ? "fill-emerald-500 text-emerald-500" :
                                        status === "failed" ? "fill-red-500 text-red-500" :
                                            "fill-amber-500 text-amber-500"
                                } />
                                <span className="capitalize">{status}</span>
                            </Badge>
                        </div>
                        {projectName && (
                            <span className="text-xs font-mono text-muted-foreground/70 truncate">
                                {projectId}
                            </span>
                        )}
                    </div>
                </div>

                <div className="flex items-center gap-4">
                    <Button
                        size="sm"
                        variant="outline"
                        className="h-8 gap-2 border-emerald-500/20 text-emerald-600 hover:bg-emerald-500/5 hover:text-emerald-700 dark:text-emerald-400 dark:hover:text-emerald-300"
                        onClick={() => setIsConnectOpen(true)}
                    >
                        <Plug size={14} />
                        <span>Connect</span>
                    </Button>

                    <UserNav />
                </div>
            </header>

            <ConnectProjectModal open={isConnectOpen} onOpenChange={setIsConnectOpen} />
        </>
    );
}
