import { ProjectSidebar } from "@/components/ProjectSidebar";
import { ProjectHeader } from "@/components/ProjectHeader";

export default function ProjectLayout({
    children,
}: {
    children: React.ReactNode;
}) {
    return (
        <div className="flex min-h-screen bg-background">
            <ProjectSidebar />
            <div className="flex-1 flex flex-col min-w-0">
                <ProjectHeader />
                <main className="flex-1 p-4 md:p-6 lg:p-8 subtle-gradient">
                    {children}
                </main>
            </div>
        </div>
    );
}
