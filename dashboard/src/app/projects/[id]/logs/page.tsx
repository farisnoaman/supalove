"use client";

import { useEffect, useState, useRef } from "react";
import { useParams } from "next/navigation";
import {
    Terminal,
    RefreshCw,
    Play,
    Pause,
    Download,
    Search,
    Filter,
    Key
} from "lucide-react";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { Tabs, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { toast } from "sonner";
import { cn } from "@/lib/utils";
import { Breadcrumb } from "@/components/ui/breadcrumb";

const SERVICES = [
    { value: "database", label: "Database", icon: <Terminal size={14} /> },
    { value: "auth", label: "Auth", icon: <Key size={14} /> },
    { value: "api", label: "API Gateway", icon: <Key size={14} /> },
    { value: "realtime", label: "Realtime", icon: <Terminal size={14} /> },
    { value: "storage", label: "Storage", icon: <Terminal size={14} /> },
];

const LogLine = ({ line }: { line: string }) => {
    let colorClass = "text-muted-foreground";
    if (line.toUpperCase().includes("ERROR") || line.toUpperCase().includes("FATAL") || line.toUpperCase().includes("FAIL")) {
        colorClass = "text-destructive font-bold";
    } else if (line.toUpperCase().includes("WARN") || line.toUpperCase().includes("WARNING")) {
        colorClass = "text-amber-500 font-semibold";
    } else if (line.toUpperCase().includes("INFO") || line.toUpperCase().includes("LOG")) {
        colorClass = "text-foreground";
    } else if (line.toUpperCase().includes("SUCCESS") || line.toUpperCase().includes("OK")) {
        colorClass = "text-emerald-500";
    }

    return (
        <div className={cn("py-0.5 border-l-2 border-transparent hover:border-primary/30 pl-2 transition-all", colorClass)}>
            <span className="opacity-40 mr-4 select-none">[{new Date().toLocaleTimeString()}]</span>
            {line}
        </div>
    );
};

export default function LogsPage() {
    const params = useParams();
    const projectId = params.id as string;

    const [logs, setLogs] = useState<string>("");
    const [loading, setLoading] = useState(true);
    const [service, setService] = useState("database");
    const [isLive, setIsLive] = useState(false);
    const [filter, setFilter] = useState("");
    const logsEndRef = useRef<HTMLDivElement>(null);
    const intervalRef = useRef<NodeJS.Timeout | null>(null);

    const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

    const fetchLogs = async () => {
        try {
            const token = localStorage.getItem("token");
            const resp = await fetch(`${API_URL}/api/v1/projects/${projectId}/logs?service=${service}&lines=500`, {
                headers: {
                    "Authorization": `Bearer ${token}`
                }
            });
            if (resp.ok) {
                const data = await resp.json();
                setLogs(data.logs);
            } else {
                console.error("Failed to fetch logs");
            }
        } catch (err) {
            console.error(err);
        } finally {
            setLoading(false);
        }
    };

    // Initial fetch and service change
    useEffect(() => {
        setLoading(true);
        fetchLogs();
    }, [projectId, service]);

    // Live polling
    useEffect(() => {
        if (isLive) {
            intervalRef.current = setInterval(fetchLogs, 2000);
        } else {
            if (intervalRef.current) clearInterval(intervalRef.current);
        }
        return () => {
            if (intervalRef.current) clearInterval(intervalRef.current);
        };
    }, [isLive, service, projectId]);

    // Auto-scroll to bottom if live
    useEffect(() => {
        if (isLive && logsEndRef.current) {
            logsEndRef.current.scrollIntoView({ behavior: "smooth" });
        }
    }, [logs, isLive]);

    const handleDownload = () => {
        const blob = new Blob([logs], { type: "text/plain" });
        const url = URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url;
        a.download = `${projectId}-${service}-logs.txt`;
        a.click();
        URL.revokeObjectURL(url);
        toast.success("Logs downloaded");
    };

    const filteredLogs = logs.split('\n').filter(line =>
        line.toLowerCase().includes(filter.toLowerCase()) && line.trim() !== ""
    );

    return (
        <div className="space-y-8 animate-in fade-in slide-in-from-bottom-4 duration-700 h-[calc(100vh-8rem)] flex flex-col">
            {/* Breadcrumb */}
            <Breadcrumb
                items={[
                    { label: "Overview", href: `/projects/${projectId}` },
                    { label: "Logs" },
                ]}
            />

            {/* Header */}
            <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
                <div>
                    <h2 className="text-3xl font-bold tracking-tight text-gradient">Logs</h2>
                    <p className="text-sm text-muted-foreground mt-1">
                        View real-time logs from your infrastructure services.
                    </p>
                </div>

                <div className="flex items-center gap-2">
                    <Button
                        variant={isLive ? "danger" : "default"}
                        onClick={() => setIsLive(!isLive)}
                        className="gap-2 w-32 shadow-lg transition-all active:scale-95"
                    >
                        {isLive ? <Pause size={16} /> : <Play size={16} />}
                        {isLive ? "Stop Live" : "Go Live"}
                    </Button>
                    <Button variant="outline" size="icon" onClick={fetchLogs} title="Refresh Now" className="glass">
                        <RefreshCw size={16} className={cn(loading && "animate-spin")} />
                    </Button>
                    <Button variant="outline" size="icon" onClick={handleDownload} title="Download Logs" className="glass">
                        <Download size={16} />
                    </Button>
                </div>
            </div>

            <Card className="flex-1 flex flex-col overflow-hidden border-border/50 shadow-2xl glass">
                <div className="border-b border-border/50 p-4 bg-muted/30 flex flex-col md:flex-row items-center justify-between gap-4">
                    <Tabs value={service} onValueChange={setService} className="w-full md:w-auto">
                        <TabsList className="bg-background/50 border border-border/50">
                            {SERVICES.map(s => (
                                <TabsTrigger key={s.value} value={s.value} className="px-4 gap-2">
                                    {s.icon} {s.label}
                                </TabsTrigger>
                            ))}
                        </TabsList>
                    </Tabs>

                    <div className="relative w-full md:w-64">
                        <Search className="absolute left-2.5 top-2.5 h-4 w-4 text-muted-foreground" />
                        <Input
                            placeholder="Filter logs..."
                            value={filter}
                            onChange={(e) => setFilter(e.target.value)}
                            className="pl-9 bg-background/50 border-border/50 focus:border-primary/50"
                        />
                    </div>
                </div>

                <div className="flex-1 bg-card border-t border-border/40 font-mono text-xs md:text-sm p-4 overflow-auto scrollbar-thin scrollbar-thumb-primary/20 scrollbar-track-transparent">
                    {loading && !logs ? (
                        <div className="h-full flex items-center justify-center text-muted-foreground gap-2">
                            <RefreshCw className="animate-spin" /> Fetching logs...
                        </div>
                    ) : (
                        <div className="space-y-0.5">
                            {filteredLogs.length > 0 ? (
                                filteredLogs.map((line, idx) => (
                                    <LogLine key={idx} line={line} />
                                ))
                            ) : (
                                <div className="p-8 text-center text-muted-foreground opacity-50 italic">
                                    {filter ? "No matching logs found." : "No logs available."}
                                </div>
                            )}
                        </div>
                    )}
                    <div ref={logsEndRef} />
                </div>
            </Card>
        </div>
    );
}
