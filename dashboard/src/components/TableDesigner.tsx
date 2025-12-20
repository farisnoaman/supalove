"use client";

import { useState } from "react";
import { Plus, Trash2, X } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Select } from "@/components/ui/select";
import { Modal, ModalContent, ModalHeader, ModalTitle, ModalFooter, ModalClose } from "@/components/ui/modal";
import { toast } from "sonner";

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
    { value: "TEXT", label: "TEXT" },
    { value: "INTEGER", label: "INTEGER" },
    { value: "BIGINT", label: "BIGINT" },
    { value: "BOOLEAN", label: "BOOLEAN" },
    { value: "TIMESTAMPTZ", label: "TIMESTAMPTZ" },
    { value: "UUID", label: "UUID" },
    { value: "JSONB", label: "JSONB" },
    { value: "NUMERIC", label: "NUMERIC" },
];

export function TableDesigner({ open, onOpenChange, projectId, onSuccess }: TableDesignerProps) {
    const [tableName, setTableName] = useState("");
    const [columns, setColumns] = useState<Column[]>([
        { name: "id", type: "BIGINT", isPrimaryKey: true, isUnique: false, isNotNull: true, defaultValue: "" },
    ]);
    const [creating, setCreating] = useState(false);

    const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

    const addColumn = () => {
        setColumns([
            ...columns,
            { name: "", type: "TEXT", isPrimaryKey: false, isUnique: false, isNotNull: false, defaultValue: "" },
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

        return `CREATE TABLE ${tableName} (\n${columnDefs.join(",\n")}\n);`;
    };

    const createTable = async () => {
        const sql = generateSQL();
        if (!sql) {
            toast.error("Please provide a table name and at least one column");
            return;
        }

        setCreating(true);
        try {
            const resp = await fetch(`${API_URL}/v1/projects/${projectId}/sql`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ sql }),
            });
            const result = await resp.json();

            if (result.success !== false) {
                toast.success(`Table "${tableName}" created successfully`);
                onOpenChange(false);
                if (onSuccess) onSuccess();
                // Reset form
                setTableName("");
                setColumns([{ name: "id", type: "BIGINT", isPrimaryKey: true, isUnique: false, isNotNull: true, defaultValue: "" }]);
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
            <ModalContent className="max-w-3xl max-h-[90vh] overflow-y-auto">
                <ModalClose onClose={() => onOpenChange(false)} />
                <ModalHeader>
                    <ModalTitle>Create new table</ModalTitle>
                </ModalHeader>

                <div className="space-y-6">
                    {/* Table Name */}
                    <div>
                        <label className="block text-sm font-medium mb-2">Table Name</label>
                        <Input
                            placeholder="users, products, orders..."
                            value={tableName}
                            onChange={(e) => setTableName(e.target.value)}
                        />
                    </div>

                    {/* Columns */}
                    <div>
                        <div className="flex items-center justify-between mb-3">
                            <label className="block text-sm font-medium">Columns</label>
                            <Button variant="outline" size="sm" onClick={addColumn} className="gap-2">
                                <Plus size={14} />
                                Add Column
                            </Button>
                        </div>

                        <div className="space-y-3">
                            {columns.map((column, index) => (
                                <div key={index} className="p-4 border border-border rounded-lg space-y-3">
                                    <div className="flex items-start gap-3">
                                        <div className="flex-1 grid grid-cols-2 gap-3">
                                            <div>
                                                <label className="block text-xs text-muted-foreground mb-1">Name</label>
                                                <Input
                                                    placeholder="column_name"
                                                    value={column.name}
                                                    onChange={(e) => updateColumn(index, "name", e.target.value)}
                                                />
                                            </div>
                                            <div>
                                                <label className="block text-xs text-muted-foreground mb-1">Type</label>
                                                <Select
                                                    options={DATA_TYPES}
                                                    value={column.type}
                                                    onChange={(e) => updateColumn(index, "type", e.target.value)}
                                                />
                                            </div>
                                        </div>
                                        {columns.length > 1 && (
                                            <Button
                                                variant="ghost"
                                                size="icon"
                                                onClick={() => removeColumn(index)}
                                                className="mt-6"
                                            >
                                                <Trash2 size={16} />
                                            </Button>
                                        )}
                                    </div>

                                    <div className="flex items-center gap-4 text-sm">
                                        <label className="flex items-center gap-2 cursor-pointer">
                                            <input
                                                type="checkbox"
                                                checked={column.isPrimaryKey}
                                                onChange={(e) => updateColumn(index, "isPrimaryKey", e.target.checked)}
                                                className="rounded border-border"
                                            />
                                            <span>Primary Key</span>
                                        </label>
                                        <label className="flex items-center gap-2 cursor-pointer">
                                            <input
                                                type="checkbox"
                                                checked={column.isUnique}
                                                onChange={(e) => updateColumn(index, "isUnique", e.target.checked)}
                                                disabled={column.isPrimaryKey}
                                                className="rounded border-border"
                                            />
                                            <span>Unique</span>
                                        </label>
                                        <label className="flex items-center gap-2 cursor-pointer">
                                            <input
                                                type="checkbox"
                                                checked={column.isNotNull}
                                                onChange={(e) => updateColumn(index, "isNotNull", e.target.checked)}
                                                disabled={column.isPrimaryKey}
                                                className="rounded border-border"
                                            />
                                            <span>Not Null</span>
                                        </label>
                                    </div>

                                    <div>
                                        <label className="block text-xs text-muted-foreground mb-1">Default Value (optional)</label>
                                        <Input
                                            placeholder="NULL, NOW(), 0, 'default'..."
                                            value={column.defaultValue}
                                            onChange={(e) => updateColumn(index, "defaultValue", e.target.value)}
                                        />
                                    </div>
                                </div>
                            ))}
                        </div>
                    </div>

                    {/* SQL Preview */}
                    <div>
                        <label className="block text-sm font-medium mb-2">SQL Preview</label>
                        <pre className="p-4 bg-muted rounded-lg text-xs font-mono overflow-x-auto">
                            {generateSQL() || "-- Configure your table above"}
                        </pre>
                    </div>
                </div>

                <ModalFooter>
                    <Button variant="outline" onClick={() => onOpenChange(false)}>
                        Cancel
                    </Button>
                    <Button onClick={createTable} disabled={creating || !tableName || columns.length === 0}>
                        {creating ? "Creating..." : "Create Table"}
                    </Button>
                </ModalFooter>
            </ModalContent>
        </Modal>
    );
}
