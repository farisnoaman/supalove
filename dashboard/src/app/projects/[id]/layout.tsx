import { ProjectSidebar } from "@/components/ProjectSidebar";

export default function ProjectLayout({
    children,
}: {
    children: React.ReactNode;
}) {
    return (
        <div className="flex min-h-screen bg-background">
            <ProjectSidebar />
            <div className="flex-1 flex flex-col">
                <header className="h-14 border-b border-border bg-card/30 backdrop-blur-sm flex items-center px-8 sticky top-0 z-10">
                    {/* Placeholder for Breadcrumbs or search */}
                    <div className="flex-1" />
                    <div className="flex items-center gap-4">
                        <div className="w-8 h-8 rounded-full bg-emerald-100 flex items-center justify-center text-emerald-700 text-xs font-bold ring-2 ring-emerald-500/20">
                            F
                        </div>
                    </div>
                </header>
                <main className="flex-1 p-8 subtle-gradient">
                    {children}
                </main>
            </div>
        </div>
    );
}
