"use client";

import { useState } from "react";
import Link from "next/link";
import { useParams, usePathname } from "next/navigation";
import {
    LayoutGrid,
    Database,
    Users,
    Folder,
    Code2,
    Cpu,
    Key,
    FileText,
    Settings,
    Shield,
    Terminal,
    Archive,
    Menu,
    X,
    Bell,
} from "lucide-react";
import { cn } from "@/lib/utils";
import { useOrg } from "@/components/providers/org-provider";

const sidebarSections = [
    {
        title: "Project",
        items: [
            { href: "", label: "Overview", icon: LayoutGrid },
        ]
    },
    {
        title: "Infrastructure",
        items: [
            { href: "/database", label: "Database", icon: Database },
            { href: "/sql", label: "SQL Editor", icon: Terminal },
            { href: "/auth", label: "Authentication", icon: Shield },
            { href: "/storage", label: "Storage", icon: Folder },
            { href: "/edge-functions", label: "Edge Functions", icon: Code2 },
            { href: "/realtime", label: "Realtime", icon: Bell },
        ]
    },
    {
        title: "Management",
        items: [
            { href: "/secrets", label: "Secrets", icon: Key },
            { href: "/backups", label: "Backups", icon: Archive },
            { href: "/logs", label: "Logs", icon: FileText },
            { href: "/settings", label: "Settings", icon: Settings },
        ]
    }
];

export function ProjectSidebar() {
    const params = useParams();
    const pathname = usePathname();
    const projectId = params.id as string;
    const [isOpen, setIsOpen] = useState(false);
    const { currentOrg } = useOrg();

    const sidebarContent = (
        <>
            <div className="p-4 border-b border-border mb-4 flex items-center gap-2">
                <div className="w-8 h-8 rounded-md bg-primary flex items-center justify-center text-primary-foreground font-bold shadow-lg shadow-primary/20">
                    S
                </div>
                <div className="flex-1 min-w-0">
                    <h1 className="font-bold text-sm truncate">Supalove</h1>
                    <p className="text-[10px] text-muted-foreground font-mono truncate">{projectId}</p>
                </div>
                {/* Close button for mobile */}
                <button
                    onClick={() => setIsOpen(false)}
                    className="lg:hidden p-1 rounded-md hover:bg-muted"
                >
                    <X size={20} />
                </button>
            </div>

            <div className="px-3 mb-2">
                <Link
                    href={`/org/${currentOrg?.id}/projects`}
                    className="flex items-center gap-2 text-sm text-muted-foreground hover:text-foreground transition-colors px-3 py-2 rounded-lg hover:bg-muted"
                >
                    <LayoutGrid size={16} />
                    Back to Projects
                </Link>
            </div>

            <nav className="flex-1 px-3 space-y-6 overflow-y-auto">
                {sidebarSections.map((section) => (
                    <div key={section.title} className="space-y-1">
                        <h3 className="px-3 text-[10px] font-bold uppercase tracking-wider text-muted-foreground/60 mb-2">
                            {section.title}
                        </h3>
                        {section.items.map((item) => {
                            const href = `/projects/${projectId}${item.href}`;
                            const isActive = item.href === ""
                                ? pathname === `/projects/${projectId}`
                                : pathname?.startsWith(href);

                            return (
                                <Link
                                    key={item.href}
                                    href={href}
                                    onClick={() => setIsOpen(false)}
                                    className={cn(
                                        "flex items-center gap-3 px-3 py-2.5 text-sm rounded-lg transition-all group",
                                        isActive
                                            ? "bg-primary/10 text-primary font-medium shadow-sm"
                                            : "text-muted-foreground hover:bg-muted hover:text-foreground"
                                    )}
                                >
                                    <item.icon
                                        size={18}
                                        className={cn(
                                            "transition-colors flex-shrink-0",
                                            isActive ? "text-primary" : "text-muted-foreground group-hover:text-foreground"
                                        )}
                                    />
                                    <span className="truncate">{item.label}</span>
                                </Link>
                            );
                        })}
                    </div>
                ))}
            </nav>

            <div className="p-4 border-t border-border mt-auto">
                <Link
                    href={`/org/${currentOrg?.id}/projects`}
                    className="flex items-center gap-2 text-xs text-muted-foreground hover:text-foreground transition-colors"
                >
                    <LayoutGrid size={14} />
                    All Projects
                </Link>
            </div>
        </>
    );

    return (
        <>
            {/* Mobile Menu Button */}
            <button
                onClick={() => setIsOpen(true)}
                className="lg:hidden fixed top-3 left-3 z-50 p-2 rounded-lg bg-card border border-border shadow-lg"
            >
                <Menu size={20} />
            </button>

            {/* Mobile Overlay */}
            {isOpen && (
                <div
                    className="lg:hidden fixed inset-0 bg-black/50 backdrop-blur-sm z-40"
                    onClick={() => setIsOpen(false)}
                />
            )}

            {/* Sidebar - Desktop */}
            <aside className="hidden lg:flex w-64 border-r border-border bg-card/50 backdrop-blur-sm sticky top-0 h-screen flex-col">
                {sidebarContent}
            </aside>

            {/* Sidebar - Mobile Drawer */}
            <aside
                className={cn(
                    "lg:hidden fixed inset-y-0 left-0 z-50 w-72 bg-card border-r border-border flex flex-col transform transition-transform duration-300 ease-in-out",
                    isOpen ? "translate-x-0" : "-translate-x-full"
                )}
            >
                {sidebarContent}
            </aside>
        </>
    );
}
