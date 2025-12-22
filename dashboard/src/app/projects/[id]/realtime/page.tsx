"use client";

import { useEffect, useState, useCallback } from "react";
import { useParams } from "next/navigation";
import {
    Wifi, WifiOff, Play, Square, Trash2, Plus, RefreshCw,
    Database, Bell, Loader2, ChevronRight, Code2
} from "lucide-react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Breadcrumb } from "@/components/ui/breadcrumb";
import { Badge } from "@/components/ui/badge";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { RealtimeStatus } from "@/components/RealtimeStatus";
import { toast, Toaster } from "sonner";
import { cn } from "@/lib/utils";

interface RealtimeEvent {
    id: string;
    type: "INSERT" | "UPDATE" | "DELETE" | "*";
    table: string;
    timestamp: Date;
    payload: any;
}

interface Subscription {
    id: string;
    table: string;
    event: "*" | "INSERT" | "UPDATE" | "DELETE";
    active: boolean;
}

export default function RealtimePage() {
    const params = useParams();
    const projectId = params.id as string;

    const [tables, setTables] = useState<string[]>([]);
    const [subscriptions, setSubscriptions] = useState<Subscription[]>([]);
    const [events, setEvents] = useState<RealtimeEvent[]>([]);
    const [loading, setLoading] = useState(true);
    const [wsConnection, setWsConnection] = useState<WebSocket | null>(null);
    const [isConnected, setIsConnected] = useState(false);
    const [realtimeUrl, setRealtimeUrl] = useState("");

    // New subscription form
    const [newTable, setNewTable] = useState("");
    const [newEvent, setNewEvent] = useState<"*" | "INSERT" | "UPDATE" | "DELETE">("*");

    const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

    useEffect(() => {
        fetchTables();
        fetchConfig();
    }, [projectId]);

    const fetchTables = async () => {
        try {
            const token = localStorage.getItem("token");
            const resp = await fetch(`${API_URL}/api/v1/projects/${projectId}/tables`, {
                headers: { "Authorization": `Bearer ${token}` }
            });
            if (resp.ok) {
                const data = await resp.json();
                setTables(data.map((t: any) => t.table_name));
            }
        } catch (err) {
            console.error("Failed to fetch tables", err);
        } finally {
            setLoading(false);
        }
    };

    const fetchConfig = async () => {
        try {
            const token = localStorage.getItem("token");
            const resp = await fetch(`${API_URL}/api/v1/projects/${projectId}/config`, {
                headers: { "Authorization": `Bearer ${token}` }
            });
            if (resp.ok) {
                const config = await resp.json();
                setRealtimeUrl(config.realtime_url || "");
            }
        } catch (err) {
            console.error("Failed to fetch config", err);
        }
    };

    const addSubscription = () => {
        if (!newTable) {
            toast.error("Please select a table");
            return;
        }

        const sub: Subscription = {
            id: `${newTable}-${newEvent}-${Date.now()}`,
            table: newTable,
            event: newEvent,
            active: false
        };

        setSubscriptions(prev => [...prev, sub]);
        setNewTable("");
        toast.success(`Added subscription for ${newTable}`);
    };

    const removeSubscription = (id: string) => {
        setSubscriptions(prev => prev.filter(s => s.id !== id));
        toast.success("Subscription removed");
    };

    const toggleSubscription = (id: string) => {
        setSubscriptions(prev =>
            prev.map(s => s.id === id ? { ...s, active: !s.active } : s)
        );
    };

    const simulateEvent = (sub: Subscription) => {
        // Simulate receiving an event for testing
        const event: RealtimeEvent = {
            id: `evt-${Date.now()}`,
            type: sub.event === "*" ? "INSERT" : sub.event,
            table: sub.table,
            timestamp: new Date(),
            payload: {
                id: Math.floor(Math.random() * 1000),
                message: "Simulated event data",
                created_at: new Date().toISOString()
            }
        };

        setEvents(prev => [event, ...prev].slice(0, 50)); // Keep last 50 events
        toast.success(`Received ${event.type} on ${event.table}`);
    };

    const clearEvents = () => {
        setEvents([]);
        toast.success("Events cleared");
    };

    const formatEventPayload = (payload: any) => {
        try {
            return JSON.stringify(payload, null, 2);
        } catch {
            return String(payload);
        }
    };

    return (
        <div className="space-y-8 animate-in fade-in slide-in-from-bottom-4 duration-700">
            <Toaster richColors position="top-right" />

            {/* Breadcrumb */}
            <Breadcrumb
                items={[
                    { label: "Overview", href: `/projects/${projectId}` },
                    { label: "Realtime" },
                ]}
            />

            {/* Header */}
            <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
                <div>
                    <h1 className="text-3xl font-bold flex items-center gap-3">
                        <div className="p-2 bg-purple-500/10 rounded-xl">
                            <Bell size={28} className="text-purple-500" />
                        </div>
                        Realtime
                    </h1>
                    <p className="text-muted-foreground mt-1">
                        Test and monitor real-time subscriptions
                    </p>
                </div>

                <RealtimeStatus projectId={projectId} />
            </div>

            {/* Connection Info Card */}
            <div className="p-6 bg-card border border-border/40 rounded-2xl">
                <div className="flex items-center justify-between">
                    <div>
                        <h3 className="font-bold text-lg">WebSocket Connection</h3>
                        <p className="text-sm text-muted-foreground mt-1">
                            {realtimeUrl || "Not configured"}
                        </p>
                    </div>
                    <Badge
                        variant={isConnected ? "default" : "secondary"}
                        className={cn(
                            "text-xs",
                            isConnected ? "bg-green-500/10 text-green-600" : "bg-yellow-500/10 text-yellow-600"
                        )}
                    >
                        {isConnected ? "Connected" : "Ready to connect"}
                    </Badge>
                </div>
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
                {/* Subscriptions Panel */}
                <div className="space-y-4">
                    <div className="flex items-center justify-between">
                        <h2 className="text-xl font-bold">Subscriptions</h2>
                        <Badge variant="secondary" className="text-xs">
                            {subscriptions.filter(s => s.active).length} active
                        </Badge>
                    </div>

                    {/* Add Subscription Form */}
                    <div className="p-4 bg-card border border-border/40 rounded-xl space-y-4">
                        <div className="flex gap-2">
                            <Select value={newTable} onValueChange={setNewTable}>
                                <SelectTrigger className="flex-1">
                                    <SelectValue placeholder="Select table" />
                                </SelectTrigger>
                                <SelectContent>
                                    {tables.map(table => (
                                        <SelectItem key={table} value={table}>
                                            {table}
                                        </SelectItem>
                                    ))}
                                </SelectContent>
                            </Select>

                            <Select value={newEvent} onValueChange={(v: any) => setNewEvent(v)}>
                                <SelectTrigger className="w-32">
                                    <SelectValue />
                                </SelectTrigger>
                                <SelectContent>
                                    <SelectItem value="*">All</SelectItem>
                                    <SelectItem value="INSERT">INSERT</SelectItem>
                                    <SelectItem value="UPDATE">UPDATE</SelectItem>
                                    <SelectItem value="DELETE">DELETE</SelectItem>
                                </SelectContent>
                            </Select>

                            <Button onClick={addSubscription} className="shrink-0">
                                <Plus size={16} className="mr-1" />
                                Add
                            </Button>
                        </div>
                    </div>

                    {/* Subscription List */}
                    <div className="space-y-2">
                        {subscriptions.length === 0 ? (
                            <div className="p-8 text-center text-muted-foreground border border-dashed border-border/40 rounded-xl">
                                <Bell size={32} className="mx-auto mb-2 opacity-50" />
                                <p className="text-sm">No subscriptions yet</p>
                                <p className="text-xs mt-1">Add a table to start listening</p>
                            </div>
                        ) : (
                            subscriptions.map(sub => (
                                <div
                                    key={sub.id}
                                    className={cn(
                                        "p-4 border rounded-xl flex items-center justify-between transition-all",
                                        sub.active
                                            ? "bg-green-500/5 border-green-500/30"
                                            : "bg-card border-border/40"
                                    )}
                                >
                                    <div className="flex items-center gap-3">
                                        <div className={cn(
                                            "w-2 h-2 rounded-full",
                                            sub.active ? "bg-green-500 animate-pulse" : "bg-gray-400"
                                        )} />
                                        <div>
                                            <span className="font-mono font-bold">{sub.table}</span>
                                            <Badge variant="secondary" className="ml-2 text-[10px]">
                                                {sub.event}
                                            </Badge>
                                        </div>
                                    </div>

                                    <div className="flex items-center gap-2">
                                        <Button
                                            variant="ghost"
                                            size="sm"
                                            onClick={() => simulateEvent(sub)}
                                            title="Simulate event"
                                        >
                                            <Wifi size={14} />
                                        </Button>
                                        <Button
                                            variant="ghost"
                                            size="sm"
                                            onClick={() => toggleSubscription(sub.id)}
                                        >
                                            {sub.active ? <Square size={14} /> : <Play size={14} />}
                                        </Button>
                                        <Button
                                            variant="ghost"
                                            size="sm"
                                            onClick={() => removeSubscription(sub.id)}
                                            className="text-red-500 hover:text-red-600"
                                        >
                                            <Trash2 size={14} />
                                        </Button>
                                    </div>
                                </div>
                            ))
                        )}
                    </div>
                </div>

                {/* Events Panel */}
                <div className="space-y-4">
                    <div className="flex items-center justify-between">
                        <h2 className="text-xl font-bold">Events</h2>
                        <Button variant="ghost" size="sm" onClick={clearEvents}>
                            <Trash2 size={14} className="mr-1" />
                            Clear
                        </Button>
                    </div>

                    <div className="bg-card border border-border/40 rounded-xl overflow-hidden">
                        {events.length === 0 ? (
                            <div className="p-8 text-center text-muted-foreground">
                                <Code2 size={32} className="mx-auto mb-2 opacity-50" />
                                <p className="text-sm">No events received</p>
                                <p className="text-xs mt-1">Events will appear here in real-time</p>
                            </div>
                        ) : (
                            <div className="max-h-[500px] overflow-y-auto divide-y divide-border/40">
                                {events.map(event => (
                                    <div key={event.id} className="p-4 hover:bg-muted/30 transition-colors">
                                        <div className="flex items-center justify-between mb-2">
                                            <div className="flex items-center gap-2">
                                                <Badge
                                                    variant="default"
                                                    className={cn(
                                                        "text-[10px]",
                                                        event.type === "INSERT" && "bg-green-500/10 text-green-600",
                                                        event.type === "UPDATE" && "bg-blue-500/10 text-blue-600",
                                                        event.type === "DELETE" && "bg-red-500/10 text-red-600"
                                                    )}
                                                >
                                                    {event.type}
                                                </Badge>
                                                <span className="font-mono text-sm font-bold">
                                                    {event.table}
                                                </span>
                                            </div>
                                            <span className="text-xs text-muted-foreground">
                                                {event.timestamp.toLocaleTimeString()}
                                            </span>
                                        </div>
                                        <pre className="text-xs font-mono bg-muted/50 p-2 rounded overflow-x-auto">
                                            {formatEventPayload(event.payload)}
                                        </pre>
                                    </div>
                                ))}
                            </div>
                        )}
                    </div>
                </div>
            </div>

            {/* Usage Example */}
            <div className="p-6 bg-card border border-border/40 rounded-2xl">
                <h3 className="font-bold text-lg mb-4">JavaScript Example</h3>
                <pre className="text-sm font-mono bg-muted/50 p-4 rounded-xl overflow-x-auto">
                    {`import { createClient } from '@supabase/supabase-js'

const supabase = createClient(
  '${realtimeUrl ? realtimeUrl.replace(/:\\d+$/, '') : 'YOUR_PROJECT_URL'}',
  'YOUR_ANON_KEY'
)

// Subscribe to changes
const channel = supabase
  .channel('table-changes')
  .on('postgres_changes', 
    { event: '*', schema: 'public', table: 'your_table' },
    (payload) => console.log('Change received!', payload)
  )
  .subscribe()`}
                </pre>
            </div>
        </div>
    );
}
