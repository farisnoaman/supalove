"use client";

import Link from "next/link";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Github, ArrowLeft } from "lucide-react";
import { useState } from "react";
import { toast } from "sonner";
import { Toaster } from "sonner";

export default function LoginPage() {
    const [loading, setLoading] = useState(false);

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setLoading(true);
        // Simulate auth delay
        await new Promise(resolve => setTimeout(resolve, 1500));
        setLoading(false);
        toast.success("Welcome back! Redirecting...");
        setTimeout(() => window.location.href = "/projects", 1000);
    };

    return (
        <div className="min-h-screen grid lg:grid-cols-2">
            <Toaster richColors position="top-right" />

            {/* Left: Form */}
            <div className="flex flex-col justify-center p-8 md:p-12 lg:p-16 relative">
                <Link href="/" className="absolute top-8 left-8 text-muted-foreground hover:text-foreground flex items-center gap-2 text-sm font-medium transition-colors">
                    <ArrowLeft size={16} />
                    Back to Home
                </Link>

                <div className="max-w-md w-full mx-auto space-y-8">
                    <div className="space-y-2 text-center lg:text-left">
                        <h1 className="text-3xl font-bold tracking-tight">Welcome back</h1>
                        <p className="text-muted-foreground">Enter your credentials to access your account.</p>
                    </div>

                    <div className="space-y-4">
                        <Button variant="outline" className="w-full h-11 gap-2 border-border/50 hover:bg-muted/50" type="button">
                            <Github size={18} />
                            Continue with GitHub
                        </Button>

                        <div className="relative">
                            <div className="absolute inset-0 flex items-center">
                                <span className="w-full border-t border-border/50" />
                            </div>
                            <div className="relative flex justify-center text-xs uppercase">
                                <span className="bg-background px-2 text-muted-foreground">Or continue with email</span>
                            </div>
                        </div>

                        <form onSubmit={handleSubmit} className="space-y-4">
                            <div className="space-y-2">
                                <Label htmlFor="email">Email</Label>
                                <Input id="email" type="email" placeholder="name@example.com" required className="h-11" />
                            </div>
                            <div className="space-y-2">
                                <div className="flex items-center justify-between">
                                    <Label htmlFor="password">Password</Label>
                                    <Link href="#" className="text-xs text-primary hover:underline">Forgot password?</Link>
                                </div>
                                <Input id="password" type="password" required className="h-11" />
                            </div>
                            <Button type="submit" className="w-full h-11 primary-gradient shadow-lg shadow-emerald-500/20" disabled={loading}>
                                {loading ? "Signing in..." : "Sign In"}
                            </Button>
                        </form>
                    </div>

                    <p className="text-center text-sm text-muted-foreground">
                        Don't have an account?{" "}
                        <Link href="/signup" className="font-semibold text-primary hover:underline">
                            Sign up
                        </Link>
                    </p>
                </div>
            </div>

            {/* Right: Visual */}
            <div className="hidden lg:flex flex-col justify-center bg-muted/30 border-l border-border/40 p-12 relative overflow-hidden">
                <div className="absolute top-0 right-0 w-[600px] h-[600px] bg-emerald-500/10 rounded-full blur-[120px] -translate-y-1/2 translate-x-1/2" />

                <div className="relative z-10 max-w-lg mx-auto text-center space-y-6">
                    <div className="w-20 h-20 rounded-2xl bg-gradient-to-br from-emerald-500 to-emerald-700 flex items-center justify-center mx-auto shadow-2xl shadow-emerald-500/30">
                        <span className="text-white text-4xl font-bold">S</span>
                    </div>
                    <h2 className="text-2xl font-bold">Manage your projects with ease</h2>
                    <p className="text-muted-foreground text-lg leading-relaxed">
                        Supalove provides you with all the tools you need to build, scale, and manage your backend infrastructure.
                    </p>
                </div>
            </div>
        </div>
    );
}
