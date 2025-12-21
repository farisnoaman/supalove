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
    Filter
} from "lucide-react";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { Tabs, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { toast } from "sonner";
import { cn } from "@/lib/utils";

const SERVICES = [
    { value: "database", label: "Database" },
    { value: "auth", label: "Auth" },
    { value: "api", label: "API Gateway" },
    { value: "realtime", label: "Realtime" },
    { value: "storage", label: "Storage" },
];

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
            const resp = await fetch(`${API_URL}/api/v1/projects/${projectId}/logs?service=${service}&lines=500`);
            if (resp.ok) {
                const data = await resp.json();
                setLogs(data.logs);
            } else {
                // If 404 or other error, might be service not running or project issue
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
        line.toLowerCase().includes(filter.toLowerCase())
    ).join('\n');

    return (
        <div className="max-w-6xl mx-auto space-y-6 animate-in fade-in duration-500 h-[calc(100vh-8rem)] flex flex-col">
            <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
                <div>
                    <h1 className="text-3xl font-bold tracking-tight">System Logs</h1>
                    <p className="text-muted-foreground mt-1">
                        View real-time logs from your infrastructure services.
                    </p>
                </div>

                <div className="flex items-center gap-2">
                    <Button
                        variant={isLive ? "destructive" : "default"}
                        onClick={() => setIsLive(!isLive)}
                        className="gap-2 w-32"
                    >
                        {isLive ? <Pause size={16} /> : <Play size={16} />}
                        {isLive ? "Stop Live" : "Go Live"}
                    </Button>
                    <Button variant="outline" size="icon" onClick={fetchLogs} title="Refresh Now">
                        <RefreshCw size={16} className={cn(loading && "animate-spin")} />
                    </Button>
                    <Button variant="outline" size="icon" onClick={handleDownload} title="Download Logs">
                        <Download size={16} />
                    </Button>
                </div>
            </div>

            <Card className="flex-1 flex flex-col overflow-hidden border-border/50 shadow-md">
                <div className="border-b border-border/50 p-4 bg-muted/20 flex flex-col md:flex-row items-center justify-between gap-4">
                    <Tabs value={service} onValueChange={setService} className="w-full md:w-auto">
                        <TabsList className="bg-background border border-border/50">
                            {SERVICES.map(s => (
                                <TabsTrigger key={s.value} value={s.value} className="px-4">
                                    {s.label}
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
                            className="pl-9 bg-background border-border/50"
                        />
                    </div>
                </div>

                <div className="flex-1 bg-[#0d1117] text-gray-300 font-mono text-xs md:text-sm p-4 overflow-auto scrollbar-thin scrollbar-thumb-gray-700 scrollbar-track-transparent">
                    {loading && !logs ? (
                        <div className="h-full flex items-center justify-center text-muted-foreground gap-2">
                            <RefreshCw className="animate-spin" /> Fetching logs...
                        </div>
                    ) : (
                        <pre className="whitespace-pre-wrap">
                            {filteredLogs || (filter ? "No matching logs found." : "No logs available.")}
                        </pre>
                    )}
                    <div ref={logsEndRef} />
                </div>
            </Card>
        </div>
    );
}
