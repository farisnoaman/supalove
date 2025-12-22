"use client";

import { useEffect, useState } from "react";
import { useParams } from "next/navigation";
import {
    Users,
    UserPlus,
    Mail,
    Shield,
    Trash2,
    MoreVertical,
    Search,
    RefreshCw,
    UserCheck,
    Lock
} from "lucide-react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Breadcrumb } from "@/components/ui/breadcrumb";
import { Skeleton } from "@/components/ui/skeleton";
import { Badge } from "@/components/ui/badge";
import { Modal, ModalContent, ModalHeader, ModalTitle, ModalFooter } from "@/components/ui/modal";
import { Toaster, toast } from "sonner";
import { cn } from "@/lib/utils";

interface User {
    id: string;
    email: string;
    username: string;
    enabled: boolean;
    createdTimestamp: number;
}

export default function AuthPage() {
    const params = useParams();
    const projectId = params.id as string;

    const [users, setUsers] = useState<User[]>([]);
    const [loading, setLoading] = useState(true);
    const [searchQuery, setSearchQuery] = useState("");
    const [isAddUserOpen, setIsAddUserOpen] = useState(false);
    const [userToDelete, setUserToDelete] = useState<string | null>(null);
    const [isDeleting, setIsDeleting] = useState(false);

    // Form state
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [isSaving, setIsSaving] = useState(false);

    const API_URL = (process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000").replace(/\/$/, "");

    useEffect(() => {
        if (projectId) fetchUsers();
    }, [projectId]);

    const fetchUsers = async () => {
        setLoading(true);
        try {
            console.log(`Fetching users for project ${projectId} from ${API_URL}`);
            const token = localStorage.getItem("token");
            const resp = await fetch(`${API_URL}/api/v1/projects/${projectId}/auth/users`, {
                headers: {
                    "Authorization": `Bearer ${token}`
                }
            });
            if (!resp.ok) throw new Error("Failed to fetch users");
            const data = await resp.json();
            setUsers(Array.isArray(data) ? data : []);
        } catch (err) {
            console.error("Auth fetch error:", err);
            toast.error("Failed to load users");
        } finally {
            setLoading(false);
        }
    };

    const handleCreateUser = async (e: React.FormEvent) => {
        e.preventDefault();
        setIsSaving(true);
        try {
            const token = localStorage.getItem("token");
            const resp = await fetch(`${API_URL}/api/v1/projects/${projectId}/auth/users`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${token}`
                },
                body: JSON.stringify({ email, password })
            });

            if (resp.ok) {
                toast.success("User created successfully");
                setIsAddUserOpen(false);
                setEmail("");
                setPassword("");
                fetchUsers();
            } else {
                toast.error("Failed to create user");
            }
        } catch (err) {
            toast.error("Network error");
        } finally {
            setIsSaving(false);
        }
    };

    const handleDeleteUser = async () => {
        if (!userToDelete) return;
        setIsDeleting(true);

        try {
            const token = localStorage.getItem("token");
            const resp = await fetch(`${API_URL}/api/v1/projects/${projectId}/auth/users/${userToDelete}`, {
                method: "DELETE",
                headers: {
                    "Authorization": `Bearer ${token}`
                }
            });
            if (resp.ok) {
                toast.success("User deleted");
                fetchUsers();
            } else {
                toast.error("Failed to delete user");
            }
        } catch (err) {
            toast.error("Network error");
        } finally {
            setIsDeleting(false);
            setUserToDelete(null);
        }
    };

    const filteredUsers = users.filter(u =>
        u.email?.toLowerCase().includes(searchQuery.toLowerCase()) ||
        u.id?.toLowerCase().includes(searchQuery.toLowerCase())
    );

    return (
        <div className="space-y-8 animate-in fade-in slide-in-from-bottom-4 duration-700">
            <Breadcrumb
                items={[
                    { label: "Overview", href: `/projects/${projectId}` },
                    { label: "Authentication" },
                ]}
            />

            <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
                <div>
                    <h2 className="text-3xl font-bold tracking-tight text-gradient">Authentication</h2>
                    <p className="text-sm text-muted-foreground mt-1">
                        Manage users, roles, and authentication settings for your project.
                    </p>
                </div>
                <Button
                    onClick={() => setIsAddUserOpen(true)}
                    className="gap-2 primary-gradient shadow-lg shadow-emerald-500/20 hover:scale-105 transition-all h-10 px-6 rounded-xl"
                >
                    <UserPlus size={18} />
                    Add User
                </Button>
            </div>

            {/* Stats Cards */}
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                <div className="p-6 bg-card border border-border/40 rounded-2xl glass relative overflow-hidden group">
                    <div className="flex items-center gap-4 relative z-10">
                        <div className="p-3 bg-emerald-500/10 rounded-xl">
                            <Users className="text-emerald-500" size={24} />
                        </div>
                        <div>
                            <p className="text-xs font-bold text-muted-foreground uppercase tracking-widest">Total Users</p>
                            <h3 className="text-2xl font-bold mt-1">{loading ? "..." : users.length}</h3>
                        </div>
                    </div>
                    <div className="absolute -right-4 -bottom-4 opacity-5 group-hover:scale-110 transition-transform duration-500">
                        <Users size={120} />
                    </div>
                </div>

                <div className="p-6 bg-card border border-border/40 rounded-2xl glass relative overflow-hidden group">
                    <div className="flex items-center gap-4 relative z-10">
                        <div className="p-3 bg-blue-500/10 rounded-xl">
                            <Shield className="text-blue-500" size={24} />
                        </div>
                        <div>
                            <p className="text-xs font-bold text-muted-foreground uppercase tracking-widest">Active Realms</p>
                            <h3 className="text-2xl font-bold mt-1">1</h3>
                        </div>
                    </div>
                    <div className="absolute -right-4 -bottom-4 opacity-5 group-hover:scale-110 transition-transform duration-500">
                        <Shield size={120} />
                    </div>
                </div>

                <div className="p-6 bg-card border border-border/40 rounded-2xl glass relative overflow-hidden group">
                    <div className="flex items-center gap-4 relative z-10">
                        <div className="p-3 bg-amber-500/10 rounded-xl">
                            <Lock className="text-amber-500" size={24} />
                        </div>
                        <div>
                            <p className="text-xs font-bold text-muted-foreground uppercase tracking-widest">Auth Providers</p>
                            <h3 className="text-2xl font-bold mt-1">1</h3>
                        </div>
                    </div>
                    <div className="absolute -right-4 -bottom-4 opacity-5 group-hover:scale-110 transition-transform duration-500">
                        <Lock size={120} />
                    </div>
                </div>
            </div>

            {/* Toolbar */}
            <div className="flex items-center gap-3">
                <div className="relative flex-1 max-w-md">
                    <Search className="absolute left-3 top-1/2 -translate-y-1/2 text-muted-foreground" size={16} />
                    <Input
                        placeholder="Search by email or user ID..."
                        value={searchQuery}
                        onChange={(e) => setSearchQuery(e.target.value)}
                        className="pl-9 bg-card border-border/40 focus:border-primary/50 h-10 rounded-xl"
                    />
                </div>
                <Button variant="outline" size="icon" onClick={fetchUsers} className="rounded-xl border-border/40 text-muted-foreground h-10 w-10">
                    <RefreshCw className={cn(loading && "animate-spin")} size={16} />
                </Button>
            </div>

            {/* Users Table */}
            <div className="bg-card border border-border/40 rounded-2xl overflow-hidden shadow-xl glass">
                <div className="overflow-x-auto">
                    <table className="w-full text-left">
                        <thead className="bg-muted/50 border-b border-border/40">
                            <tr>
                                <th className="px-6 py-4 text-[11px] font-bold uppercase tracking-widest text-muted-foreground">User</th>
                                <th className="px-6 py-4 text-[11px] font-bold uppercase tracking-widest text-muted-foreground">Status</th>
                                <th className="px-6 py-4 text-[11px] font-bold uppercase tracking-widest text-muted-foreground">User ID</th>
                                <th className="px-6 py-4 text-[11px] font-bold uppercase tracking-widest text-muted-foreground">Created</th>
                                <th className="px-6 py-4 text-right"></th>
                            </tr>
                        </thead>
                        <tbody className="divide-y divide-border/20">
                            {loading ? (
                                [...Array(5)].map((_, i) => (
                                    <tr key={i}>
                                        <td className="px-6 py-4"><Skeleton className="h-10 w-48" /></td>
                                        <td className="px-6 py-4"><Skeleton className="h-6 w-20" /></td>
                                        <td className="px-6 py-4"><Skeleton className="h-4 w-32" /></td>
                                        <td className="px-6 py-4"><Skeleton className="h-4 w-24" /></td>
                                        <td className="px-6 py-4"></td>
                                    </tr>
                                ))
                            ) : filteredUsers.length === 0 ? (
                                <tr>
                                    <td colSpan={5} className="px-6 py-20 text-center">
                                        <div className="flex flex-col items-center">
                                            <div className="p-4 bg-muted/50 rounded-full mb-4">
                                                <Users size={40} className="text-muted-foreground/30" />
                                            </div>
                                            <h3 className="text-lg font-bold">No users found</h3>
                                            <p className="text-sm text-muted-foreground max-w-xs mt-1">
                                                {searchQuery ? `No users match "${searchQuery}"` : "Start by adding users to your project."}
                                            </p>
                                        </div>
                                    </td>
                                </tr>
                            ) : (
                                filteredUsers.map((user) => (
                                    <tr key={user.id} className="hover:bg-emerald-50/20 dark:hover:bg-emerald-500/5 transition-colors group">
                                        <td className="px-6 py-4">
                                            <div className="flex items-center gap-3">
                                                <div className="w-9 h-9 rounded-xl bg-primary/10 flex items-center justify-center text-primary font-bold">
                                                    {user.email?.[0].toUpperCase()}
                                                </div>
                                                <div className="flex flex-col">
                                                    <span className="text-sm font-bold text-foreground group-hover:text-primary transition-colors">
                                                        {user.email}
                                                    </span>
                                                    <span className="text-[10px] text-muted-foreground font-mono">
                                                        {user.username}
                                                    </span>
                                                </div>
                                            </div>
                                        </td>
                                        <td className="px-6 py-4">
                                            <Badge
                                                variant={user.enabled ? "default" : "secondary"}
                                                className={cn("text-[10px] uppercase font-bold tracking-tight", user.enabled && "bg-emerald-500/10 text-emerald-500 border-emerald-500/20 shadow-none")}
                                            >
                                                {user.enabled ? "Active" : "Disabled"}
                                            </Badge>
                                        </td>
                                        <td className="px-6 py-4">
                                            <code className="text-[11px] font-mono p-1 bg-muted/50 rounded border border-border/20 text-muted-foreground">
                                                {user.id}
                                            </code>
                                        </td>
                                        <td className="px-6 py-4 text-sm text-muted-foreground">
                                            {new Date(user.createdTimestamp).toLocaleDateString()}
                                        </td>
                                        <td className="px-6 py-4 text-right">
                                            <Button
                                                variant="ghost"
                                                size="icon"
                                                onClick={() => setUserToDelete(user.id)}
                                                className="text-muted-foreground hover:text-destructive transition-colors opacity-0 group-hover:opacity-100"
                                            >
                                                <Trash2 size={16} />
                                            </Button>
                                        </td>
                                    </tr>
                                ))
                            )}
                        </tbody>
                    </table>
                </div>
            </div>

            {/* Add User Modal */}
            <Modal open={isAddUserOpen} onOpenChange={setIsAddUserOpen}>
                <ModalContent className="max-w-md bg-card border-border/40 shadow-2xl p-0 overflow-hidden rounded-3xl glass">
                    <ModalHeader className="p-6 border-b border-border/20 bg-muted/30">
                        <div className="flex items-center gap-3">
                            <div className="p-2 bg-emerald-500/10 rounded-lg">
                                <UserPlus size={20} className="text-emerald-500" />
                            </div>
                            <ModalTitle className="text-2xl font-bold tracking-tight">Add New User</ModalTitle>
                        </div>
                    </ModalHeader>

                    <form onSubmit={handleCreateUser} className="p-6 space-y-4">
                        <div className="space-y-2">
                            <label className="text-xs font-bold text-muted-foreground uppercase tracking-widest pl-1">Email Address</label>
                            <div className="relative">
                                <Mail className="absolute left-3 top-1/2 -translate-y-1/2 text-muted-foreground" size={16} />
                                <Input
                                    required
                                    type="email"
                                    placeholder="user@example.com"
                                    value={email}
                                    onChange={(e) => setEmail(e.target.value)}
                                    className="pl-10 bg-muted/50 border-border/40 focus:border-primary/40 focus:ring-primary/10 rounded-xl"
                                />
                            </div>
                        </div>

                        <div className="space-y-2">
                            <label className="text-xs font-bold text-muted-foreground uppercase tracking-widest pl-1">Password (Optional)</label>
                            <div className="relative">
                                <Lock className="absolute left-3 top-1/2 -translate-y-1/2 text-muted-foreground" size={16} />
                                <Input
                                    type="password"
                                    placeholder="••••••••"
                                    value={password}
                                    onChange={(e) => setPassword(e.target.value)}
                                    className="pl-10 bg-muted/50 border-border/40 focus:border-primary/40 focus:ring-primary/10 rounded-xl"
                                />
                            </div>
                        </div>

                        <div className="pt-4 flex items-center justify-end gap-3">
                            <Button
                                type="button"
                                variant="ghost"
                                onClick={() => setIsAddUserOpen(false)}
                                className="text-muted-foreground hover:text-foreground"
                            >
                                Cancel
                            </Button>
                            <Button
                                type="submit"
                                disabled={isSaving || !email}
                                className="primary-gradient shadow-lg shadow-emerald-500/20 px-8 rounded-xl"
                            >
                                {isSaving ? "Adding..." : "Add User"}
                            </Button>
                        </div>
                    </form>
                </ModalContent>
            </Modal>
            {/* Delete Confirmation Modal */}
            <Modal open={!!userToDelete} onOpenChange={(open) => !open && setUserToDelete(null)}>
                <ModalContent className="max-w-md bg-card border-border/40 shadow-2xl glass rounded-2xl p-6">
                    <ModalHeader className="mb-4">
                        <ModalTitle className="text-xl font-bold text-destructive">Delete User</ModalTitle>
                    </ModalHeader>
                    <div className="space-y-4">
                        <p className="text-sm text-muted-foreground">
                            Are you sure you want to delete this user? This action cannot be undone.
                        </p>
                        <ModalFooter className="flex items-center justify-end gap-3 mt-8">
                            <Button variant="ghost" onClick={() => setUserToDelete(null)} disabled={isDeleting} className="rounded-xl">
                                Cancel
                            </Button>
                            <Button
                                onClick={handleDeleteUser}
                                disabled={isDeleting}
                                className="bg-destructive text-destructive-foreground hover:bg-destructive/90 px-6 rounded-xl shadow-lg shadow-destructive/20"
                            >
                                {isDeleting ? "Deleting..." : "Delete User"}
                            </Button>
                        </ModalFooter>
                    </div>
                </ModalContent>
            </Modal>

            <Toaster position="top-right" />
        </div>
    );
}
