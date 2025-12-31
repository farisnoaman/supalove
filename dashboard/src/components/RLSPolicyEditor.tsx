"use client";

import { useState, useEffect } from "react";
import { Modal, ModalContent, ModalHeader, ModalTitle, ModalFooter } from "@/components/ui/modal";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { Checkbox } from "@/components/ui/checkbox";
import { toast } from "sonner";
import { Shield, Code2, Info } from "lucide-react";

interface RLSPolicyEditorProps {
    open: boolean;
    onOpenChange: (open: boolean) => void;
    projectId: string;
    tableName: string;
    policy?: any | null;
    onSuccess: () => void;
}

export function RLSPolicyEditor({
    open,
    onOpenChange,
    projectId,
    tableName,
    policy = null,
    onSuccess
}: RLSPolicyEditorProps) {
    const [policyName, setPolicyName] = useState("");
    const [command, setCommand] = useState("SELECT");
    const [roles, setRoles] = useState<string[]>(["authenticated"]);
    const [usingExpression, setUsingExpression] = useState("");
    const [checkExpression, setCheckExpression] = useState("");
    const [saving, setSaving] = useState(false);

    const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

    useEffect(() => {
        if (policy) {
            setPolicyName(policy.policy_name || "");
            setCommand(policy.command || "SELECT");
            setRoles(policy.roles || ["authenticated"]);
            setUsingExpression(policy.using_expression || "");
            setCheckExpression(policy.check_expression || "");
        } else {
            resetForm();
        }
    }, [policy, open]);

    const resetForm = () => {
        setPolicyName("");
        setCommand("SELECT");
        setRoles(["authenticated"]);
        setUsingExpression("");
        setCheckExpression("");
    };

    const handleRoleToggle = (role: string) => {
        setRoles(prev =>
            prev.includes(role)
                ? prev.filter(r => r !== role)
                : [...prev, role]
        );
    };

    const handleSave = async () => {
        if (!policyName.trim()) {
            toast.error("Policy name is required");
            return;
        }

        if (command !== "INSERT" && !usingExpression.trim()) {
            toast.error("USING expression is required for this command");
            return;
        }

        if (command === "INSERT" && !checkExpression.trim()) {
            toast.error("WITH CHECK expression is required for INSERT");
            return;
        }

        setSaving(true);
        try {
            const url = policy
                ? `${API_URL}/api/v1/projects/${projectId}/tables/${tableName}/policies/${policy.policy_name}`
                : `${API_URL}/api/v1/projects/${projectId}/tables/${tableName}/policies`;

            const method = policy ? "PUT" : "POST";

            const token = localStorage.getItem("token");
            const resp = await fetch(url, {
                method,
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${token}`
                },
                body: JSON.stringify({
                    policy_name: policyName,
                    command,
                    roles,
                    using_expression: usingExpression,
                    check_expression: checkExpression || null,
                }),
            });

            const result = await resp.json();

            if (result.success !== false) {
                toast.success(policy ? "Policy updated" : "Policy created");
                onSuccess();
                onOpenChange(false);
                resetForm();
            } else {
                toast.error(result.error || "Failed to save policy");
            }
        } catch (err) {
            toast.error("Network error while saving policy");
        } finally {
            setSaving(false);
        }
    };

    const templates = [
        {
            name: "Users can view their own data",
            command: "SELECT",
            using: "auth.uid() = id",
        },
        {
            name: "Users can update their own data",
            command: "UPDATE",
            using: "auth.uid() = id",
        },
        {
            name: "Users can insert their own data",
            command: "INSERT",
            check: "auth.uid() = id",
        },
        {
            name: "Public read access",
            command: "SELECT",
            using: "true",
        },
    ];

    const applyTemplate = (template: typeof templates[0]) => {
        setPolicyName(template.name);
        setCommand(template.command);
        if (template.using) setUsingExpression(template.using);
        if (template.check) setCheckExpression(template.check);
    };

    return (
        <Modal open={open} onOpenChange={onOpenChange}>
            <ModalContent className="max-w-3xl bg-card border-border/40 shadow-2xl glass rounded-2xl p-6 max-h-[90vh] overflow-y-auto">
                <ModalHeader className="mb-4">
                    <div className="flex items-center gap-3">
                        <div className="p-2 bg-purple-500/10 rounded-lg">
                            <Shield size={24} className="text-purple-500" />
                        </div>
                        <div>
                            <ModalTitle className="text-xl font-bold">
                                {policy ? "Edit RLS Policy" : "Create RLS Policy"}
                            </ModalTitle>
                            <p className="text-sm text-muted-foreground mt-1">
                                For table <span className="font-mono font-bold">{tableName}</span>
                            </p>
                        </div>
                    </div>
                </ModalHeader>

                <div className="space-y-6">
                    {/* Security Warning */}
                    <div className="p-4 bg-amber-500/5 border border-amber-500/20 rounded-xl flex gap-3 items-start">
                        <Info size={16} className="text-amber-500 mt-0.5 flex-shrink-0" />
                        <div className="text-xs text-amber-700 dark:text-amber-400">
                            <p className="font-bold mb-1">Security Notice</p>
                            <p>RLS policies control who can access data. Incorrect policies can expose sensitive data or prevent legitimate access.</p>
                        </div>
                    </div>

                    {/* Templates */}
                    {!policy && (
                        <div>
                            <Label className="text-sm font-bold mb-2 block">Quick Templates</Label>
                            <div className="grid grid-cols-2 gap-2">
                                {templates.map((template, idx) => (
                                    <button
                                        key={idx}
                                        onClick={() => applyTemplate(template)}
                                        className="p-3 text-left border border-border/40 rounded-lg hover:border-primary/40 hover:bg-primary/5 transition-all text-xs"
                                    >
                                        <div className="font-bold text-foreground">{template.name}</div>
                                        <div className="text-muted-foreground mt-1">{template.command}</div>
                                    </button>
                                ))}
                            </div>
                        </div>
                    )}

                    {/* Policy Name */}
                    <div>
                        <Label htmlFor="policyName" className="text-sm font-bold mb-2 block">
                            Policy Name
                        </Label>
                        <Input
                            id="policyName"
                            value={policyName}
                            onChange={(e) => setPolicyName(e.target.value)}
                            placeholder="e.g., users_view_own_data"
                            className="bg-background border-border/50"
                        />
                    </div>

                    {/* Command */}
                    <div>
                        <Label htmlFor="command" className="text-sm font-bold mb-2 block">
                            Command
                        </Label>
                        <Select value={command} onValueChange={setCommand}>
                            <SelectTrigger className="bg-background border-border/50">
                                <SelectValue />
                            </SelectTrigger>
                            <SelectContent>
                                <SelectItem value="ALL">ALL</SelectItem>
                                <SelectItem value="SELECT">SELECT</SelectItem>
                                <SelectItem value="INSERT">INSERT</SelectItem>
                                <SelectItem value="UPDATE">UPDATE</SelectItem>
                                <SelectItem value="DELETE">DELETE</SelectItem>
                            </SelectContent>
                        </Select>
                    </div>

                    {/* Roles */}
                    <div>
                        <Label className="text-sm font-bold mb-2 block">Roles</Label>
                        <div className="flex flex-wrap gap-3">
                            {["public", "anon", "authenticated"].map((role) => (
                                <label key={role} className="flex items-center gap-2 cursor-pointer">
                                    <Checkbox
                                        checked={roles.includes(role)}
                                        onCheckedChange={() => handleRoleToggle(role)}
                                    />
                                    <span className="text-sm font-mono">{role}</span>
                                </label>
                            ))}
                        </div>
                    </div>

                    {/* USING Expression */}
                    <div>
                        <Label htmlFor="usingExpr" className="text-sm font-bold mb-2 flex items-center gap-2">
                            <Code2 size={14} />
                            USING Expression
                        </Label>
                        <textarea
                            id="usingExpr"
                            value={usingExpression}
                            onChange={(e) => setUsingExpression(e.target.value)}
                            placeholder="e.g., auth.uid() = user_id"
                            className="w-full h-24 px-3 py-2 bg-background border border-border/50 rounded-lg font-mono text-sm resize-none focus:outline-none focus:ring-2 focus:ring-primary/50"
                        />
                        <p className="text-xs text-muted-foreground mt-1">
                            Determines which rows are visible to the role
                        </p>
                    </div>

                    {/* WITH CHECK Expression */}
                    {(command === "INSERT" || command === "UPDATE" || command === "ALL") && (
                        <div>
                            <Label htmlFor="checkExpr" className="text-sm font-bold mb-2 flex items-center gap-2">
                                <Code2 size={14} />
                                WITH CHECK Expression <span className="text-muted-foreground font-normal">(optional)</span>
                            </Label>
                            <textarea
                                id="checkExpr"
                                value={checkExpression}
                                onChange={(e) => setCheckExpression(e.target.value)}
                                placeholder="e.g., auth.uid() = user_id"
                                className="w-full h-24 px-3 py-2 bg-background border border-border/50 rounded-lg font-mono text-sm resize-none focus:outline-none focus:ring-2 focus:ring-primary/50"
                            />
                            <p className="text-xs text-muted-foreground mt-1">
                                Determines which rows can be inserted/updated by the role
                            </p>
                        </div>
                    )}
                </div>

                <ModalFooter className="flex items-center justify-end gap-3 mt-8">
                    <Button
                        variant="ghost"
                        onClick={() => onOpenChange(false)}
                        disabled={saving}
                        className="rounded-xl"
                    >
                        Cancel
                    </Button>
                    <Button
                        onClick={handleSave}
                        disabled={saving}
                        className="bg-purple-600 hover:bg-purple-700 text-white px-6 rounded-xl shadow-lg shadow-purple-500/20"
                    >
                        {saving ? "Saving..." : policy ? "Update Policy" : "Create Policy"}
                    </Button>
                </ModalFooter>
            </ModalContent>
        </Modal>
    );
}
