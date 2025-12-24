"use client";

import { OrgSidebar } from "@/components/OrgSidebar";
import { useOrg } from "@/components/providers/org-provider";
import { useParams, useRouter } from "next/navigation";
import { useEffect, useState } from "react";
import { Loader2, Settings, FlaskConical, LogOut, Sun, Moon, Laptop, Check } from "lucide-react";
import { useTheme } from "next-themes";
import Link from "next/link";
import {
    DropdownMenu,
    DropdownMenuContent,
    DropdownMenuItem,
    DropdownMenuLabel,
    DropdownMenuSeparator,
    DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";

export default function OrgLayout({
    children,
}: {
    children: React.ReactNode;
}) {
    const { currentOrg, switchOrg, isLoading } = useOrg();
    const params = useParams();
    const router = useRouter();
    const orgId = params.orgId as string;
    const { setTheme, theme } = useTheme();
    const [email, setEmail] = useState("");

    useEffect(() => {
        if (!isLoading) {
            if (currentOrg && currentOrg.id !== orgId) {
                switchOrg(orgId);
            }
        }

        // Get email from token
        const token = localStorage.getItem("token");
        if (token) {
            try {
                const payload = JSON.parse(atob(token.split('.')[1]));
                setEmail(payload.email || payload.sub || "user@supalove.com");
            } catch (e) {
                console.error("Failed to parse token", e);
            }
        }
    }, [orgId, currentOrg, isLoading, switchOrg]);

    if (isLoading) {
        return (
            <div className="flex h-screen items-center justify-center">
                <Loader2 className="animate-spin text-muted-foreground" />
            </div>
        );
    }

    const handleLogout = () => {
        localStorage.removeItem('token');
        window.location.href = '/';
    };

    return (
        <div className="flex min-h-screen bg-background">
            <OrgSidebar />
            <div className="flex-1 flex flex-col min-w-0">
                <header className="hidden lg:flex h-14 border-b border-border bg-card/30 backdrop-blur-sm items-center px-4 md:px-8 sticky top-0 z-10 justify-end">
                    <div className="flex items-center gap-4">
                        <DropdownMenu>
                            <DropdownMenuTrigger asChild>
                                <div
                                    className="w-8 h-8 rounded-full bg-emerald-100 flex items-center justify-center text-emerald-700 text-xs font-bold ring-2 ring-emerald-500/20 hover:ring-emerald-500/50 transition-all cursor-pointer select-none"
                                    title="Account"
                                >
                                    {email ? email[0].toUpperCase() : "U"}
                                </div>
                            </DropdownMenuTrigger>
                            <DropdownMenuContent className="w-64" align="end" forceMount>
                                <DropdownMenuLabel className="font-normal">
                                    <div className="flex flex-col space-y-1">
                                        <p className="text-sm font-medium leading-none truncate">{email}</p>
                                    </div>
                                </DropdownMenuLabel>
                                <DropdownMenuSeparator />
                                <DropdownMenuItem asChild>
                                    <Link href="/settings/profile" className="w-full cursor-pointer">
                                        <Settings className="mr-2 h-4 w-4" />
                                        <span>Account preferences</span>
                                    </Link>
                                </DropdownMenuItem>
                                <DropdownMenuItem>
                                    <FlaskConical className="mr-2 h-4 w-4" />
                                    <span>Feature previews</span>
                                </DropdownMenuItem>
                                <DropdownMenuSeparator />
                                <DropdownMenuLabel>Theme</DropdownMenuLabel>
                                <DropdownMenuItem onClick={() => setTheme("dark")}>
                                    <Moon className="mr-2 h-4 w-4" />
                                    <span>Dark</span>
                                    {theme === "dark" && <Check className="ml-auto h-4 w-4" />}
                                </DropdownMenuItem>
                                <DropdownMenuItem onClick={() => setTheme("light")}>
                                    <Sun className="mr-2 h-4 w-4" />
                                    <span>Light</span>
                                    {theme === "light" && <Check className="ml-auto h-4 w-4" />}
                                </DropdownMenuItem>
                                <DropdownMenuItem onClick={() => setTheme("system")}>
                                    <Laptop className="mr-2 h-4 w-4" />
                                    <span>System</span>
                                    {theme === "system" && <Check className="ml-auto h-4 w-4" />}
                                </DropdownMenuItem>
                                <DropdownMenuSeparator />
                                <DropdownMenuItem onClick={handleLogout} className="text-red-600 focus:text-red-600 focus:bg-red-50">
                                    <LogOut className="mr-2 h-4 w-4" />
                                    <span>Log out</span>
                                </DropdownMenuItem>
                            </DropdownMenuContent>
                        </DropdownMenu>
                    </div>
                </header>
                <main className="flex-1 overflow-y-auto subtle-gradient pt-14 lg:pt-0">
                    {children}
                </main>
            </div>
        </div>
    );
}
