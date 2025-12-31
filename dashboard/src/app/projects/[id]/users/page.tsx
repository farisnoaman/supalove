"use client";

import { useState, useEffect } from "react";
import { useParams } from "next/navigation";
import { Button } from "@/components/ui/button";
import { UserPlus, Trash2, Shield, User, Eye, EyeOff, Copy, Check } from "lucide-react";
import { toast } from "sonner";
import {
    Dialog,
    DialogContent,
    DialogDescription,
    DialogFooter,
    DialogHeader,
    DialogTitle,
} from "@/components/ui/dialog";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import {
    Select,
    SelectContent,
    SelectItem,
    SelectTrigger,
    SelectValue,
} from "@/components/ui/select";
import {
    Table,
    TableBody,
    TableCell,
    TableHead,
    TableHeader,
    TableRow,
} from "@/components/ui/table";
import { Badge } from "@/components/ui/badge";

interface ProjectUser {
    id: string;
    email: string;
    role: string;
    created_at: string;
    email_confirmed_at?: string;
    user_metadata: any;
}

export default function ProjectUsersPage() {
    const params = useParams();
    const projectId = params.id as string;

    const [users, setUsers] = useState<ProjectUser[]>([]);
    const [loading, setLoading] = useState(true);
    const [showCreateModal, setShowCreateModal] = useState(false);
    const [showAdminPassword, setShowAdminPassword] = useState(false);
    const [adminPassword, setAdminPassword] = useState<string | null>(null);
    const [copied, setCopied] = useState(false);

    // Create user form state
    const [newUser, setNewUser] = useState({
        email: "",
        password: "",
        role: "member"
    });
    const [showPassword, setShowPassword] = useState(false);
    const [creating, setCreating] = useState(false);

    const fetchUsers = async () => {
        try {
            const token = localStorage.getItem("token");
            const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

            const res = await fetch(`${API_URL}/api/v1/projects/${projectId}/users`, {
                headers: {
                    "Authorization": `Bearer ${token}`
                }
            });

            if (!res.ok) throw new Error("Failed to fetch users");

            const data = await res.json();
            setUsers(data);
        } catch (error: any) {
            toast.error(error.message);
        } finally {
            setLoading(false);
        }
    };

    const fetchAdminPassword = async () => {
        try {
            const token = localStorage.getItem("token");
            const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

            const res = await fetch(`${API_URL}/api/v1/projects/${projectId}/admin-password`, {
                headers: {
                    "Authorization": `Bearer ${token}`
                }
            });

            if (res.status === 404) {
                toast.error("Admin password already retrieved or not found");
                return;
            }

            if (!res.ok) throw new Error("Failed to fetch admin password");

            const data = await res.json();
            setAdminPassword(data.password);
            setShowAdminPassword(true);
        } catch (error: any) {
            toast.error(error.message);
        }
    };

    const createUser = async () => {
        if (!newUser.email || !newUser.password) {
            toast.error("Email and password are required");
            return;
        }

        setCreating(true);
        try {
            const token = localStorage.getItem("token");
            const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

            const res = await fetch(`${API_URL}/api/v1/projects/${projectId}/users`, {
                method: "POST",
                headers: {
                    "Authorization": `Bearer ${token}`,
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(newUser)
            });

            if (!res.ok) {
                const error = await res.json();
                throw new Error(error.detail || "Failed to create user");
            }

            toast.success("User created successfully");
            setShowCreateModal(false);
            setNewUser({ email: "", password: "", role: "member" });
            fetchUsers();
        } catch (error: any) {
            toast.error(error.message);
        } finally {
            setCreating(false);
        }
    };

    const deleteUser = async (userId: string, email: string) => {
        if (!confirm(`Are you sure you want to delete user ${email}?`)) return;

        try {
            const token = localStorage.getItem("token");
            const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

            const res = await fetch(`${API_URL}/api/v1/projects/${projectId}/users/${userId}`, {
                method: "DELETE",
                headers: {
                    "Authorization": `Bearer ${token}`
                }
            });

            if (!res.ok) throw new Error("Failed to delete user");

            toast.success("User deleted successfully");
            fetchUsers();
        } catch (error: any) {
            toast.error(error.message);
        }
    };

    const copyToClipboard = () => {
        if (adminPassword) {
            navigator.clipboard.writeText(adminPassword);
            setCopied(true);
            setTimeout(() => setCopied(false), 2000);
            toast.success("Password copied to clipboard");
        }
    };

    useEffect(() => {
        fetchUsers();
    }, [projectId]);

    return (
        <div className="container mx-auto p-6 space-y-6">
            <div className="flex justify-between items-center">
                <div>
                    <h1 className="text-3xl font-bold">Project Users</h1>
                    <p className="text-muted-foreground mt-1">
                        Manage users who have access to this project's database
                    </p>
                </div>
                <div className="flex gap-2">
                    <Button
                        variant="outline"
                        onClick={fetchAdminPassword}
                    >
                        Get Admin Password
                    </Button>
                    <Button
                        onClick={() => setShowCreateModal(true)}
                        className="gap-2"
                    >
                        <UserPlus size={16} />
                        Add User
                    </Button>
                </div>
            </div>

            {/* Users Table */}
            <div className="border rounded-lg">
                <Table>
                    <TableHeader>
                        <TableRow>
                            <TableHead>Email</TableHead>
                            <TableHead>Role</TableHead>
                            <TableHead>Created</TableHead>
                            <TableHead>Status</TableHead>
                            <TableHead className="text-right">Actions</TableHead>
                        </TableRow>
                    </TableHeader>
                    <TableBody>
                        {loading ? (
                            <TableRow>
                                <TableCell colSpan={5} className="text-center py-8 text-muted-foreground">
                                    Loading users...
                                </TableCell>
                            </TableRow>
                        ) : users.length === 0 ? (
                            <TableRow>
                                <TableCell colSpan={5} className="text-center py-8 text-muted-foreground">
                                    No users found. Create your first user to get started.
                                </TableCell>
                            </TableRow>
                        ) : (
                            users.map((user) => (
                                <TableRow key={user.id}>
                                    <TableCell className="font-medium">{user.email}</TableCell>
                                    <TableCell>
                                        <Badge variant={user.role === "admin" ? "default" : "secondary"} className="gap-1">
                                            {user.role === "admin" ? <Shield size={12} /> : <User size={12} />}
                                            {user.role}
                                        </Badge>
                                    </TableCell>
                                    <TableCell className="text-muted-foreground">
                                        {new Date(user.created_at).toLocaleDateString()}
                                    </TableCell>
                                    <TableCell>
                                        {user.email_confirmed_at ? (
                                            <Badge variant="outline" className="bg-green-50 text-green-700 border-green-200">
                                                Confirmed
                                            </Badge>
                                        ) : (
                                            <Badge variant="outline" className="bg-yellow-50 text-yellow-700 border-yellow-200">
                                                Pending
                                            </Badge>
                                        )}
                                    </TableCell>
                                    <TableCell className="text-right">
                                        <Button
                                            variant="ghost"
                                            size="sm"
                                            onClick={() => deleteUser(user.id, user.email)}
                                        >
                                            <Trash2 size={16} />
                                        </Button>
                                    </TableCell>
                                </TableRow>
                            ))
                        )}
                    </TableBody>
                </Table>
            </div>

            {/* Create User Modal */}
            <Dialog open={showCreateModal} onOpenChange={setShowCreateModal}>
                <DialogContent>
                    <DialogHeader>
                        <DialogTitle>Create New User</DialogTitle>
                        <DialogDescription>
                            Add a new user to this project's database
                        </DialogDescription>
                    </DialogHeader>

                    <div className="space-y-4 py-4">
                        <div className="space-y-2">
                            <Label htmlFor="email">Email</Label>
                            <Input
                                id="email"
                                type="email"
                                placeholder="user@example.com"
                                value={newUser.email}
                                onChange={(e) => setNewUser({ ...newUser, email: e.target.value })}
                            />
                        </div>

                        <div className="space-y-2">
                            <Label htmlFor="password">Password</Label>
                            <div className="relative">
                                <Input
                                    id="password"
                                    type={showPassword ? "text" : "password"}
                                    placeholder="Enter password"
                                    value={newUser.password}
                                    onChange={(e) => setNewUser({ ...newUser, password: e.target.value })}
                                />
                                <Button
                                    type="button"
                                    variant="ghost"
                                    size="sm"
                                    className="absolute right-0 top-0 h-full px-3"
                                    onClick={() => setShowPassword(!showPassword)}
                                >
                                    {showPassword ? <EyeOff size={16} /> : <Eye size={16} />}
                                </Button>
                            </div>
                        </div>

                        <div className="space-y-2">
                            <Label htmlFor="role">Role</Label>
                            <Select
                                value={newUser.role}
                                onValueChange={(value) => setNewUser({ ...newUser, role: value })}
                            >
                                <SelectTrigger>
                                    <SelectValue />
                                </SelectTrigger>
                                <SelectContent>
                                    <SelectItem value="member">Member</SelectItem>
                                    <SelectItem value="admin">Admin</SelectItem>
                                </SelectContent>
                            </Select>
                        </div>
                    </div>

                    <DialogFooter>
                        <Button variant="outline" onClick={() => setShowCreateModal(false)}>
                            Cancel
                        </Button>
                        <Button onClick={createUser} disabled={creating}>
                            {creating ? "Creating..." : "Create User"}
                        </Button>
                    </DialogFooter>
                </DialogContent>
            </Dialog>

            {/* Admin Password Modal */}
            <Dialog open={showAdminPassword} onOpenChange={setShowAdminPassword}>
                <DialogContent>
                    <DialogHeader>
                        <DialogTitle>Admin Password</DialogTitle>
                        <DialogDescription>
                            This password will only be shown once. Make sure to save it securely.
                        </DialogDescription>
                    </DialogHeader>

                    <div className="space-y-4 py-4">
                        <div className="bg-muted p-4 rounded-lg font-mono text-center text-lg">
                            {adminPassword}
                        </div>
                        <Button
                            variant="outline"
                            className="w-full gap-2"
                            onClick={copyToClipboard}
                        >
                            {copied ? <Check size={16} /> : <Copy size={16} />}
                            {copied ? "Copied!" : "Copy to Clipboard"}
                        </Button>
                    </div>

                    <DialogFooter>
                        <Button onClick={() => setShowAdminPassword(false)}>
                            Close
                        </Button>
                    </DialogFooter>
                </DialogContent>
            </Dialog>
        </div>
    );
}
