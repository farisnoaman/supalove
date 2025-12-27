"use client";

import { LayoutGrid, Database, HardDrive } from "lucide-react";
import { Progress } from "@/components/ui/progress";

function UsageCard({ title, icon: Icon, used, limit, unit }: any) {
    const isUnlimited = limit === -1;
    const percent = isUnlimited ? 0 : Math.min(100, Math.round((used / limit) * 100));

    return (
        <Card className="border border-border/40">
            <CardHeader className="pb-3">
                <CardTitle className="text-sm font-medium text-muted-foreground flex items-center gap-2">
                    <Icon size={16} />
                    {title}
                </CardTitle>
            </CardHeader>
            <CardContent>
                <div className="flex items-end justify-between mb-2">
                    <span className="text-2xl font-bold">{used}{unit}</span>
                    <span className="text-xs text-muted-foreground">
                        of {isUnlimited ? "Unlimited" : `${limit}${unit}`}
                    </span>
                </div>
                {!isUnlimited && <Progress value={percent} className="h-2" />}
            </CardContent>
        </Card>
    );
}
import { useEffect, useState } from "react";
import { useParams } from "next/navigation";
import {
    CreditCard, Check, Zap, Shield, Crown,
    Loader2, AlertCircle, ExternalLink
} from "lucide-react";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card";
import { toast, Toaster } from "sonner";
import { cn } from "@/lib/utils";

interface Subscription {
    status: string;
    plan: string;
    current_period_end: string | null;
}

export default function BillingPage() {
    const params = useParams();
    const orgId = params.orgId as string;

    const [sub, setSub] = useState<Subscription | null>(null);
    const [usage, setUsage] = useState<any>(null);
    const [loading, setLoading] = useState(true);
    const [processing, setProcessing] = useState(false);

    const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

    useEffect(() => {
        fetchSubscription();
    }, [orgId]);

    const fetchSubscription = async () => {
        try {
            const token = localStorage.getItem("token");
            const resp = await fetch(`${API_URL}/api/v1/billing/orgs/${orgId}/subscription`, {
                headers: { "Authorization": `Bearer ${token}` }
            });
            if (resp.ok) {
                setSub(await resp.json());
            }

            // Fetch usage
            const usageResp = await fetch(`${API_URL}/api/v1/billing/orgs/${orgId}/usage`, {
                headers: { "Authorization": `Bearer ${token}` }
            });
            if (usageResp.ok) {
                setUsage(await usageResp.json());
            }
        } catch (err) {
            console.error("Failed to fetch subscription", err);
        } finally {
            setLoading(false);
        }
    };

    const handleUpgrade = async (planId: string) => {
        setProcessing(true);
        try {
            const token = localStorage.getItem("token");
            const resp = await fetch(`${API_URL}/api/v1/billing/orgs/${orgId}/checkout`, {
                method: "POST",
                headers: {
                    "Authorization": `Bearer ${token}`,
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    plan_id: planId,
                    return_url: window.location.href
                })
            });

            if (resp.ok) {
                const data = await resp.json();
                if (data.mock) {
                    // DEV MODE: Call dev-upgrade endpoint to actually update the plan
                    const devResp = await fetch(`${API_URL}/api/v1/billing/orgs/${orgId}/dev-upgrade`, {
                        method: "POST",
                        headers: {
                            "Authorization": `Bearer ${token}`,
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify({
                            plan_id: planId === "price_pro_monthly" ? "pro" :
                                planId === "price_premium_monthly" ? "premium" : "free"
                        })
                    });

                    if (devResp.ok) {
                        toast.success("Plan upgraded successfully! (Dev Mode)");
                        setTimeout(() => window.location.reload(), 1000);
                    } else {
                        toast.error("Dev upgrade failed");
                    }
                } else {
                    window.location.href = data.url;
                }
            } else {
                toast.error("Failed to start checkout");
            }
        } catch (err) {
            toast.error("Network error");
        } finally {
            setProcessing(false);
        }
    };

    const manageSubscription = async () => {
        setProcessing(true);
        try {
            const token = localStorage.getItem("token");
            const resp = await fetch(`${API_URL}/api/v1/billing/orgs/${orgId}/portal`, {
                method: "POST",
                headers: {
                    "Authorization": `Bearer ${token}`,
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    return_url: window.location.href
                })
            });

            if (resp.ok) {
                const data = await resp.json();
                window.location.href = data.url;
            } else {
                toast.error("Failed to open billing portal");
            }
        } catch (err) {
            toast.error("Network error");
        } finally {
            setProcessing(false);
        }
    };

    if (loading) {
        return (
            <div className="flex items-center justify-center h-64">
                <Loader2 className="animate-spin" size={32} />
            </div>
        );
    }

    const isPlan = (planId: string) => {
        if (!sub) return planId === "free";
        return sub.plan === planId;
    };

    // Derived active plan for display
    const currentPlanId = sub?.plan || "free";

    return (
        <div className="space-y-8 p-8 animate-in fade-in slide-in-from-bottom-4 duration-700">
            <Toaster richColors position="top-right" />

            <div>
                <h1 className="text-3xl font-bold flex items-center gap-3">
                    Billing & Plans
                    {currentPlanId === "pro" && (
                        <Badge className="bg-gradient-to-r from-purple-500 to-pink-500 border-0">PRO</Badge>
                    )}
                    {currentPlanId === "premium" && (
                        <Badge className="bg-gradient-to-r from-amber-500 to-orange-500 border-0">PREMIUM</Badge>
                    )}
                </h1>
                <p className="text-muted-foreground mt-1">
                    Manage your organization's subscription and billing details
                </p>
            </div>

            {/* Current Plan Status */}
            <div className="p-6 bg-card border border-border/40 rounded-2xl flex items-center justify-between">
                <div>
                    <h3 className="font-bold text-lg">Current Subscription</h3>
                    <p className="text-sm text-muted-foreground mt-1">
                        You are currently on the <span className="font-bold text-foreground capitalize">{currentPlanId}</span> plan.
                    </p>
                    {sub?.current_period_end && (
                        <p className="text-xs text-muted-foreground mt-2">
                            Renews on {new Date(sub.current_period_end).toLocaleDateString()}
                        </p>
                    )}
                </div>
                {currentPlanId !== "free" && (
                    <Button onClick={manageSubscription} disabled={processing} variant="outline">
                        {processing ? <Loader2 className="animate-spin mr-2" size={16} /> : <CreditCard className="mr-2" size={16} />}
                        Manage Billing
                    </Button>
                )}
            </div>

            {/* Resource Usage */}
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                <UsageCard
                    title="Projects"
                    icon={LayoutGrid}
                    used={usage?.projects?.used || 0}
                    limit={usage?.projects?.limit || 2}
                    unit=""
                />
                <UsageCard
                    title="Database"
                    icon={Database}
                    used={usage?.db_size?.used_mb || 0}
                    limit={usage?.db_size?.limit_mb || 500}
                    unit="MB"
                />
                <UsageCard
                    title="Storage"
                    icon={HardDrive}
                    used={usage?.storage?.used_mb || 0}
                    limit={usage?.storage?.limit_mb || 1024}
                    unit="MB"
                />
            </div>

            {/* Plans Grid */}
            <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 xl:gap-8">
                {/* Free Plan */}
                <Card className={cn("relative border-2 flex flex-col", isPlan("free") ? "border-primary" : "border-border/40")}>
                    {isPlan("free") && (
                        <div className="absolute -top-3 left-1/2 -translate-x-1/2 bg-primary text-primary-foreground px-3 py-1 rounded-full text-xs font-bold">
                            Current Plan
                        </div>
                    )}
                    <CardHeader>
                        <CardTitle className="text-2xl">Free</CardTitle>
                        <CardDescription>Perfect for hobby projects</CardDescription>
                        <div className="mt-4">
                            <span className="text-4xl font-bold">$0</span>
                            <span className="text-muted-foreground">/month</span>
                        </div>
                    </CardHeader>
                    <CardContent className="space-y-3 flex-1">
                        <ul className="space-y-2 text-sm">
                            <li className="flex items-center gap-2"><Check size={16} className="text-green-500" /> 2 Projects</li>
                            <li className="flex items-center gap-2"><Check size={16} className="text-green-500" /> 500MB Database</li>
                            <li className="flex items-center gap-2"><Check size={16} className="text-green-500" /> 1GB Bandwidth</li>
                            <li className="flex items-center gap-2"><Check size={16} className="text-green-500" /> Community Support</li>
                        </ul>
                    </CardContent>
                    <CardFooter>
                        <Button className="w-full" variant="outline" disabled>
                            {isPlan("free") ? "Current Plan" : "Downgrade via Support"}
                        </Button>
                    </CardFooter>
                </Card>

                {/* Pro Plan */}
                <Card className={cn("relative border-2 flex flex-col", isPlan("pro") ? "border-purple-500" : "border-border/40")}>
                    {isPlan("pro") && (
                        <div className="absolute -top-3 left-1/2 -translate-x-1/2 bg-purple-500 text-white px-3 py-1 rounded-full text-xs font-bold">
                            Current Plan
                        </div>
                    )}
                    <CardHeader>
                        <CardTitle className="text-2xl flex items-center justify-between">
                            Pro
                            <Crown size={24} className="text-purple-500" />
                        </CardTitle>
                        <CardDescription>Power for scaling apps</CardDescription>
                        <div className="mt-4">
                            <span className="text-4xl font-bold">$25</span>
                            <span className="text-muted-foreground">/month</span>
                        </div>
                    </CardHeader>
                    <CardContent className="space-y-3 flex-1">
                        <ul className="space-y-2 text-sm">
                            <li className="flex items-center gap-2"><Check size={16} className="text-purple-500" /> 20 Projects</li>
                            <li className="flex items-center gap-2"><Check size={16} className="text-purple-500" /> 5GB Database</li>
                            <li className="flex items-center gap-2"><Check size={16} className="text-purple-500" /> 50GB Bandwidth</li>
                            <li className="flex items-center gap-2"><Check size={16} className="text-purple-500" /> Priority Support</li>
                            <li className="flex items-center gap-2"><Check size={16} className="text-purple-500" /> Daily Backups</li>
                        </ul>
                    </CardContent>
                    <CardFooter>
                        {isPlan("pro") ? (
                            <Button className="w-full bg-purple-500/10 text-purple-600 hover:bg-purple-500/20" variant="ghost" disabled>
                                Active Plan
                            </Button>
                        ) : (
                            <Button
                                className="w-full bg-gradient-to-r from-purple-600 to-pink-600 hover:opacity-90 transition-opacity"
                                onClick={() => handleUpgrade("price_pro_monthly")}
                                disabled={processing || isPlan("premium")} // Can't easily downgrade in UI
                            >
                                {processing ? <Loader2 className="animate-spin mr-2" size={16} /> : <Zap className="mr-2" size={16} />}
                                Upgrade to Pro
                            </Button>
                        )}
                    </CardFooter>
                </Card>

                {/* Premium Plan */}
                <Card className={cn("relative border-2 flex flex-col", isPlan("premium") ? "border-amber-500" : "border-border/40")}>
                    {isPlan("premium") && (
                        <div className="absolute -top-3 left-1/2 -translate-x-1/2 bg-amber-500 text-white px-3 py-1 rounded-full text-xs font-bold">
                            Current Plan
                        </div>
                    )}
                    <CardHeader>
                        <CardTitle className="text-2xl flex items-center justify-between">
                            Premium
                            <Shield size={24} className="text-amber-500" />
                        </CardTitle>
                        <CardDescription>Dedicated infrastructure</CardDescription>
                        <div className="mt-4">
                            <span className="text-4xl font-bold">$100</span>
                            <span className="text-muted-foreground">/month</span>
                        </div>
                    </CardHeader>
                    <CardContent className="space-y-3 flex-1">
                        <ul className="space-y-2 text-sm">
                            <li className="flex items-center gap-2"><Check size={16} className="text-amber-500" /> 100 Projects</li>
                            <li className="flex items-center gap-2"><Check size={16} className="text-amber-500" /> 20GB Database</li>
                            <li className="flex items-center gap-2"><Check size={16} className="text-amber-500" /> <strong>Dedicated Clusters</strong></li>
                            <li className="flex items-center gap-2"><Check size={16} className="text-amber-500" /> 24/7 Phone Support</li>
                            <li className="flex items-center gap-2"><Check size={16} className="text-amber-500" /> Custom SLAs</li>
                        </ul>
                    </CardContent>
                    <CardFooter>
                        {isPlan("premium") ? (
                            <Button className="w-full bg-amber-500/10 text-amber-600 hover:bg-amber-500/20" variant="ghost" disabled>
                                Active Plan
                            </Button>
                        ) : (
                            <Button
                                className="w-full bg-gradient-to-r from-amber-500 to-orange-600 hover:opacity-90 transition-opacity"
                                onClick={() => handleUpgrade("price_premium_monthly")}
                                disabled={processing}
                            >
                                {processing ? <Loader2 className="animate-spin mr-2" size={16} /> : <Shield className="mr-2" size={16} />}
                                Upgrade to Premium
                            </Button>
                        )}
                    </CardFooter>
                </Card>
            </div>
        </div>
    );
}
