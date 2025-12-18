import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Supalove | Self-hosted Supabase Clone",
  description: "Control Plane for managing your Supabase instances",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={`${inter.className} bg-background text-foreground`}>
        <div className="flex h-screen overflow-hidden">
          {/* Sidebar */}
          <aside className="w-64 border-r bg-card flex flex-col">
            <div className="p-6 border-b">
              <h1 className="text-xl font-extrabold tracking-tight text-primary">Supalove</h1>
            </div>
            <nav className="flex-1 p-4 space-y-2">
              <a href="/" className="block p-2 rounded hover:bg-muted font-medium">Projects</a>
              <a href="/settings" className="block p-2 rounded hover:bg-muted font-medium text-muted-foreground opacity-50 cursor-not-allowed">Settings</a>
            </nav>
            <div className="p-4 border-t text-xs text-muted-foreground">
              v0.1.0-alpha
            </div>
          </aside>

          {/* Main Content */}
          <main className="flex-1 overflow-y-auto bg-slate-50/50 p-8">
            {children}
          </main>
        </div>
      </body>
    </html>
  );
}
