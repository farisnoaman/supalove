"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { ArrowLeft } from "lucide-react";
import { cn } from "@/lib/utils";

const sidebarItems = [
    {
        category: "Account Settings",
        items: [
            { name: "Preferences", href: "/settings/profile" },
            { name: "Access Tokens", href: "/settings/tokens" },
            { name: "Security", href: "/settings/security" },
        ],
    },
    {
        category: "Logs",
        items: [
            { name: "Audit Logs", href: "/settings/audit-logs" },
        ],
    },
];

export default function SettingsLayout({
    children,
}: {
    children: React.ReactNode;
}) {
    const pathname = usePathname();

    return (
        <div className="flex min-h-screen bg-background">
            {/* Sidebar */}
            <aside className="w-64 border-r border-border bg-card hidden md:block">
                <div className="p-4 h-14 flex items-center border-b border-border/40">
                    <Link
                        href="/projects"
                        className="flex items-center text-sm text-muted-foreground hover:text-foreground transition-colors"
                    >
                        <ArrowLeft className="mr-2 h-4 w-4" />
                        Back to dashboard
                    </Link>
                </div>

                <div className="py-6 px-3 space-y-6">
                    {sidebarItems.map((section) => (
                        <div key={section.category}>
                            <h4 className="px-3 mb-2 text-xs font-semibold text-muted-foreground uppercase tracking-wider">
                                {section.category}
                            </h4>
                            <div className="space-y-0.5">
                                {section.items.map((item) => {
                                    const isActive = pathname === item.href;
                                    return (
                                        <Link
                                            key={item.href}
                                            href={item.href}
                                            className={cn(
                                                "flex items-center px-3 py-2 text-sm font-medium rounded-md transition-colors",
                                                isActive
                                                    ? "bg-primary/10 text-primary"
                                                    : "text-muted-foreground hover:bg-muted hover:text-foreground"
                                            )}
                                        >
                                            {item.name}
                                        </Link>
                                    );
                                })}
                            </div>
                        </div>
                    ))}
                </div>
            </aside>

            {/* Main Content */}
            <div className="flex-1 flex flex-col min-w-0 overflow-hidden">
                {/* Mobile Header (optional, for responsive) */}
                <header className="md:hidden h-14 border-b border-border flex items-center px-4 bg-card">
                    <Link href="/projects" className="mr-4">
                        <ArrowLeft className="h-5 w-5" />
                    </Link>
                    <span className="font-semibold">Settings</span>
                </header>

                <main className="flex-1 overflow-y-auto p-4 md:p-8 lg:px-12 max-w-5xl">
                    {children}
                </main>
            </div>
        </div>
    );
}
