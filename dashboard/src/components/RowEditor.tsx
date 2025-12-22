"use client";

import { useState, useEffect } from "react";
import { X, Save, Lock, Terminal, Database, Columns, RefreshCw, Plus } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Modal, ModalContent, ModalHeader, ModalTitle } from "@/components/ui/modal";
import { toast } from "sonner";
import { cn } from "@/lib/utils";

interface RowEditorProps {
    open: boolean;
    onOpenChange: (open: boolean) => void;
    projectId: string;
    tableName: string;
    onSuccess?: () => void;
}

interface DBColumn {
    column_name: string;
    data_type: string;
    is_nullable: string;
    column_default: string | null;
}

export function RowEditor({ open, onOpenChange, projectId, tableName, onSuccess }: RowEditorProps) {
    const [schema, setSchema] = useState<DBColumn[]>([]);
    const [rowValues, setRowValues] = useState<Record<string, any>>({});
    const [loading, setLoading] = useState(false);
    const [saving, setSaving] = useState(false);

    const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

    useEffect(() => {
        if (open) {
            fetchSchema();
        }
    }, [open, projectId, tableName]);

    const fetchSchema = async () => {
        setLoading(true);
        try {
            const token = localStorage.getItem("token");
            const resp = await fetch(`${API_URL}/api/v1/projects/${projectId}/tables/${tableName}/schema`, {
                headers: {
                    "Authorization": `Bearer ${token}`
                }
            });
            if (!resp.ok) throw new Error("Failed to fetch schema");
            const data = await resp.json();
            setSchema(data);

            // Initialize values: undefined means "use database default/null"
            const initialValues: Record<string, any> = {};
            data.forEach((col: DBColumn) => {
                initialValues[col.column_name] = undefined;
            });
            setRowValues(initialValues);
        } catch (err) {
            toast.error("Failed to load table structure");
            console.error(err);
        } finally {
            setLoading(false);
        }
    };

    const handleValueChange = (column: string, value: any) => {
        setRowValues(prev => ({ ...prev, [column]: value }));
    };

    const generateInsertSQL = () => {
        // Only include columns where the user explicitly set a value
        const columnsToInsert = Object.entries(rowValues)
            .filter(([_, value]) => value !== undefined && value !== "")
            .map(([col, _]) => col);

        if (columnsToInsert.length === 0) return "";

        const values = columnsToInsert.map(col => {
            const val = rowValues[col];
            const colSchema = schema.find(s => s.column_name === col);

            if (val === null) return "NULL";

            const type = colSchema?.data_type.toUpperCase() || "";

            // Handle numeric types
            if (type.includes("INT") || type.includes("SERIAL") || type.includes("NUMERIC") || type.includes("DECIMAL") || type.includes("REAL") || type.includes("DOUBLE")) {
                const numericVal = Number(val);
                return isNaN(numericVal) ? "NULL" : val;
            }

            // Handle booleans
            if (type.includes("BOOL")) {
                return val === "true" || val === true ? "TRUE" : "FALSE";
            }

            // Default to string escaping
            return `'${String(val).replace(/'/g, "''")}'`;
        });

        return `INSERT INTO public.${tableName} (${columnsToInsert.join(", ")})\nVALUES (${values.join(", ")})\nRETURNING *;`;
    };

    const handleSave = async () => {
        const sql = generateInsertSQL();
        if (!sql) {
            toast.error("Please provide at least one value");
            return;
        }

        setSaving(true);
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
                toast.success("Row inserted successfully");
                onSuccess?.();
                onOpenChange(false);
            } else {
                toast.error(result.error || "Failed to insert row");
            }
        } catch (err) {
            toast.error("Network error while saving row");
        } finally {
            setSaving(false);
        }
    };

    return (
        <Modal open={open} onOpenChange={onOpenChange}>
            <ModalContent className="max-w-2xl bg-card border-border/40 shadow-2xl overflow-hidden p-0 rounded-3xl glass animate-in zoom-in-95 duration-200">
                <ModalHeader className="p-6 border-b border-border/20 bg-muted/30">
                    <div className="flex items-center gap-3">
                        <div className="p-2 bg-emerald-500/10 rounded-lg">
                            <Plus size={20} className="text-emerald-500" />
                        </div>
                        <div>
                            <ModalTitle className="text-2xl font-bold tracking-tight">Insert Row</ModalTitle>
                            <p className="text-xs text-muted-foreground mt-0.5">
                                Add a new entry to <span className="font-mono text-foreground font-medium">public.{tableName}</span>
                            </p>
                        </div>
                    </div>
                </ModalHeader>

                <div className="p-0 max-h-[60vh] overflow-y-auto custom-scrollbar">
                    {loading ? (
                        <div className="p-12 space-y-6">
                            {[...Array(3)].map((_, i) => (
                                <div key={i} className="space-y-2">
                                    <div className="h-4 w-1/4 bg-muted animate-pulse rounded" />
                                    <div className="h-10 w-full bg-muted animate-pulse rounded-xl" />
                                </div>
                            ))}
                        </div>
                    ) : (
                        <div className="divide-y divide-border/10">
                            {schema.map((col) => (
                                <div key={col.column_name} className="p-6 grid grid-cols-1 md:grid-cols-12 gap-6 hover:bg-muted/5 transition-colors group">
                                    <div className="md:col-span-4 space-y-1">
                                        <div className="flex items-center gap-2">
                                            <span className="text-sm font-bold text-foreground group-hover:text-primary transition-colors">
                                                {col.column_name}
                                            </span>
                                            {col.is_nullable === "NO" && col.column_default === null && (
                                                <span className="text-[10px] text-destructive font-bold uppercase tracking-widest">* Required</span>
                                            )}
                                        </div>
                                        <p className="text-[10px] text-muted-foreground/60 uppercase tracking-widest font-bold font-mono">
                                            {col.data_type}
                                        </p>
                                    </div>
                                    <div className="md:col-span-8">
                                        {rowValues[col.column_name] === undefined ? (
                                            <div className="flex items-center justify-between p-3 rounded-xl bg-muted/40 border border-border/20 group cursor-pointer hover:border-primary/20"
                                                onClick={() => handleValueChange(col.column_name, "")}>
                                                <div className="flex items-center gap-2 text-xs text-muted-foreground italic font-mono">
                                                    <Lock size={12} />
                                                    {col.column_default ? `Default: ${col.column_default.split('::')[0]}` : "NULL"}
                                                </div>
                                                <Button variant="ghost" size="sm" className="h-6 text-[10px] uppercase tracking-tighter hover:bg-primary/10 hover:text-primary">
                                                    Override
                                                </Button>
                                            </div>
                                        ) : col.data_type.toUpperCase().includes("BOOL") ? (
                                            <div className="flex gap-2">
                                                <Button
                                                    variant={rowValues[col.column_name] === "true" ? "default" : "outline"}
                                                    size="sm"
                                                    className="flex-1"
                                                    onClick={() => handleValueChange(col.column_name, "true")}
                                                >
                                                    true
                                                </Button>
                                                <Button
                                                    variant={rowValues[col.column_name] === "false" ? "default" : "outline"}
                                                    size="sm"
                                                    className="flex-1"
                                                    onClick={() => handleValueChange(col.column_name, "false")}
                                                >
                                                    false
                                                </Button>
                                                <Button
                                                    variant="ghost"
                                                    size="sm"
                                                    onClick={() => handleValueChange(col.column_name, undefined)}
                                                >
                                                    <X size={14} />
                                                </Button>
                                            </div>
                                        ) : (
                                            <div className="relative group/input">
                                                <Input
                                                    placeholder={`Enter ${col.data_type.toLowerCase()}`}
                                                    value={rowValues[col.column_name] ?? ""}
                                                    onChange={(e) => handleValueChange(col.column_name, e.target.value)}
                                                    className="bg-background border-border/40 focus:border-primary/40 focus:ring-primary/10 rounded-xl pr-10"
                                                />
                                                <button
                                                    onClick={() => handleValueChange(col.column_name, undefined)}
                                                    className="absolute right-3 top-1/2 -translate-y-1/2 text-muted-foreground hover:text-foreground opacity-0 group-hover/input:opacity-100 transition-opacity"
                                                >
                                                    <X size={14} />
                                                </button>
                                            </div>
                                        )}
                                    </div>
                                </div>
                            ))}
                        </div>
                    )}
                </div>

                {/* Footer and SQL Preview */}
                <div className="p-6 border-t border-border/20 bg-muted/30 space-y-6">
                    <div className="bg-card/50 border border-border/40 rounded-2xl overflow-hidden shadow-inner">
                        <div className="px-4 py-2 border-b border-border/30 bg-muted/20 flex items-center gap-2 font-mono italic">
                            <Terminal size={14} className="text-muted-foreground" />
                            <span className="text-[10px] font-bold uppercase tracking-widest text-muted-foreground">SQL Execution Preview</span>
                        </div>
                        <pre className="p-4 text-xs font-mono text-emerald-600 dark:text-emerald-400 overflow-x-auto whitespace-pre-wrap max-h-24">
                            {generateInsertSQL() || "-- Provide values to see the generated SQL"}
                        </pre>
                    </div>

                    <div className="flex items-center justify-between">
                        <Button variant="ghost" onClick={() => onOpenChange(false)} className="text-muted-foreground hover:text-foreground">
                            Discard
                        </Button>
                        <Button
                            onClick={handleSave}
                            disabled={saving || loading}
                            className="primary-gradient shadow-lg shadow-emerald-500/20 px-10 h-11 rounded-2xl min-w-[140px]"
                        >
                            {saving ? (
                                <RefreshCw size={18} className="animate-spin" />
                            ) : (
                                <span className="flex items-center gap-2 font-bold tracking-tight">
                                    <Save size={18} />
                                    Save Row
                                </span>
                            )}
                        </Button>
                    </div>
                </div>
            </ModalContent>
        </Modal>
    );
}
