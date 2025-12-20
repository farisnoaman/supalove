"use client";

import React, { useRef, useState, useEffect } from "react";
import Editor from "@monaco-editor/react";
import { Play, Download, History, Sparkles, Clock } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Modal, ModalContent, ModalHeader, ModalTitle, ModalClose } from "@/components/ui/modal";

interface SQLEditorProps {
    projectId: string;
    onExecute?: (sql: string) => void;
}

interface QueryHistoryItem {
    sql: string;
    timestamp: number;
    success?: boolean;
}

export default function SQLEditor({ projectId, onExecute }: SQLEditorProps) {
    const [sql, setSql] = useState("");
    const [theme, setTheme] = useState<"light" | "vs-dark">("vs-dark");
    const [showHistory, setShowHistory] = useState(false);
    const [history, setHistory] = useState<QueryHistoryItem[]>([]);
    const editorRef = useRef<any>(null);

    // Load history from localStorage
    useEffect(() => {
        const stored = localStorage.getItem(`sql-history-${projectId}`);
        if (stored) {
            try {
                setHistory(JSON.parse(stored));
            } catch (e) {
                console.error("Failed to parse history", e);
            }
        }
    }, [projectId]);

    // Save to history
    const saveToHistory = (query: string, success: boolean = true) => {
        const newItem: QueryHistoryItem = {
            sql: query,
            timestamp: Date.now(),
            success,
        };
        const newHistory = [newItem, ...history].slice(0, 50); // Keep last 50
        setHistory(newHistory);
        localStorage.setItem(`sql-history-${projectId}`, JSON.stringify(newHistory));
    };

    const handleEditorDidMount = (editor: any, monaco: any) => {
        editorRef.current = editor;

        // Add keyboard shortcut for execute (Cmd+Enter / Ctrl+Enter)
        editor.addCommand(monaco.KeyMod.CtrlCmd | monaco.KeyCode.Enter, () => {
            handleExecute();
        });
    };

    const handleExecute = () => {
        const selectedText = editorRef.current?.getModel()?.getValueInRange(
            editorRef.current?.getSelection()
        );
        const queryToRun = selectedText || sql;
        if (onExecute && queryToRun) {
            saveToHistory(queryToRun);
            onExecute(queryToRun);
        }
    };

    const handleFormat = () => {
        editorRef.current?.getAction("editor.action.formatDocument")?.run();
    };

    const exportSQL = () => {
        const blob = new Blob([sql], { type: "text/plain" });
        const url = URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url;
        a.download = `query-${Date.now()}.sql`;
        a.click();
        URL.revokeObjectURL(url);
    };

    const loadFromHistory = (item: QueryHistoryItem) => {
        setSql(item.sql);
        setShowHistory(false);
    };

    const clearHistory = () => {
        setHistory([]);
        localStorage.removeItem(`sql-history-${projectId}`);
    };

    return (
        <div className="flex flex-col h-full">
            {/* Toolbar */}
            <div className="flex items-center justify-between p-3 border-b bg-card">
                <div className="flex items-center gap-2">
                    <Button onClick={handleExecute} size="sm" className="gap-2">
                        <Play size={14} />
                        Run (⌘↵)
                    </Button>
                    <Button onClick={handleFormat} variant="outline" size="sm" className="gap-2">
                        <Sparkles size={14} />
                        Format
                    </Button>
                </div>
                <div className="flex items-center gap-2">
                    <Button
                        variant="ghost"
                        size="sm"
                        title="Query History"
                        onClick={() => setShowHistory(true)}
                    >
                        <History size={16} />
                    </Button>
                    <Button onClick={exportSQL} variant="ghost" size="sm" title="Export SQL">
                        <Download size={16} />
                    </Button>
                    <Button
                        variant="ghost"
                        size="sm"
                        onClick={() => setTheme(theme === "light" ? "vs-dark" : "light")}
                    >
                        {theme === "light" ? "🌙" : "☀️"}
                    </Button>
                </div>
            </div>

            {/* Editor */}
            <div className="flex-1">
                <Editor
                    height="100%"
                    defaultLanguage="sql"
                    theme={theme}
                    value={sql}
                    onChange={(value) => setSql(value || "")}
                    onMount={handleEditorDidMount}
                    options={{
                        minimap: { enabled: true },
                        fontSize: 14,
                        lineNumbers: "on",
                        scrollBeyondLastLine: false,
                        automaticLayout: true,
                        tabSize: 2,
                        wordWrap: "on",
                        formatOnPaste: true,
                        formatOnType: true,
                        suggestOnTriggerCharacters: true,
                        quickSuggestions: true,
                    }}
                />
            </div>

            {/* History Modal */}
            <Modal open={showHistory} onOpenChange={setShowHistory}>
                <ModalContent className="max-w-2xl">
                    <ModalClose onClose={() => setShowHistory(false)} />
                    <ModalHeader>
                        <ModalTitle>Query History</ModalTitle>
                    </ModalHeader>
                    <div className="space-y-2 max-h-96 overflow-y-auto">
                        {history.length === 0 ? (
                            <p className="text-muted-foreground text-sm text-center py-8">
                                No query history yet
                            </p>
                        ) : (
                            history.map((item, index) => (
                                <div
                                    key={index}
                                    className="p-3 border rounded-lg hover:bg-muted cursor-pointer transition-colors"
                                    onClick={() => loadFromHistory(item)}
                                >
                                    <div className="flex items-center justify-between mb-2">
                                        <div className="flex items-center gap-2 text-xs text-muted-foreground">
                                            <Clock size={12} />
                                            {new Date(item.timestamp).toLocaleString()}
                                        </div>
                                    </div>
                                    <pre className="text-xs font-mono bg-muted p-2 rounded overflow-x-auto">
                                        {item.sql}
                                    </pre>
                                </div>
                            ))
                        )}
                    </div>
                    {history.length > 0 && (
                        <div className="mt-4 flex justify-end">
                            <Button variant="outline" size="sm" onClick={clearHistory}>
                                Clear History
                            </Button>
                        </div>
                    )}
                </ModalContent>
            </Modal>
        </div>
    );
}
