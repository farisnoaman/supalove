"use client";

import { useState } from "react";
import { Plus, Database, Lock, Type } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { Modal, ModalContent, ModalHeader, ModalTitle, ModalFooter } from "@/components/ui/modal";
import { toast } from "sonner";

interface AddColumnModalProps {
    open: boolean;
    onOpenChange: (open: boolean) => void;
    projectId: string;
    tableName: string;
    onSuccess?: () => void;
}

const DATA_TYPES = [
    { value: "TEXT", label: "text" },
    { value: "INTEGER", label: "int4" },
    { value: "BIGINT", label: "int8" },
    { value: "BOOLEAN", label: "bool" },
    { value: "TIMESTAMPTZ", label: "timestamptz" },
    { value: "UUID", label: "uuid" },
    { value: "JSONB", label: "jsonb" },
    { value: "NUMERIC", label: "numeric" },
    { value: "DATE", label: "date" },
];

export function AddColumnModal({ open, onOpenChange, projectId, tableName, onSuccess }: AddColumnModalProps) {
    const [name, setName] = useState("");
    const [type, setType] = useState("TEXT");
    const [defaultValue, setDefaultValue] = useState("");
    const [isNullable, setIsNullable] = useState(true);
    const [isUnique, setIsUnique] = useState(false);
    const [loading, setLoading] = useState(false);

    const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

    const handleCreate = async () => {
        if (!name) {
            toast.error("Column name is required");
            return;
        }

        setLoading(true);
        try {
            // Construct SQL
            let sql = `ALTER TABLE public."${tableName}" ADD COLUMN "${name}" ${type}`;

            if (!isNullable) sql += " NOT NULL";
            if (isUnique) sql += " UNIQUE";
            if (defaultValue) sql += ` DEFAULT ${defaultValue}`;

            sql += ";";

            const resp = await fetch(`${API_URL}/api/v1/projects/${projectId}/sql`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ sql }),
            });
            const result = await resp.json();

            if (result.success !== false) {
                toast.success(`Column "${name}" added successfully`);
                onOpenChange(false);
                if (onSuccess) onSuccess();
                // Reset form
                setName("");
                setType("TEXT");
                setDefaultValue("");
                setIsNullable(true);
                setIsUnique(false);
            } else {
                toast.error(result.error || "Failed to add column");
            }
        } catch (err: any) {
            toast.error(err.message || "Failed to add column");
        } finally {
            setLoading(false);
        }
    };

    return (
        <Modal open={open} onOpenChange={onOpenChange}>
            <ModalContent className="max-w-md bg-card border-border/40 shadow-2xl glass rounded-2xl p-6">
                <ModalHeader className="mb-4">
                    <div className="flex items-center gap-3">
                        <div className="p-2 bg-primary/10 rounded-lg">
                            <Plus size={20} className="text-primary" />
                        </div>
                        <div>
                            <ModalTitle className="text-xl">Add Column</ModalTitle>
                            <p className="text-xs text-muted-foreground">
                                Add a new column to <span className="font-mono font-bold text-foreground">{tableName}</span>
                            </p>
                        </div>
                    </div>
                </ModalHeader>

                <div className="space-y-4">
                    <div className="space-y-2">
                        <label className="text-xs font-bold uppercase tracking-wider text-muted-foreground">Name</label>
                        <Input
                            placeholder="e.g. status, phone_number"
                            value={name}
                            onChange={(e) => setName(e.target.value)}
                            className="bg-background/50 border-border/40"
                        />
                    </div>

                    <div className="space-y-2">
                        <label className="text-xs font-bold uppercase tracking-wider text-muted-foreground flex items-center gap-2">
                            <Type size={12} /> Data Type
                        </label>
                        <Select value={type} onValueChange={setType}>
                            <SelectTrigger className="bg-background/50 border-border/40">
                                <SelectValue />
                            </SelectTrigger>
                            <SelectContent>
                                {DATA_TYPES.map(t => (
                                    <SelectItem key={t.value} value={t.value}>{t.label}</SelectItem>
                                ))}
                            </SelectContent>
                        </Select>
                    </div>

                    <div className="space-y-2">
                        <label className="text-xs font-bold uppercase tracking-wider text-muted-foreground flex items-center gap-2">
                            <Lock size={12} /> Default Value (Optional)
                        </label>
                        <Input
                            placeholder="NULL, 0, 'active'..."
                            value={defaultValue}
                            onChange={(e) => setDefaultValue(e.target.value)}
                            className="font-mono text-xs bg-background/50 border-border/40"
                        />
                    </div>

                    <div className="flex items-center gap-6 pt-2">
                        <label className="flex items-center gap-2 cursor-pointer group">
                            <input
                                type="checkbox"
                                checked={isNullable}
                                onChange={(e) => setIsNullable(e.target.checked)}
                                className="rounded border-border text-primary focus:ring-primary/20"
                            />
                            <span className="text-sm text-muted-foreground group-hover:text-foreground transition-colors">Nullable</span>
                        </label>
                        <label className="flex items-center gap-2 cursor-pointer group">
                            <input
                                type="checkbox"
                                checked={isUnique}
                                onChange={(e) => setIsUnique(e.target.checked)}
                                className="rounded border-border text-primary focus:ring-primary/20"
                            />
                            <span className="text-sm text-muted-foreground group-hover:text-foreground transition-colors">Unique</span>
                        </label>
                    </div>
                </div>

                <ModalFooter className="flex items-center justify-end gap-3 mt-6">
                    <Button variant="ghost" onClick={() => onOpenChange(false)} disabled={loading}>Cancel</Button>
                    <Button onClick={handleCreate} disabled={loading || !name} className="primary-gradient">
                        {loading ? "Adding..." : "Add Column"}
                    </Button>
                </ModalFooter>
            </ModalContent>
        </Modal>
    );
}
