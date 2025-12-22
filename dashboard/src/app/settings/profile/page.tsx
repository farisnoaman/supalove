"use client";

import { useEffect, useState } from "react";
import { useTheme } from "next-themes";
import { Moon, Sun, Monitor, User, Clock, Save, ArrowLeft, ArrowRight } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { toast, Toaster } from "sonner";
import Link from "next/link";

interface UserProfile {
    id: string;
    email: string;
    full_name: string | null;
    timezone: string;
    avatar_url: string | null;
    preferences: {
        theme?: string;
    } | null;
}

const TIMEZONES = [
    "UTC",
    "America/New_York",
    "America/Los_Angeles",
    "America/Chicago",
    "Europe/London",
    "Europe/Paris",
    "Europe/Berlin",
    "Asia/Tokyo",
    "Asia/Shanghai",
    "Asia/Dubai",
    "Asia/Kolkata",
    "Australia/Sydney",
    "Pacific/Auckland",
];

export default function ProfilePage() {
    const { theme, setTheme } = useTheme();
    const [profile, setProfile] = useState<UserProfile | null>(null);
    const [loading, setLoading] = useState(true);
    const [saving, setSaving] = useState(false);
    const [fullName, setFullName] = useState("");
    const [timezone, setTimezone] = useState("UTC");
    const [mounted, setMounted] = useState(false);

    const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

    useEffect(() => {
        setMounted(true);
        fetchProfile();
    }, []);

    const fetchProfile = async () => {
        try {
            const token = localStorage.getItem("token");
            if (!token) {
                window.location.href = "/login";
                return;
            }

            const resp = await fetch(`${API_URL}/api/v1/users/me`, {
                headers: { "Authorization": `Bearer ${token}` }
            });

            if (!resp.ok) throw new Error("Failed to fetch profile");

            const data = await resp.json();
            setProfile(data);
            setFullName(data.full_name || "");
            setTimezone(data.timezone || "UTC");

            // Sync theme from backend if exists
            if (data.preferences?.theme) {
                setTheme(data.preferences.theme);
            }
        } catch (err) {
            console.error(err);
            toast.error("Failed to load profile");
        } finally {
            setLoading(false);
        }
    };

    const handleSave = async () => {
        setSaving(true);
        try {
            const token = localStorage.getItem("token");
            const resp = await fetch(`${API_URL}/api/v1/users/me`, {
                method: "PATCH",
                headers: {
                    "Authorization": `Bearer ${token}`,
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    full_name: fullName,
                    timezone: timezone,
                    theme: theme
                })
            });

            if (!resp.ok) throw new Error("Failed to save");

            const data = await resp.json();
            setProfile(data);
            toast.success("Profile updated successfully");
        } catch (err) {
            toast.error("Failed to save profile");
        } finally {
            setSaving(false);
        }
    };

    if (!mounted) return null;

    return (
        <div className="min-h-screen bg-background">
            <Toaster richColors position="top-right" />

            {/* Header */}
            <header className="border-b border-border bg-card/50 backdrop-blur-sm sticky top-0 z-10">
                <div className="container mx-auto px-4 md:px-8 h-16 flex items-center gap-4">
                    <Link href="/projects" className="text-muted-foreground hover:text-foreground transition-colors">
                        <ArrowLeft size={20} />
                    </Link>
                    <h1 className="text-xl font-bold">Profile Settings</h1>
                </div>
            </header>

            <main className="container mx-auto px-4 md:px-8 py-8">
                {loading ? (
                    <div className="flex justify-center py-20">
                        <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-primary"></div>
                    </div>
                ) : (
                    <div className="max-w-2xl mx-auto space-y-8">
                        {/* Profile Card */}
                        <div className="bg-card border border-border rounded-2xl p-6 md:p-8 shadow-lg">
                            <div className="flex items-center gap-4 mb-8">
                                <div className="w-16 h-16 rounded-full bg-primary/10 flex items-center justify-center text-primary text-2xl font-bold ring-4 ring-primary/20">
                                    {(fullName || profile?.email || "U")[0].toUpperCase()}
                                </div>
                                <div>
                                    <h2 className="text-2xl font-bold">{fullName || "User"}</h2>
                                    <p className="text-sm text-muted-foreground">{profile?.email}</p>
                                </div>
                            </div>

                            <div className="space-y-6">
                                {/* Full Name */}
                                <div className="space-y-2">
                                    <label className="text-xs font-bold text-muted-foreground uppercase tracking-widest flex items-center gap-2">
                                        <User size={14} />
                                        Full Name
                                    </label>
                                    <Input
                                        value={fullName}
                                        onChange={(e) => setFullName(e.target.value)}
                                        placeholder="Your name"
                                        className="bg-muted/50 border-border/40"
                                    />
                                </div>

                                {/* Timezone */}
                                <div className="space-y-2">
                                    <label className="text-xs font-bold text-muted-foreground uppercase tracking-widest flex items-center gap-2">
                                        <Clock size={14} />
                                        Timezone
                                    </label>
                                    <select
                                        value={timezone}
                                        onChange={(e) => setTimezone(e.target.value)}
                                        className="w-full h-10 px-3 rounded-lg bg-muted/50 border border-border/40 text-sm focus:outline-none focus:ring-2 focus:ring-primary/20"
                                    >
                                        {TIMEZONES.map(tz => (
                                            <option key={tz} value={tz}>{tz}</option>
                                        ))}
                                    </select>
                                </div>

                                {/* Theme */}
                                <div className="space-y-2">
                                    <label className="text-xs font-bold text-muted-foreground uppercase tracking-widest">
                                        Theme
                                    </label>
                                    <div className="flex gap-2">
                                        <Button
                                            variant={theme === "light" ? "default" : "outline"}
                                            onClick={() => setTheme("light")}
                                            className="flex-1 gap-2"
                                        >
                                            <Sun size={16} />
                                            Light
                                        </Button>
                                        <Button
                                            variant={theme === "dark" ? "default" : "outline"}
                                            onClick={() => setTheme("dark")}
                                            className="flex-1 gap-2"
                                        >
                                            <Moon size={16} />
                                            Dark
                                        </Button>
                                        <Button
                                            variant={theme === "system" ? "default" : "outline"}
                                            onClick={() => setTheme("system")}
                                            className="flex-1 gap-2"
                                        >
                                            <Monitor size={16} />
                                            System
                                        </Button>
                                    </div>
                                </div>
                            </div>
                        </div>

                        {/* Save Button */}
                        <div className="flex justify-end">
                            <Button
                                onClick={handleSave}
                                disabled={saving}
                                className="gap-2 px-8 bg-primary hover:bg-primary/90"
                            >
                                <Save size={16} />
                                {saving ? "Saving..." : "Save Changes"}
                            </Button>
                        </div>

                        {/* Account Info */}
                        <div className="bg-card border border-border rounded-2xl p-6 md:p-8 shadow-lg">
                            <h3 className="text-lg font-bold mb-4">Account Information</h3>
                            <div className="space-y-4 text-sm">
                                <div className="flex justify-between py-2 border-b border-border/40">
                                    <span className="text-muted-foreground">User ID</span>
                                    <code className="text-xs bg-muted/50 px-2 py-1 rounded">{profile?.id}</code>
                                </div>
                                <div className="flex justify-between py-2 border-b border-border/40">
                                    <span className="text-muted-foreground">Email</span>
                                    <span>{profile?.email}</span>
                                </div>
                            </div>
                        </div>

                        {/* Organizations Link */}
                        <div className="bg-card border border-border rounded-2xl p-6 shadow-sm hover:shadow-md transition-shadow">
                            <div className="flex items-center justify-between">
                                <div>
                                    <h3 className="text-lg font-bold">Organizations</h3>
                                    <p className="text-sm text-muted-foreground">Manage your teams and memberships.</p>
                                </div>
                                <Link href="/settings/organization">
                                    <Button variant="outline" className="gap-2">
                                        Manage Organizations
                                        <ArrowRight size={16} />
                                    </Button>
                                </Link>
                            </div>
                        </div>
                    </div>
                )}
            </main>
        </div>
    );
}
