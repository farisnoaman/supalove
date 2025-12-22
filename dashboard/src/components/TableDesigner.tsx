"use client";

import { useState } from "react";
import { Plus, Trash2, X, Database, Shield, Lock, Settings2 } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { Modal, ModalContent, ModalHeader, ModalTitle, ModalFooter, ModalClose } from "@/components/ui/modal";
import { toast } from "sonner";
import { cn } from "@/lib/utils";

interface Column {
    name: string;
    type: string;
    isPrimaryKey: boolean;
    isUnique: boolean;
    isNotNull: boolean;
    defaultValue: string;
}

interface TableDesignerProps {
    open: boolean;
    onOpenChange: (open: boolean) => void;
    projectId: string;
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
];

export function TableDesigner({ open, onOpenChange, projectId, onSuccess }: TableDesignerProps) {
    const [tableName, setTableName] = useState("");
    const [columns, setColumns] = useState<Column[]>([
        { name: "id", type: "UUID", isPrimaryKey: true, isUnique: false, isNotNull: true, defaultValue: "gen_random_uuid()" },
        { name: "created_at", type: "TIMESTAMPTZ", isPrimaryKey: false, isUnique: false, isNotNull: true, defaultValue: "now()" },
        { name: "updated_at", type: "TIMESTAMPTZ", isPrimaryKey: false, isUnique: false, isNotNull: true, defaultValue: "now()" },
    ]);
    const [creating, setCreating] = useState(false);

    const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

    const addColumn = () => {
        setColumns([
            ...columns,
            { name: `col_${columns.length}`, type: "TEXT", isPrimaryKey: false, isUnique: false, isNotNull: false, defaultValue: "" },
        ]);
    };

    const removeColumn = (index: number) => {
        setColumns(columns.filter((_, i) => i !== index));
    };

    const updateColumn = (index: number, field: keyof Column, value: any) => {
        const newColumns = [...columns];
        newColumns[index] = { ...newColumns[index], [field]: value };
        setColumns(newColumns);
    };

    const generateSQL = () => {
        if (!tableName || columns.length === 0) return "";

        const columnDefs = columns.map((col) => {
            let def = `  ${col.name} ${col.type}`;
            if (col.isPrimaryKey) def += " PRIMARY KEY";
            if (col.isUnique && !col.isPrimaryKey) def += " UNIQUE";
            if (col.isNotNull && !col.isPrimaryKey) def += " NOT NULL";
            if (col.defaultValue) def += ` DEFAULT ${col.defaultValue}`;
            return def;
        });

        return `CREATE TABLE public.${tableName} (\n${columnDefs.join(",\n")}\n);`;
    };

    const createTable = async () => {
        const sql = generateSQL();
        if (!sql) {
            toast.error("Please provide a table name and at least one column");
            return;
        }

        setCreating(true);
        try {
            const token = localStorage.getItem("token");
            const resp = await fetch(`${API_URL}/api/v1/projects/${projectId}/sql`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${token}`
                },
                body: JSON.stringify({ sql }),
            });
            const result = await resp.json();

            if (result.success !== false) {
                toast.success(`Table "${tableName}" created successfully`, {
                    description: "Your data structure is now live.",
                });
                onOpenChange(false);
                if (onSuccess) onSuccess();
                setTableName("");
                setColumns([
                    { name: "id", type: "UUID", isPrimaryKey: true, isUnique: false, isNotNull: true, defaultValue: "gen_random_uuid()" },
                    { name: "created_at", type: "TIMESTAMPTZ", isPrimaryKey: false, isUnique: false, isNotNull: true, defaultValue: "now()" },
                    { name: "updated_at", type: "TIMESTAMPTZ", isPrimaryKey: false, isUnique: false, isNotNull: true, defaultValue: "now()" },
                ]);
            } else {
                toast.error(result.error || "Failed to create table");
            }
        } catch (err: any) {
            toast.error(err.message || "Failed to create table");
        } finally {
            setCreating(false);
        }
    };

    return (
        <Modal open={open} onOpenChange={onOpenChange}>
            <ModalContent className="max-w-4xl max-h-[95vh] overflow-hidden flex flex-col p-0 border-none bg-background shadow-2xl">
                <div className="flex items-center justify-between p-6 border-b border-border/40 bg-card/50 backdrop-blur-md">
                    <div className="flex items-center gap-3">
                        <div className="p-2 bg-primary/10 rounded-lg">
                            <Database size={20} className="text-primary" />
                        </div>
                        <div>
                            <ModalTitle className="text-xl">Table Designer</ModalTitle>
                            <p className="text-xs text-muted-foreground">Create a new relational table in your project.</p>
                        </div>
                    </div>
                </div>

                <div className="flex-1 overflow-y-auto p-6 space-y-8 subtle-gradient">
                    {/* Table Configuration */}
                    <div className="space-y-4">
                        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                            <div className="space-y-2">
                                <label className="text-xs font-bold uppercase tracking-wider text-muted-foreground">Table Name</label>
                                <Input
                                    placeholder="e.g. products, orders, customers"
                                    value={tableName}
                                    onChange={(e) => setTableName(e.target.value)}
                                    className="bg-card border-border/50 focus:border-primary/50"
                                />
                            </div>
                            <div className="space-y-2">
                                <label className="text-xs font-bold uppercase tracking-wider text-muted-foreground">Schema</label>
                                <Input value="public" disabled className="bg-muted/50 border-border/30 italic" />
                            </div>
                        </div>
                    </div>

                    {/* Columns Builder */}
                    <div className="space-y-6">
                        <div className="flex items-center justify-between">
                            <h3 className="text-sm font-bold flex items-center gap-2">
                                <Settings2 size={16} className="text-muted-foreground" />
                                Columns Configuration
                            </h3>
                            <Button variant="outline" size="sm" onClick={addColumn} className="gap-2 border-emerald-500/20 text-emerald-600 dark:text-emerald-400 hover:bg-emerald-500/10">
                                <Plus size={14} />
                                Add New Column
                            </Button>
                        </div>

                        <div className="space-y-4">
                            {columns.map((column, index) => (
                                <div key={index} className="group relative p-6 bg-card border border-border/40 rounded-xl hover:border-primary/30 transition-all shadow-sm">
                                    <div className="grid grid-cols-1 md:grid-cols-12 gap-6 items-start">
                                        <div className="md:col-span-4 space-y-2">
                                            <label className="text-[10px] font-bold uppercase tracking-widest text-muted-foreground/60">Name</label>
                                            <Input
                                                placeholder="column_name"
                                                value={column.name}
                                                onChange={(e) => updateColumn(index, "name", e.target.value)}
                                                className="bg-background border-border/40"
                                            />
                                        </div>
                                        <div className="md:col-span-3 space-y-2">
                                            <label className="text-[10px] font-bold uppercase tracking-widest text-muted-foreground/60">Type</label>
                                            <Select
                                                value={column.type}
                                                onValueChange={(val) => updateColumn(index, "type", val)}
                                            >
                                                <SelectTrigger className="h-10 bg-background border-border/40">
                                                    <SelectValue placeholder="Select type" />
                                                </SelectTrigger>
                                                <SelectContent>
                                                    {DATA_TYPES.map((type) => (
                                                        <SelectItem key={type.value} value={type.value}>
                                                            {type.label}
                                                        </SelectItem>
                                                    ))}
                                                </SelectContent>
                                            </Select>
                                        </div>
                                        <div className="md:col-span-4 flex items-center gap-4 mt-8">
                                            <label className="flex items-center gap-2 cursor-pointer group/toggle">
                                                <input
                                                    type="checkbox"
                                                    checked={column.isPrimaryKey}
                                                    onChange={(e) => updateColumn(index, "isPrimaryKey", e.target.checked)}
                                                    className="w-4 h-4 rounded border-border text-primary focus:ring-primary/20"
                                                />
                                                <span className="text-xs font-medium text-muted-foreground group-hover/toggle:text-foreground">PK</span>
                                            </label>
                                            <label className="flex items-center gap-2 cursor-pointer group/toggle">
                                                <input
                                                    type="checkbox"
                                                    checked={column.isUnique}
                                                    onChange={(e) => updateColumn(index, "isUnique", e.target.checked)}
                                                    disabled={column.isPrimaryKey}
                                                    className="w-4 h-4 rounded border-border text-primary focus:ring-primary/20"
                                                />
                                                <span className="text-xs font-medium text-muted-foreground group-hover/toggle:text-foreground">Unique</span>
                                            </label>
                                            <label className="flex items-center gap-2 cursor-pointer group/toggle">
                                                <input
                                                    type="checkbox"
                                                    checked={column.isNotNull}
                                                    onChange={(e) => updateColumn(index, "isNotNull", e.target.checked)}
                                                    disabled={column.isPrimaryKey}
                                                    className="w-4 h-4 rounded border-border text-primary focus:ring-primary/20"
                                                />
                                                <span className="text-xs font-medium text-muted-foreground group-hover/toggle:text-foreground">Not Null</span>
                                            </label>
                                        </div>
                                        <div className="md:col-span-1 flex justify-end mt-7">
                                            <Button
                                                variant="ghost"
                                                size="icon"
                                                onClick={() => removeColumn(index)}
                                                disabled={columns.length === 1}
                                                className="text-muted-foreground hover:text-destructive hover:bg-destructive/10 transition-colors"
                                            >
                                                <Trash2 size={16} />
                                            </Button>
                                        </div>
                                    </div>

                                    <div className="mt-4 pt-4 border-t border-border/30">
                                        <div className="flex items-center gap-2 text-xs text-muted-foreground mb-2">
                                            <Lock size={12} />
                                            Default Value (optional)
                                        </div>
                                        <Input
                                            placeholder="NULL, 0, 'default', gen_random_uuid()..."
                                            value={column.defaultValue}
                                            onChange={(e) => updateColumn(index, "defaultValue", e.target.value)}
                                            className="bg-background/50 border-border/30 h-8 text-xs font-mono"
                                        />
                                    </div>
                                </div>
                            ))}
                        </div>
                    </div>

                    {/* SQL Preview Section */}
                    <div className="bg-card/50 border border-border/40 rounded-xl overflow-hidden shadow-inner">
                        <div className="px-4 py-2 border-b border-border/30 bg-muted/40 flex items-center gap-2">
                            <Terminal size={14} className="text-muted-foreground" />
                            <span className="text-[10px] font-bold uppercase tracking-widest text-muted-foreground">SQL Preview</span>
                        </div>
                        <pre className="p-4 text-xs font-mono text-emerald-600 dark:text-emerald-400 overflow-x-auto">
                            {generateSQL() || "-- Configure your table above to see SQL preview"}
                        </pre>
                    </div>
                </div>

                <div className="p-6 border-t border-border/40 bg-card/50 backdrop-blur-md flex items-center justify-between">
                    <Button variant="ghost" onClick={() => onOpenChange(false)} className="text-muted-foreground hover:text-foreground">
                        Cancel
                    </Button>
                    <div className="flex items-center gap-3">
                        <div className="text-right hidden md:block">
                            <p className="text-[10px] text-muted-foreground font-mono">public.{tableName || "untitled"}</p>
                            <p className="text-[10px] text-muted-foreground">{columns.length} columns defined</p>
                        </div>
                        <Button
                            onClick={createTable}
                            disabled={creating || !tableName || columns.length === 0}
                            className="primary-gradient shadow-lg shadow-emerald-500/20 px-8"
                        >
                            {creating ? "Creating..." : "Save Table"}
                        </Button>
                    </div>
                </div>
            </ModalContent>
        </Modal>
    );
}

const Terminal = ({ size, className }: { size?: number, className?: string }) => (
    <svg
        width={size || 24}
        height={size || 24}
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        strokeWidth="2"
        strokeLinecap="round"
        strokeLinejoin="round"
        className={className}
    >
        <polyline points="4 17 10 11 4 5" />
        <line x1="12" y1="19" x2="20" y2="19" />
    </svg>
);
