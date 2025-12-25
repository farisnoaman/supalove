"use client";

import { usePathname } from "next/navigation";
import Link from "next/link";
import { LayoutGrid, Users, Settings, Plus, Menu, X, CreditCard } from "lucide-react";
import { cn } from "@/lib/utils";
import { OrgSwitcher } from "@/components/OrgSwitcher";
import { useOrg } from "@/components/providers/org-provider";
import { useState } from "react";
import { UserNav } from "./UserNav";

export function OrgSidebar() {
    const pathname = usePathname();
    const { currentOrg } = useOrg();
    const [isOpen, setIsOpen] = useState(false);

    if (!currentOrg) return null;

    const navItems = [
        {
            label: "Projects",
            icon: LayoutGrid,
            href: `/org/${currentOrg.id}/projects`,
            isActive: (path: string) => path.includes("/projects"),
        },
        {
            label: "Team",
            icon: Users,
            href: `/org/${currentOrg.id}/team`,
            isActive: (path: string) => path.includes("/team"),
        },
        {
            label: "Billing",
            icon: CreditCard,
            href: `/org/${currentOrg.id}/billing`,
            isActive: (path: string) => path.includes("/billing"),
        },
        {
            label: "Settings",
            icon: Settings,
            href: `/org/${currentOrg.id}/settings`,
            isActive: (path: string) => path.includes("/settings") && !path.includes("/team") && !path.includes("/projects") && !path.includes("/billing"),
        },
    ];

    const sidebarContent = (
        <div className="flex flex-col h-full bg-card/50 backdrop-blur-sm border-r border-border">
            <div className="p-4 border-b border-border">
                <OrgSwitcher className="w-full" />
            </div>

            <nav className="flex-1 p-4 space-y-2">
                {navItems.map((item) => {
                    const active = item.isActive(pathname || "");
                    return (
                        <Link
                            key={item.href}
                            href={item.href}
                            onClick={() => setIsOpen(false)}
                            className={cn(
                                "flex items-center gap-3 px-3 py-2 rounded-lg text-sm transition-colors",
                                active
                                    ? "bg-primary/10 text-primary font-medium"
                                    : "text-muted-foreground hover:bg-muted hover:text-foreground"
                            )}
                        >
                            <item.icon size={18} />
                            {item.label}
                        </Link>
                    )
                })}
            </nav>

            <div className="p-4 border-t border-border mt-auto">
                <Link href="/projects/new">
                    <button className="w-full bg-primary text-primary-foreground px-4 py-2 rounded-lg font-medium flex items-center justify-center gap-2 hover:opacity-90 transition-all shadow-sm">
                        <Plus size={16} />
                        New Project
                    </button>
                </Link>
            </div>
        </div>
    );

    return (
        <>
            {/* Mobile Header */}
            <header className="lg:hidden fixed top-0 left-0 right-0 h-14 bg-background/80 backdrop-blur-md border-b border-border z-40 flex items-center px-4 gap-4">
                <button
                    onClick={() => setIsOpen(true)}
                    className="p-2 -ml-2 rounded-md hover:bg-muted text-muted-foreground hover:text-foreground"
                >
                    <Menu size={20} />
                </button>
                <div className="font-semibold tracking-tight cursor-default select-none flex-1">
                    {currentOrg.name}
                </div>
                <UserNav />
            </header>

            {/* Mobile Overlay */}
            {isOpen && (
                <div
                    className="lg:hidden fixed inset-0 bg-black/50 backdrop-blur-sm z-40"
                    onClick={() => setIsOpen(false)}
                />
            )}

            {/* Desktop Sidebar */}
            <aside className="hidden lg:block w-64 h-screen sticky top-0">
                {sidebarContent}
            </aside>

            {/* Mobile Drawer */}
            <aside
                className={cn(
                    "lg:hidden fixed inset-y-0 left-0 z-50 w-72 bg-card border-r border-border shadow-2xl transform transition-transform duration-300 ease-in-out",
                    isOpen ? "translate-x-0" : "-translate-x-full"
                )}
            >
                {sidebarContent}
                <button
                    onClick={() => setIsOpen(false)}
                    className="absolute top-2 right-2 p-2 hover:bg-muted rounded-md"
                >
                    <X size={20} />
                </button>
            </aside>
        </>
    );
}
