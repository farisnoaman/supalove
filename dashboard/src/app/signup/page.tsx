"use client";

import Link from "next/link";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Github, ArrowLeft, Check } from "lucide-react";
import { useState } from "react";
import { toast } from "sonner";
import { Toaster } from "sonner";

export default function SignupPage() {
    const [loading, setLoading] = useState(false);

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setLoading(true);

        const full_name = (document.getElementById("name") as HTMLInputElement).value;
        const email = (document.getElementById("email") as HTMLInputElement).value;
        const password = (document.getElementById("password") as HTMLInputElement).value;

        try {
            const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";
            const res = await fetch(`${API_URL}/api/v1/auth/register`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ email, password, full_name }),
            });

            if (!res.ok) {
                const data = await res.json();
                throw new Error(data.detail || "Signup failed");
            }

            const data = await res.json();
            localStorage.setItem("token", data.access_token);
            toast.success("Account created! Redirecting...");
            setTimeout(() => window.location.href = "/projects", 1000);
        } catch (err: any) {
            toast.error(err.message);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="min-h-screen grid lg:grid-cols-2">
            <Toaster richColors position="top-right" />

            {/* Left: Visual */}
            <div className="hidden lg:flex flex-col justify-center bg-muted/30 border-r border-border/40 p-12 relative overflow-hidden">
                <div className="absolute bottom-0 left-0 w-[600px] h-[600px] bg-blue-500/10 rounded-full blur-[120px] translate-y-1/2 -translate-x-1/3" />

                <div className="relative z-10 max-w-lg mx-auto space-y-8">
                    <div>
                        <h2 className="text-2xl font-bold mb-6">Built for developers</h2>
                        <ul className="space-y-4">
                            {[
                                "Unlimited API requests",
                                "5GB Database storage included",
                                "Real-time subscriptions",
                                "Auto-generated documentation"
                            ].map((item, i) => (
                                <li key={i} className="flex items-center gap-3 text-muted-foreground">
                                    <div className="w-6 h-6 rounded-full bg-emerald-500/20 text-emerald-600 flex items-center justify-center flex-shrink-0">
                                        <Check size={14} />
                                    </div>
                                    {item}
                                </li>
                            ))}
                        </ul>
                    </div>
                </div>
            </div>

            {/* Right: Form */}
            <div className="flex flex-col justify-center p-8 md:p-12 lg:p-16 relative">
                <Link href="/" className="absolute top-8 right-8 text-muted-foreground hover:text-foreground flex items-center gap-2 text-sm font-medium transition-colors">
                    Back to Home
                    <ArrowLeft size={16} className="rotate-180" />
                </Link>

                <div className="max-w-md w-full mx-auto space-y-8">
                    <div className="space-y-2">
                        <h1 className="text-3xl font-bold tracking-tight">Create an account</h1>
                        <p className="text-muted-foreground">Start building your backend in seconds.</p>
                    </div>

                    <div className="space-y-4">
                        <Button variant="outline" className="w-full h-11 gap-2 border-border/50 hover:bg-muted/50" type="button">
                            <Github size={18} />
                            Sign up with GitHub
                        </Button>

                        <div className="relative">
                            <div className="absolute inset-0 flex items-center">
                                <span className="w-full border-t border-border/50" />
                            </div>
                            <div className="relative flex justify-center text-xs uppercase">
                                <span className="bg-background px-2 text-muted-foreground">Or sign up with email</span>
                            </div>
                        </div>

                        <form onSubmit={handleSubmit} className="space-y-4">
                            <div className="space-y-2">
                                <Label htmlFor="name">Full Name</Label>
                                <Input id="name" placeholder="John Doe" required className="h-11" />
                            </div>
                            <div className="space-y-2">
                                <Label htmlFor="email">Email</Label>
                                <Input id="email" type="email" placeholder="name@example.com" required className="h-11" />
                            </div>
                            <div className="space-y-2">
                                <Label htmlFor="password">Password</Label>
                                <Input id="password" type="password" required className="h-11" />
                                <p className="text-[10px] text-muted-foreground">
                                    Must be at least 8 characters long.
                                </p>
                            </div>
                            <Button type="submit" className="w-full h-11 primary-gradient shadow-lg shadow-emerald-500/20" disabled={loading}>
                                {loading ? "Creating account..." : "Sign Up"}
                            </Button>
                        </form>
                    </div>

                    <p className="text-center text-sm text-muted-foreground">
                        Already have an account?{" "}
                        <Link href="/login" className="font-semibold text-primary hover:underline">
                            Log in
                        </Link>
                    </p>
                </div>
            </div>
        </div>
    );
}
