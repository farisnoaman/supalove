"use client";

import { useEffect, useState } from "react";
import { useTheme } from "next-themes";
import { Mail, Github, Trash2, Command, Terminal, Database, Wand2, Monitor, Moon, Sun, AlertTriangle } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Switch } from "@/components/ui/switch";
import { toast } from "sonner";
import { cn } from "@/lib/utils";

interface UserProfile {
    id: string;
    email: string;
    full_name: string | null;
    username?: string; // fallback to email part
    preferences: {
        theme?: string;
        sidebar_behavior?: string;
        shortcuts?: {
            command_menu: boolean;
            ai_assistant: boolean;
            sql_editor: boolean;
        };
        telemetry?: boolean;
    } | null;
}

export default function ProfilePage() {
    const { theme, setTheme } = useTheme();
    const [profile, setProfile] = useState<UserProfile | null>(null);
    const [loading, setLoading] = useState(true);
    const [saving, setSaving] = useState(false);

    // Form States
    const [firstName, setFirstName] = useState("");
    const [lastName, setLastName] = useState("");
    const [sidebarBehavior, setSidebarBehavior] = useState("open");
    const [shortcuts, setShortcuts] = useState({
        command_menu: true,
        ai_assistant: true,
        sql_editor: true
    });
    const [telemetry, setTelemetry] = useState(true);

    const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

    useEffect(() => {
        fetchProfile();
    }, []);

    const fetchProfile = async () => {
        try {
            const token = localStorage.getItem("token");
            if (!token) return;

            const resp = await fetch(`${API_URL}/api/v1/users/me`, {
                headers: { "Authorization": `Bearer ${token}` }
            });

            if (!resp.ok) throw new Error("Failed");

            const data = await resp.json();
            setProfile(data);

            // Parse full name
            const names = (data.full_name || "").split(" ");
            setFirstName(names[0] || "");
            setLastName(names.slice(1).join(" ") || "");

            // Parse preferences
            if (data.preferences) {
                if (data.preferences.theme) setTheme(data.preferences.theme);
                if (data.preferences.sidebar_behavior) setSidebarBehavior(data.preferences.sidebar_behavior);
                if (data.preferences.shortcuts) setShortcuts(data.preferences.shortcuts);
                if (data.preferences.telemetry !== undefined) setTelemetry(data.preferences.telemetry);
            }
        } catch (err) {
            console.error(err);
        } finally {
            setLoading(false);
        }
    };

    const handleSave = async () => {
        setSaving(true);
        try {
            const token = localStorage.getItem("token");
            const fullName = `${firstName} ${lastName}`.trim();

            const newPrefs = {
                theme,
                sidebar_behavior: sidebarBehavior,
                shortcuts,
                telemetry
            };

            const resp = await fetch(`${API_URL}/api/v1/users/me`, {
                method: "PATCH",
                headers: {
                    "Authorization": `Bearer ${token}`,
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    full_name: fullName,
                    preferences: newPrefs
                })
            });

            if (!resp.ok) throw new Error("Failed");
            toast.success("Preferences updated");
        } catch (err) {
            toast.error("Failed to save preferences");
        } finally {
            setSaving(false);
        }
    };

    if (loading) {
        return <div className="p-8">Loading...</div>;
    }

    return (
        <div className="space-y-12 pb-20">
            <div>
                <h1 className="text-2xl font-semibold mb-1">Preferences</h1>
                <p className="text-muted-foreground text-sm">
                    Manage your account profile, connections, and dashboard experience.
                </p>
            </div>

            {/* Profile Information */}
            <div className="space-y-6">
                <h2 className="text-lg font-medium border-b border-border/50 pb-2">Profile information</h2>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-3xl">
                    <div className="space-y-2">
                        <label className="text-sm font-medium">First name</label>
                        <Input value={firstName} onChange={e => setFirstName(e.target.value)} />
                    </div>
                    <div className="space-y-2">
                        <label className="text-sm font-medium">Last name</label>
                        <Input value={lastName} onChange={e => setLastName(e.target.value)} />
                    </div>
                    <div className="space-y-2">
                        <label className="text-sm font-medium">Primary email</label>
                        <Input value={profile?.email} disabled className="bg-muted/50" />
                        <p className="text-xs text-muted-foreground">Primary email is used for account notifications.</p>
                    </div>
                    <div className="space-y-2">
                        <label className="text-sm font-medium">Username</label>
                        <Input value={profile?.email} disabled className="bg-muted/50" />
                        <p className="text-xs text-muted-foreground">Username appears as a display name throughout the dashboard.</p>
                    </div>
                </div>
                <div className="flex justify-end max-w-3xl">
                    <Button onClick={handleSave} disabled={saving} className="bg-emerald-600 hover:bg-emerald-700 text-white">
                        {saving ? "Saving..." : "Save"}
                    </Button>
                </div>
            </div>

            {/* Account Identities */}
            <div className="space-y-6">
                <h2 className="text-lg font-medium border-b border-border/50 pb-2">Account identities</h2>
                <p className="text-sm text-muted-foreground mb-4">Manage the providers linked to your Supabase account and update their details.</p>

                <div className="max-w-3xl border border-border rounded-md divide-y divide-border">
                    <div className="p-4 flex items-center justify-between bg-card hover:bg-accent/5 transition-colors">
                        <div className="flex items-center gap-4">
                            <Mail className="h-5 w-5 text-muted-foreground" />
                            <div>
                                <p className="text-sm font-medium">Email</p>
                                <p className="text-xs text-muted-foreground">{profile?.email}</p>
                            </div>
                        </div>
                        <Button variant="outline" size="sm" className="h-8">Reset password</Button>
                    </div>
                </div>
            </div>

            {/* Connections */}
            <div className="space-y-6">
                <h2 className="text-lg font-medium border-b border-border/50 pb-2">Connections</h2>
                <p className="text-sm text-muted-foreground mb-4">Connect your Supabase account with other services.</p>

                <div className="max-w-3xl border border-border rounded-md divide-y divide-border">
                    <div className="p-4 flex items-center justify-between">
                        <div className="flex items-center gap-4">
                            <Github className="h-6 w-6" />
                            <div>
                                <p className="text-sm font-medium">GitHub</p>
                                <p className="text-xs text-muted-foreground">Sync repos to Supabase projects for automatic branch creation and merging</p>
                            </div>
                        </div>
                        <Button variant="default" size="sm" className="h-8 bg-emerald-600 hover:bg-emerald-700 text-white">Connect</Button>
                    </div>
                </div>
            </div>

            {/* Appearance */}
            <div className="space-y-6">
                <h2 className="text-lg font-medium border-b border-border/50 pb-2">Appearance</h2>
                <p className="text-sm text-muted-foreground">Choose how Supabase looks and behaves in the dashboard.</p>

                <div className="max-w-3xl bg-card border border-border rounded-md p-6 space-y-6">
                    <div>
                        <label className="text-sm font-medium block mb-3">Theme mode</label>
                        <p className="text-xs text-muted-foreground mb-4">Choose how Supabase looks to you. Select a single theme, or sync with your system.</p>

                        <div className="grid grid-cols-2 gap-4">
                            {/* Dark Option */}
                            <label className={cn("relative cursor-pointer border rounded-md p-2 flex flex-col gap-2 hover:bg-accent/50 transition-all", theme === 'dark' ? "border-emerald-500 ring-1 ring-emerald-500" : "border-border")}>
                                <div className="bg-slate-900 h-24 rounded border border-slate-800 flex items-center justify-center">
                                    <div className="w-16 h-12 bg-slate-800 rounded opacity-50" />
                                </div>
                                <div className="flex items-center gap-2">
                                    <input type="radio" name="theme" checked={theme === 'dark'} onChange={() => setTheme('dark')} className="accent-emerald-500" />
                                    <span className="text-sm font-medium">Dark</span>
                                </div>
                            </label>

                            {/* Light Option */}
                            <label className={cn("relative cursor-pointer border rounded-md p-2 flex flex-col gap-2 hover:bg-accent/50 transition-all", theme === 'light' ? "border-emerald-500 ring-1 ring-emerald-500" : "border-border")}>
                                <div className="bg-white h-24 rounded border border-slate-200 flex items-center justify-center">
                                    <div className="w-16 h-12 bg-slate-100 rounded" />
                                </div>
                                <div className="flex items-center gap-2">
                                    <input type="radio" name="theme" checked={theme === 'light'} onChange={() => setTheme('light')} className="accent-emerald-500" />
                                    <span className="text-sm font-medium">Light</span>
                                </div>
                            </label>

                            {/* Classic Dark (same as dark for now) */}
                            <label className={cn("relative cursor-pointer border rounded-md p-2 flex flex-col gap-2 hover:bg-accent/50 transition-all", theme === 'classic-dark' ? "border-emerald-500 ring-1 ring-emerald-500" : "border-border")}>
                                <div className="bg-[#121212] h-24 rounded border border-slate-800 flex items-center justify-center">
                                    <div className="w-16 h-12 bg-slate-800/50 rounded" />
                                </div>
                                <div className="flex items-center gap-2">
                                    <input type="radio" name="theme" checked={false} disabled className="accent-emerald-500" />
                                    <span className="text-sm font-medium">Classic Dark</span>
                                </div>
                            </label>

                            {/* System Option */}
                            <label className={cn("relative cursor-pointer border rounded-md p-2 flex flex-col gap-2 hover:bg-accent/50 transition-all", theme === 'system' ? "border-emerald-500 ring-1 ring-emerald-500" : "border-border")}>
                                <div className="bg-gradient-to-br from-slate-900 to-white h-24 rounded border border-border flex items-center justify-center">
                                    <Monitor className="text-muted-foreground" />
                                </div>
                                <div className="flex items-center gap-2">
                                    <input type="radio" name="theme" checked={theme === 'system'} onChange={() => setTheme('system')} className="accent-emerald-500" />
                                    <span className="text-sm font-medium">System</span>
                                </div>
                            </label>
                        </div>
                    </div>

                    <div className="border-t border-border pt-6">
                        <div className="flex items-center justify-between">
                            <div className="space-y-1">
                                <label className="text-sm font-medium">Sidebar behavior</label>
                                <p className="text-xs text-muted-foreground">Choose your preferred sidebar behavior: open, closed, or expand on hover.</p>
                            </div>
                            <select
                                value={sidebarBehavior}
                                onChange={(e) => setSidebarBehavior(e.target.value)}
                                className="h-9 w-40 rounded-md border border-input bg-background px-3 py-1 text-sm shadow-sm transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring"
                            >
                                <option value="open">Open</option>
                                <option value="closed">Closed</option>
                                <option value="hover">Expand on hover</option>
                            </select>
                        </div>
                    </div>
                </div>
            </div>

            {/* Keyboard Shortcuts */}
            <div className="space-y-6">
                <h2 className="text-lg font-medium border-b border-border/50 pb-2">Keyboard shortcuts</h2>
                <p className="text-sm text-muted-foreground">Choose which shortcuts stay active while working in the dashboard.</p>

                <div className="max-w-3xl bg-card border border-border rounded-md divide-y divide-border">
                    {/* Command Menu */}
                    <div className="p-4 flex items-center justify-between">
                        <div className="flex items-center gap-4">
                            <div className="bg-muted px-2 py-1 rounded border border-border text-xs text-muted-foreground flex items-center gap-1">
                                <span>Cmd</span> <span>K</span>
                            </div>
                            <span className="text-sm font-medium">Command menu</span>
                        </div>
                        <Switch
                            checked={shortcuts.command_menu}
                            onCheckedChange={checked => setShortcuts({ ...shortcuts, command_menu: checked })}
                        />
                    </div>
                    {/* AI Assistant */}
                    <div className="p-4 flex items-center justify-between">
                        <div className="flex items-center gap-4">
                            <div className="bg-muted px-2 py-1 rounded border border-border text-xs text-muted-foreground flex items-center gap-1">
                                <span>Cmd</span> <span>I</span>
                            </div>
                            <span className="text-sm font-medium">AI Assistant Panel</span>
                        </div>
                        <Switch
                            checked={shortcuts.ai_assistant}
                            onCheckedChange={checked => setShortcuts({ ...shortcuts, ai_assistant: checked })}
                        />
                    </div>
                    {/* Inline SQL */}
                    <div className="p-4 flex items-center justify-between">
                        <div className="flex items-center gap-4">
                            <div className="bg-muted px-2 py-1 rounded border border-border text-xs text-muted-foreground flex items-center gap-1">
                                <span>Cmd</span> <span>E</span>
                            </div>
                            <span className="text-sm font-medium">Inline SQL Editor Panel</span>
                        </div>
                        <Switch
                            checked={shortcuts.sql_editor}
                            onCheckedChange={checked => setShortcuts({ ...shortcuts, sql_editor: checked })}
                        />
                    </div>
                </div>
            </div>

            {/* Analytics and Marketing */}
            <div className="space-y-6">
                <h2 className="text-lg font-medium border-b border-border/50 pb-2">Analytics and Marketing</h2>
                <p className="text-sm text-muted-foreground">Control whether telemetry and marketing data is sent from Supabase services.</p>

                <div className="max-w-3xl bg-card border border-border rounded-md p-4 flex items-center justify-between">
                    <div className="space-y-1">
                        <span className="text-sm font-medium block">Send telemetry data from Supabase services</span>
                        <p className="text-xs text-muted-foreground max-w-lg">By opting in to sharing telemetry data, Supabase can analyze usage patterns to enhance user experience and use it for marketing and advertising purposes</p>
                    </div>
                    <Switch checked={telemetry} onCheckedChange={setTelemetry} />
                </div>
            </div>

            {/* Danger Zone */}
            <div className="space-y-6">
                <h2 className="text-lg font-medium border-b border-border/50 pb-2">Danger zone</h2>
                <p className="text-sm text-muted-foreground">Permanently delete your Supabase account and data.</p>

                <div className="max-w-3xl bg-red-50/50 border border-red-200 rounded-md p-4">
                    <div className="flex items-start gap-4">
                        <AlertTriangle className="h-5 w-5 text-red-600 mt-0.5" />
                        <div className="space-y-3">
                            <h4 className="text-sm font-medium text-red-900">Request for account deletion</h4>
                            <p className="text-xs text-red-700 max-w-xl">
                                Deleting your account is permanent and cannot be undone. Your data will be deleted within 30 days, but we may retain some metadata and logs for longer where required or permitted by law.
                            </p>
                            <Button variant="outline" size="sm" className="border-red-200 text-red-700 hover:bg-red-50 hover:text-red-800">
                                Request to delete account
                            </Button>
                        </div>
                    </div>
                </div>
            </div>

        </div>
    );
}
