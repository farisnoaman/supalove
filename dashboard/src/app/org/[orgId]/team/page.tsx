"use client";

import { useEffect, useState } from "react";
import { useParams } from "next/navigation";
import { UserPlus, Users, Shield } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { toast } from "sonner";
import { Skeleton } from "@/components/ui/skeleton";
import { Modal, ModalContent, ModalHeader, ModalTitle, ModalFooter } from "@/components/ui/modal";
import { useOrg } from "@/components/providers/org-provider";

interface Member {
    id: string;
    email: string;
    full_name: string;
    role: string;
    user_id: string;
}

export default function OrgTeamPage() {
    const params = useParams();
    const orgId = params.orgId as string;
    const { currentOrg } = useOrg();

    const [members, setMembers] = useState<Member[]>([]);
    const [loading, setLoading] = useState(true);
    const [isInviteOpen, setIsInviteOpen] = useState(false);
    const [inviteEmail, setInviteEmail] = useState("");
    const [inviting, setInviting] = useState(false);

    const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

    useEffect(() => {
        if (orgId) fetchMembers();
    }, [orgId]);

    const fetchMembers = async () => {
        try {
            const token = localStorage.getItem("token");
            const resp = await fetch(`${API_URL}/api/v1/orgs/${orgId}/members`, {
                headers: { "Authorization": `Bearer ${token}` }
            });

            if (!resp.ok) throw new Error("Failed to fetch members");

            const data = await resp.json();
            setMembers(data);
        } catch (err) {
            console.error(err);
            toast.error("Failed to load members");
        } finally {
            setLoading(false);
        }
    };

    const handleInvite = async (e: React.FormEvent) => {
        e.preventDefault();
        setInviting(true);
        try {
            const token = localStorage.getItem("token");
            const resp = await fetch(`${API_URL}/api/v1/orgs/${orgId}/members`, {
                method: "POST",
                headers: {
                    "Authorization": `Bearer ${token}`,
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ email: inviteEmail, role: "MEMBER" })
            });

            if (!resp.ok) {
                const err = await resp.json();
                throw new Error(err.detail || "Failed to add member");
            }

            toast.success("Member added successfully");
            setIsInviteOpen(false);
            setInviteEmail("");
            fetchMembers();
        } catch (err: any) {
            toast.error(err.message || "Failed to invite member");
        } finally {
            setInviting(false);
        }
    };

    return (
        <div className="container mx-auto px-4 md:px-8 py-8 space-y-8 animate-in fade-in duration-500">
            <div className="flex items-center justify-between">
                <div>
                    <h2 className="text-2xl font-bold tracking-tight">Team Members</h2>
                    <p className="text-sm text-muted-foreground mt-1">Manage access to {currentOrg?.name}.</p>
                </div>
                <Button onClick={() => setIsInviteOpen(true)} className="gap-2 shadow-sm">
                    <UserPlus size={16} />
                    Invite Member
                </Button>
            </div>

            <div className="bg-card border border-border rounded-xl overflow-hidden shadow-sm">
                <table className="w-full text-left">
                    <thead className="bg-muted/50 border-b border-border">
                        <tr>
                            <th className="px-6 py-3 text-xs font-bold uppercase tracking-widest text-muted-foreground">User</th>
                            <th className="px-6 py-3 text-xs font-bold uppercase tracking-widest text-muted-foreground">Role</th>
                            <th className="px-6 py-3 text-xs font-bold uppercase tracking-widest text-muted-foreground">ID</th>
                        </tr>
                    </thead>
                    <tbody className="divide-y divide-border/20">
                        {loading ? (
                            [...Array(3)].map((_, i) => (
                                <tr key={i}>
                                    <td className="px-6 py-4"><Skeleton className="h-4 w-32" /></td>
                                    <td className="px-6 py-4"><Skeleton className="h-4 w-16" /></td>
                                    <td className="px-6 py-4"><Skeleton className="h-4 w-24" /></td>
                                </tr>
                            ))
                        ) : (
                            members.map((member) => (
                                <tr key={member.id} className="hover:bg-muted/30 transition-colors">
                                    <td className="px-6 py-4">
                                        <div className="flex items-center gap-3">
                                            <div className="w-8 h-8 rounded-full bg-primary/10 flex items-center justify-center text-primary font-bold text-xs ring-2 ring-background">
                                                {(member.full_name || member.email)[0].toUpperCase()}
                                            </div>
                                            <div>
                                                <div className="font-medium text-sm">{member.full_name || "Unknown"}</div>
                                                <div className="text-xs text-muted-foreground">{member.email}</div>
                                            </div>
                                        </div>
                                    </td>
                                    <td className="px-6 py-4">
                                        <span className={`inline-flex items-center px-2 py-0.5 rounded text-xs font-medium border ${member.role === 'OWNER' ? 'bg-purple-100 text-purple-800 border-purple-200 dark:bg-purple-500/20 dark:text-purple-300 dark:border-purple-500/30' :
                                            member.role === 'ADMIN' ? 'bg-blue-100 text-blue-800 border-blue-200 dark:bg-blue-500/20 dark:text-blue-300 dark:border-blue-500/30' :
                                                'bg-gray-100 text-gray-800 border-gray-200 dark:bg-muted dark:text-muted-foreground dark:border-border'
                                            }`}>
                                            {member.role}
                                        </span>
                                    </td>
                                    <td className="px-6 py-4">
                                        <code className="text-[10px] font-mono text-muted-foreground bg-muted p-1 rounded">
                                            {member.user_id.substring(0, 8)}...
                                        </code>
                                    </td>
                                </tr>
                            ))
                        )}
                    </tbody>
                </table>
            </div>

            {/* Invite Modal */}
            <Modal open={isInviteOpen} onOpenChange={setIsInviteOpen}>
                <ModalContent>
                    <ModalHeader>
                        <ModalTitle>Add Member</ModalTitle>
                    </ModalHeader>
                    <form onSubmit={handleInvite} className="space-y-4 py-4">
                        <div className="space-y-2">
                            <label className="text-sm font-medium">Email Address</label>
                            <Input
                                type="email"
                                required
                                placeholder="colleague@example.com"
                                value={inviteEmail}
                                onChange={(e) => setInviteEmail(e.target.value)}
                            />
                            <p className="text-xs text-muted-foreground">
                                User must already be registered on this platform.
                            </p>
                        </div>
                        <ModalFooter>
                            <Button type="button" variant="ghost" onClick={() => setIsInviteOpen(false)}>Cancel</Button>
                            <Button type="submit" disabled={inviting}>
                                {inviting ? "Adding..." : "Add Member"}
                            </Button>
                        </ModalFooter>
                    </form>
                </ModalContent>
            </Modal>
        </div>
    );
}
