import Link from "next/link";
import { FileText, ChevronLeft } from "lucide-react";
import fs from "fs";
import path from "path";

export default function DocsLayout({
    children,
}: {
    children: React.ReactNode;
}) {
    // Read docs directory
    const docsDir = path.join(process.cwd(), "..", "docs");
    const files = fs.readdirSync(docsDir).filter(f => f.endsWith(".md"));

    const docItems = files.map(file => ({
        name: file.replace(".md", ""),
        slug: file.replace(".md", "").toLowerCase(),
        fileName: file
    }));

    return (
        <div className="flex h-screen bg-background overflow-hidden">
            {/* Docs Sidebar */}
            <aside className="w-72 border-r border-border bg-card/30 backdrop-blur-sm flex flex-col hidden lg:flex">
                <div className="p-6 border-b border-border">
                    <Link
                        href="/projects"
                        className="flex items-center gap-2 text-sm text-muted-foreground hover:text-foreground transition-colors mb-4 group"
                    >
                        <ChevronLeft size={16} className="group-hover:-translate-x-0.5 transition-transform" />
                        Back to Dashboard
                    </Link>
                    <h1 className="text-xl font-bold tracking-tight">Documentation</h1>
                    <p className="text-xs text-muted-foreground mt-1">Supalove Platforms Guide</p>
                </div>

                <nav className="flex-1 overflow-y-auto p-4 space-y-1">
                    {docItems.map((item) => (
                        <Link
                            key={item.slug}
                            href={`/docs/${item.slug}`}
                            className="flex items-center gap-3 px-3 py-2 rounded-lg text-sm text-muted-foreground hover:bg-muted hover:text-foreground transition-all group"
                        >
                            <FileText size={16} className="text-muted-foreground/60 group-hover:text-primary transition-colors" />
                            <span className="capitalize">{item.name.replace(/_/g, " ")}</span>
                        </Link>
                    ))}
                </nav>

                <div className="p-4 border-t border-border mt-auto">
                    <div className="bg-emerald-500/5 border border-emerald-500/10 rounded-lg p-3">
                        <p className="text-[10px] font-bold text-emerald-600 uppercase tracking-widest mb-1">Open Source</p>
                        <p className="text-xs text-muted-foreground">Self-host Supabase with ease and 100% compatibility.</p>
                    </div>
                </div>
            </aside>

            {/* Main Content */}
            <div className="flex-1 flex flex-col min-w-0 overflow-hidden relative">
                {/* Mobile Header (Simplified) */}
                <header className="lg:hidden h-14 border-b border-border bg-background/80 backdrop-blur-md flex items-center px-4 sticky top-0 z-20">
                    <Link href="/projects" className="p-2 -ml-2">
                        <ChevronLeft size={20} />
                    </Link>
                    <span className="font-semibold ml-2">Documentation</span>
                </header>

                <main className="flex-1 overflow-y-auto p-6 md:p-12 lg:p-16 subtle-gradient scroll-smooth">
                    <div className="max-w-4xl mx-auto">
                        {children}
                    </div>
                </main>
            </div>
        </div>
    );
}
