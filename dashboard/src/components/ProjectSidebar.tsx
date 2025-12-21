"use client";

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
} from "lucide-react";
import { cn } from "@/lib/utils";

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

    return (
        <aside className="w-64 border-r border-border bg-card/50 backdrop-blur-sm sticky top-0 h-screen overflow-y-auto flex flex-col">
            <div className="p-4 border-b border-border mb-4 flex items-center gap-2">
                <div className="w-8 h-8 rounded-md bg-primary flex items-center justify-center text-primary-foreground font-bold shadow-lg shadow-primary/20">
                    S
                </div>
                <div>
                    <h1 className="font-bold text-sm truncate">Supalove</h1>
                    <p className="text-[10px] text-muted-foreground font-mono truncate">{projectId}</p>
                </div>
            </div>

            <nav className="flex-1 px-3 space-y-6">
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
                                    className={cn(
                                        "flex items-center gap-3 px-3 py-2 text-sm rounded-md transition-all group",
                                        isActive
                                            ? "bg-primary/10 text-primary font-medium shadow-sm"
                                            : "text-muted-foreground hover:bg-muted hover:text-foreground"
                                    )}
                                >
                                    <item.icon
                                        size={16}
                                        className={cn(
                                            "transition-colors",
                                            isActive ? "text-primary" : "text-muted-foreground group-hover:text-foreground"
                                        )}
                                    />
                                    {item.label}
                                </Link>
                            );
                        })}
                    </div>
                ))}
            </nav>

            <div className="p-4 border-t border-border mt-auto">
                <Link
                    href="/projects"
                    className="flex items-center gap-2 text-xs text-muted-foreground hover:text-foreground transition-colors"
                >
                    <LayoutGrid size={14} />
                    All Projects
                </Link>
            </div>
        </aside>
    );
}
