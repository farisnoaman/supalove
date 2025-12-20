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
    FileText
} from "lucide-react";
import { cn } from "@/lib/utils";

const navItems = [
    { href: "", label: "Overview", icon: LayoutGrid },
    { href: "/database", label: "Database", icon: Database },
    { href: "/users", label: "Users", icon: Users },
    { href: "/storage", label: "Storage", icon: Folder },
    { href: "/edge-functions", label: "Edge functions", icon: Code2 },
    { href: "/ai", label: "AI", icon: Cpu },
    { href: "/secrets", label: "Secrets", icon: Key },
    { href: "/logs", label: "Logs", icon: FileText },
];

export function ProjectSidebar() {
    const params = useParams();
    const pathname = usePathname();
    const projectId = params.id as string;

    return (
        <aside className="w-56 border-r border-border bg-background min-h-screen p-4">
            <nav className="space-y-1">
                {navItems.map((item) => {
                    const href = `/projects/${projectId}${item.href}`;
                    const isActive = item.href === ""
                        ? pathname === `/projects/${projectId}`
                        : pathname?.startsWith(href);

                    return (
                        <Link
                            key={item.href}
                            href={href}
                            className={cn(
                                "flex items-center gap-3 px-3 py-2 text-sm rounded-md transition-colors",
                                isActive
                                    ? "bg-muted text-foreground font-medium"
                                    : "text-muted-foreground hover:bg-muted hover:text-foreground"
                            )}
                        >
                            <item.icon size={16} />
                            {item.label}
                        </Link>
                    );
                })}
            </nav>
        </aside>
    );
}
