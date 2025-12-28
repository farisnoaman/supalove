"use client";

import { useState } from "react";
import { ArrowLeft, Rocket, Loader2, Sparkles, Server } from "lucide-react";

export default function NewProjectPage() {
    const [projectId, setProjectId] = useState("");
    const [plan, setPlan] = useState<"shared" | "dedicated">("shared");
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);
    const [success, setSuccess] = useState(false);
    const [resultData, setResultData] = useState<any>(null);

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setLoading(true);
        setError(null);
        setSuccess(false);
        const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

        try {
            const token = localStorage.getItem("token");
            if (!token) throw new Error("Not authenticated");

            const resp = await fetch(`${API_URL}/api/v1/projects`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${token}`
                },
                body: JSON.stringify({ name: projectId, plan }),
            });

            if (!resp.ok) {
                const errData = await resp.json();
                throw new Error(errData.detail || "Failed to create project");
            }

            const data = await resp.json();
            setResultData(data);
            setSuccess(true);
        } catch (err: any) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="max-w-2xl mx-auto space-y-8">
            <button
                onClick={() => window.location.href = "/"}
                className="text-muted-foreground hover:text-foreground flex items-center gap-2 transition-colors"
            >
                <ArrowLeft size={16} />
                Back to projects
            </button>

            <div className="bg-card border rounded-xl p-8 shadow-sm">
                <h2 className="text-2xl font-bold mb-6">Create a New Project</h2>

                {!success ? (
                    <form onSubmit={handleSubmit} className="space-y-6">
                        {/* Plan Selection */}
                        <div>
                            <label className="block text-sm font-medium mb-3 text-muted-foreground">
                                Select Plan
                            </label>
                            <div className="grid grid-cols-2 gap-4">
                                {/* Shared Plan */}
                                <button
                                    type="button"
                                    onClick={() => setPlan("shared")}
                                    className={`relative p-4 rounded-xl border-2 text-left transition-all ${plan === "shared"
                                        ? "border-primary bg-primary/5 shadow-md"
                                        : "border-muted hover:border-muted-foreground/30"
                                        }`}
                                >
                                    <div className="flex items-center gap-2 mb-2">
                                        <div className={`p-2 rounded-lg ${plan === "shared" ? "bg-primary/10 text-primary" : "bg-muted"}`}>
                                            <Sparkles size={18} />
                                        </div>
                                        <span className="font-bold">Shared</span>
                                        <span className="text-xs bg-green-100 text-green-700 px-2 py-0.5 rounded-full">Free</span>
                                    </div>
                                    <p className="text-xs text-muted-foreground">
                                        Shared infrastructure. Perfect for development and small projects.
                                    </p>
                                    {plan === "shared" && (
                                        <div className="absolute top-2 right-2 w-3 h-3 bg-primary rounded-full" />
                                    )}
                                </button>

                                {/* Dedicated Plan */}
                                <button
                                    type="button"
                                    onClick={() => setPlan("dedicated")}
                                    className={`relative p-4 rounded-xl border-2 text-left transition-all ${plan === "dedicated"
                                        ? "border-primary bg-primary/5 shadow-md"
                                        : "border-muted hover:border-muted-foreground/30"
                                        }`}
                                >
                                    <div className="flex items-center gap-2 mb-2">
                                        <div className={`p-2 rounded-lg ${plan === "dedicated" ? "bg-primary/10 text-primary" : "bg-muted"}`}>
                                            <Server size={18} />
                                        </div>
                                        <span className="font-bold">Dedicated</span>
                                        <span className="text-xs bg-purple-100 text-purple-700 px-2 py-0.5 rounded-full">Premium</span>
                                    </div>
                                    <p className="text-xs text-muted-foreground">
                                        Isolated Docker stack. Best for production workloads.
                                    </p>
                                    {plan === "dedicated" && (
                                        <div className="absolute top-2 right-2 w-3 h-3 bg-primary rounded-full" />
                                    )}
                                </button>
                            </div>
                        </div>

                        {/* Project Name */}
                        <div>
                            <label htmlFor="projectId" className="block text-sm font-medium mb-2 text-muted-foreground">
                                Project Name
                            </label>
                            <input
                                id="projectId"
                                type="text"
                                required
                                placeholder="e.g. Food App"
                                className="w-full p-3 bg-muted border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary/50 transition-all font-sans"
                                value={projectId}
                                onChange={(e) => setProjectId(e.target.value)}
                            />
                            <p className="mt-2 text-xs text-muted-foreground">
                                This is just a display name. You can use spaces, capital letters, and emojis.
                            </p>
                        </div>

                        {error && (
                            <div className="bg-red-50 border border-red-200 text-red-600 p-3 rounded-lg text-sm">
                                {error}
                            </div>
                        )}

                        <button
                            type="submit"
                            disabled={loading || !projectId}
                            className="w-full bg-primary text-white py-3 rounded-lg font-bold flex items-center justify-center gap-3 disabled:opacity-50 disabled:cursor-not-allowed hover:opacity-90 transition-all shadow-md active:scale-[0.98]"
                        >
                            {loading ? (
                                <>
                                    <Loader2 className="animate-spin" size={20} />
                                    {plan === "shared" ? "Creating Database..." : "Provisioning Infrastructure..."}
                                </>
                            ) : (
                                <>
                                    <Rocket size={20} />
                                    Create {plan === "shared" ? "Shared" : "Dedicated"} Project
                                </>
                            )}
                        </button>
                    </form>
                ) : (
                    <div className="space-y-6 animate-in fade-in slide-in-from-bottom-4 duration-500">
                        <div className="bg-green-50 border border-green-200 text-green-700 p-4 rounded-lg flex items-center gap-3">
                            <div className="bg-green-100 p-2 rounded-full">✅</div>
                            <div>
                                <h4 className="font-bold">Project Provisioned Successfully!</h4>
                                <p className="text-sm opacity-90">
                                    Your new {resultData?.plan === "shared" ? "shared" : "dedicated"} Supabase instance is ready.
                                </p>
                            </div>
                        </div>

                        <div className="space-y-4">
                            <h5 className="font-semibold text-muted-foreground uppercase text-xs tracking-wider">Credentials & Endpoints</h5>
                            <div className="grid gap-3">
                                {resultData?.plan && (
                                    <div className="p-4 bg-muted border rounded-lg">
                                        <div className="text-xs text-muted-foreground mb-1">Plan</div>
                                        <div className="font-mono text-sm capitalize">{resultData?.plan}</div>
                                    </div>
                                )}
                                <div className="p-4 bg-muted border rounded-lg">
                                    <div className="text-xs text-muted-foreground mb-1">API URL</div>
                                    <div className="font-mono text-sm break-all">{resultData?.api_url}</div>
                                </div>
                                <div className="p-4 bg-muted border rounded-lg">
                                    <div className="text-xs text-muted-foreground mb-1">Database URL (Postgres)</div>
                                    <div className="font-mono text-sm break-all">{resultData?.db_url}</div>
                                </div>
                                {resultData?.realtime_url && (
                                    <div className="p-4 bg-muted border rounded-lg">
                                        <div className="text-xs text-muted-foreground mb-1">Realtime (WS)</div>
                                        <div className="font-mono text-sm break-all">{resultData?.realtime_url}</div>
                                    </div>
                                )}
                            </div>
                        </div>

                        <div className="flex flex-col sm:flex-row gap-3">
                            <button
                                onClick={() => window.location.href = `/projects/${resultData.id}`}
                                className="flex-1 py-3 bg-primary text-white rounded-lg font-bold hover:opacity-90 transition-all shadow-md active:scale-[0.98]"
                            >
                                Go to Dashboard
                            </button>
                            <button
                                onClick={() => window.location.href = `/org/${resultData.org_id}/projects`}
                                className="flex-1 py-3 border rounded-lg font-medium hover:bg-muted transition-colors"
                            >
                                Return to Project List
                            </button>
                        </div>
                    </div>
                )}
            </div>
        </div >
    );
}

