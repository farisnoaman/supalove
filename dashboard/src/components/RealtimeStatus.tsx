"use client";

import { useEffect, useState, useCallback } from "react";
import { Wifi, WifiOff, RefreshCw, Loader2 } from "lucide-react";
import { cn } from "@/lib/utils";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";

interface RealtimeStatusProps {
    projectId: string;
    className?: string;
    showLabel?: boolean;
}

type ConnectionState = "connecting" | "connected" | "disconnected" | "error";

export function RealtimeStatus({ projectId, className, showLabel = true }: RealtimeStatusProps) {
    const [status, setStatus] = useState<ConnectionState>("connecting");
    const [realtimeUrl, setRealtimeUrl] = useState<string>("");
    const [lastPing, setLastPing] = useState<Date | null>(null);

    const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

    const checkConnection = useCallback(async () => {
        setStatus("connecting");
        try {
            const token = localStorage.getItem("token");

            // First get the realtime URL from project config
            const configResp = await fetch(`${API_URL}/api/v1/projects/${projectId}/config`, {
                headers: { "Authorization": `Bearer ${token}` }
            });

            if (!configResp.ok) {
                setStatus("error");
                return;
            }

            const config = await configResp.json();
            const wsUrl = config.realtime_url;

            if (!wsUrl) {
                setStatus("disconnected");
                return;
            }

            setRealtimeUrl(wsUrl);

            // Try to connect to the realtime WebSocket
            // We'll just check if we can reach the HTTP health endpoint
            const httpUrl = wsUrl.replace("ws://", "http://").replace("wss://", "https://");

            try {
                const healthResp = await fetch(`${httpUrl}/api/tenants`, {
                    method: "GET",
                    signal: AbortSignal.timeout(3000)
                });

                if (healthResp.ok || healthResp.status === 401) {
                    // 401 is expected without auth, but it means service is running
                    setStatus("connected");
                    setLastPing(new Date());
                } else {
                    setStatus("disconnected");
                }
            } catch {
                // Try websocket directly
                const ws = new WebSocket(wsUrl);

                ws.onopen = () => {
                    setStatus("connected");
                    setLastPing(new Date());
                    ws.close();
                };

                ws.onerror = () => {
                    setStatus("disconnected");
                };

                // Timeout after 3 seconds
                setTimeout(() => {
                    if (ws.readyState === WebSocket.CONNECTING) {
                        ws.close();
                        setStatus("disconnected");
                    }
                }, 3000);
            }
        } catch (err) {
            console.error("Realtime check error:", err);
            setStatus("error");
        }
    }, [projectId, API_URL]);

    useEffect(() => {
        checkConnection();

        // Check every 30 seconds
        const interval = setInterval(checkConnection, 30000);

        return () => clearInterval(interval);
    }, [checkConnection]);

    const statusConfig = {
        connecting: {
            icon: Loader2,
            color: "text-yellow-500",
            bgColor: "bg-yellow-500/10",
            label: "Connecting..."
        },
        connected: {
            icon: Wifi,
            color: "text-green-500",
            bgColor: "bg-green-500/10",
            label: "Connected"
        },
        disconnected: {
            icon: WifiOff,
            color: "text-red-500",
            bgColor: "bg-red-500/10",
            label: "Disconnected"
        },
        error: {
            icon: WifiOff,
            color: "text-gray-500",
            bgColor: "bg-gray-500/10",
            label: "Error"
        }
    };

    const config = statusConfig[status];
    const Icon = config.icon;

    return (
        <div className={cn("flex items-center gap-2", className)}>
            <div className={cn(
                "flex items-center gap-2 px-3 py-1.5 rounded-full",
                config.bgColor
            )}>
                <Icon
                    size={14}
                    className={cn(
                        config.color,
                        status === "connecting" && "animate-spin"
                    )}
                />
                {showLabel && (
                    <span className={cn("text-xs font-medium", config.color)}>
                        {config.label}
                    </span>
                )}
            </div>

            <Button
                variant="ghost"
                size="sm"
                onClick={checkConnection}
                className="h-7 w-7 p-0"
                title="Refresh connection"
            >
                <RefreshCw size={12} />
            </Button>
        </div>
    );
}

// Compact version for sidebar/header
export function RealtimeStatusBadge({ projectId }: { projectId: string }) {
    const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";
    const [isConnected, setIsConnected] = useState<boolean | null>(null);

    useEffect(() => {
        const check = async () => {
            try {
                const token = localStorage.getItem("token");
                const resp = await fetch(`${API_URL}/api/v1/projects/${projectId}/config`, {
                    headers: { "Authorization": `Bearer ${token}` }
                });
                if (resp.ok) {
                    const config = await resp.json();
                    setIsConnected(!!config.realtime_url);
                }
            } catch {
                setIsConnected(false);
            }
        };
        check();
    }, [projectId, API_URL]);

    if (isConnected === null) return null;

    return (
        <Badge
            variant={isConnected ? "default" : "secondary"}
            className={cn(
                "text-[10px] h-5",
                isConnected ? "bg-green-500/10 text-green-600" : "bg-red-500/10 text-red-600"
            )}
        >
            <Wifi size={10} className="mr-1" />
            {isConnected ? "Live" : "Offline"}
        </Badge>
    );
}
