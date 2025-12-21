"use client";

import Link from "next/link";
import { Button } from "@/components/ui/button";
import { ArrowRight, Database, Shield, Zap, CheckCircle2, ChevronRight, Github } from "lucide-react";
import Image from "next/image";

export default function LandingPage() {
  return (
    <div className="min-h-screen flex flex-col bg-background">
      {/* Header */}
      <header className="sticky top-0 z-50 w-full border-b border-border/40 bg-background/80 backdrop-blur-md">
        <div className="container mx-auto px-4 h-16 flex items-center justify-between">
          <div className="flex items-center gap-2 font-bold text-xl tracking-tight">
            <div className="w-8 h-8 rounded-lg bg-emerald-500 flex items-center justify-center text-white shadow-lg shadow-emerald-500/30">
              S
            </div>
            <span>Supalove</span>
          </div>

          <nav className="hidden md:flex items-center gap-8 text-sm font-medium text-muted-foreground">
            <a href="#features" className="hover:text-foreground transition-colors">Features</a>
            <a href="#pricing" className="hover:text-foreground transition-colors">Pricing</a>
            <a href="#docs" className="hover:text-foreground transition-colors">Documentation</a>
          </nav>

          <div className="flex items-center gap-4">
            <Link href="/login">
              <Button variant="ghost" className="text-muted-foreground hover:text-foreground">
                Log in
              </Button>
            </Link>
            <Link href="/signup">
              <Button className="bg-emerald-600 hover:bg-emerald-700 text-white shadow-lg shadow-emerald-500/20">
                Sign up
              </Button>
            </Link>
          </div>
        </div>
      </header>

      <main className="flex-1">
        {/* Hero Section */}
        <section className="relative pt-20 pb-32 overflow-hidden">
          <div className="absolute top-0 left-1/2 -translate-x-1/2 w-full h-full max-w-7xl pointer-events-none">
            <div className="absolute top-20 left-20 w-72 h-72 bg-emerald-500/10 rounded-full blur-[100px]" />
            <div className="absolute bottom-20 right-20 w-96 h-96 bg-blue-500/10 rounded-full blur-[100px]" />
          </div>

          <div className="container mx-auto px-4 relative z-10 text-center">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/10 text-emerald-600 text-xs font-bold uppercase tracking-wider mb-8 border border-emerald-500/20">
              <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse" />
              v1.0 Public Beta is Live
            </div>

            <h1 className="text-5xl md:text-7xl font-black tracking-tighter mb-6 bg-clip-text text-transparent bg-gradient-to-r from-foreground via-foreground/90 to-muted-foreground max-w-4xl mx-auto leading-[1.1]">
              The Open Source <br className="hidden md:block" />
              Backend Platform
            </h1>

            <p className="text-xl text-muted-foreground max-w-2xl mx-auto mb-10 leading-relaxed">
              Supalove gives you a dedicated Postgres database, Authentication, instant APIs, and Realtime subscriptions.
            </p>

            <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
              <Link href="/signup">
                <Button size="lg" className="h-12 px-8 text-base bg-emerald-600 hover:bg-emerald-700 text-white shadow-xl shadow-emerald-500/25 rounded-full w-full sm:w-auto">
                  Start your project
                  <ChevronRight className="ml-2 w-4 h-4" />
                </Button>
              </Link>
              <Link href="/docs">
                <Button size="lg" variant="outline" className="h-12 px-8 text-base border-border/50 bg-card/50 backdrop-blur-sm hover:bg-muted/50 rounded-full w-full sm:w-auto">
                  <Github className="mr-2 w-4 h-4" />
                  Star on GitHub
                </Button>
              </Link>
            </div>

            {/* Visual Preview */}
            <div className="mt-20 relative max-w-5xl mx-auto">
              <div className="absolute -inset-1 bg-gradient-to-r from-emerald-500 to-blue-600 rounded-2xl blur opacity-20" />
              <div className="relative rounded-xl border border-border/40 bg-card/50 backdrop-blur-xl shadow-2xl overflow-hidden aspect-video flex items-center justify-center group">
                <div className="absolute inset-0 bg-grid-white/[0.02] [mask-image:linear-gradient(0deg,transparent,black)]" />
                <div className="text-center p-8">
                  <div className="w-16 h-16 rounded-2xl bg-gradient-to-br from-emerald-500 to-emerald-700 flex items-center justify-center mx-auto mb-6 shadow-xl shadow-emerald-500/30 group-hover:scale-110 transition-transform duration-500">
                    <Database className="text-white w-8 h-8" />
                  </div>
                  <h3 className="text-2xl font-bold mb-2">Supalove Dashboard</h3>
                  <p className="text-muted-foreground">Interactive preview coming soon</p>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* Features Grid */}
        <section id="features" className="py-24 bg-muted/30 border-y border-border/40">
          <div className="container mx-auto px-4">
            <div className="text-center max-w-2xl mx-auto mb-16">
              <h2 className="text-3xl font-bold tracking-tight mb-4">Everything you need to build</h2>
              <p className="text-muted-foreground">
                Stop worrying about infrastructure. Focus on shipping features with our comprehensive suite of backend tools.
              </p>
            </div>

            <div className="grid md:grid-cols-3 gap-8">
              {[
                {
                  icon: Database,
                  title: "Postgres Database",
                  desc: "Every project is a full Postgres database. Trusted, relentless, and robust.",
                  color: "text-emerald-500 bg-emerald-500/10"
                },
                {
                  icon: Shield,
                  title: "Authentication",
                  desc: "Add user sign ups and logins. Secure your data with Row Level Security.",
                  color: "text-blue-500 bg-blue-500/10"
                },
                {
                  icon: Zap,
                  title: "Instant APIs",
                  desc: "We introspect your database to provide instant REST and Realtime APIs.",
                  color: "text-amber-500 bg-amber-500/10"
                }
              ].map((feature, i) => (
                <div key={i} className="p-8 rounded-2xl bg-card border border-border/50 hover:border-primary/20 hover:shadow-lg transition-all">
                  <div className={`w-12 h-12 rounded-lg flex items-center justify-center mb-6 ${feature.color}`}>
                    <feature.icon size={24} />
                  </div>
                  <h3 className="text-xl font-bold mb-3">{feature.title}</h3>
                  <p className="text-muted-foreground leading-relaxed">
                    {feature.desc}
                  </p>
                </div>
              ))}
            </div>
          </div>
        </section>
      </main>

      <footer className="py-12 border-t border-border/40 bg-card/30">
        <div className="container mx-auto px-4 flex flex-col md:flex-row justify-between items-center gap-6">
          <div className="flex items-center gap-2 font-bold text-lg opacity-80">
            <div className="w-6 h-6 rounded bg-emerald-500 flex items-center justify-center text-white text-xs">
              S
            </div>
            <span>Supalove</span>
          </div>
          <p className="text-sm text-muted-foreground">
            © 2025 Supalove Inc. All rights reserved.
          </p>
          <div className="flex gap-6">
            <a href="#" className="text-muted-foreground hover:text-foreground">Twitter</a>
            <a href="#" className="text-muted-foreground hover:text-foreground">GitHub</a>
            <a href="#" className="text-muted-foreground hover:text-foreground">Discord</a>
          </div>
        </div>
      </footer>
    </div>
  );
}
