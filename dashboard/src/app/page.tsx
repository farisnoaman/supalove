"use client";

import { useEffect, useState } from "react";
import { Plus, RefreshCcw, ExternalLink, AlertCircle } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Alert, AlertDescription } from "@/components/ui/alert";

interface Project {
  id: string;
  name: string;
  status: string;
  api_url?: string;
  db_url?: string;
  realtime_url?: string;
  created_at: string;
}

export default function ProjectsPage() {
  const [projects, setProjects] = useState<Project[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [retryCount, setRetryCount] = useState(0);

  const fetchProjects = async () => {
    const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";
    setLoading(true);
    setError(null);

    try {
      // Add timeout to prevent hanging requests
      const controller = new AbortController();
      const timeoutId = setTimeout(() => controller.abort(), 10000); // 10 second timeout

      const response = await fetch(`${API_URL}/api/v1/projects`, {
        signal: controller.signal,
        headers: {
          'Content-Type': 'application/json',
        },
      });

      clearTimeout(timeoutId);

      if (!response.ok) {
        throw new Error(`HTTP ${response.status}: ${response.statusText}`);
      }

      const data = await response.json();
      setProjects(Array.isArray(data) ? data : []);
    } catch (err: any) {
      if (err.name === 'AbortError') {
        setError('Request timeout - API may not be running');
      } else {
        setError(`Failed to load projects: ${err.message}`);
      }
      console.error('Projects fetch error:', err);
    } finally {
      setLoading(false);
    }
  };

  // Prevent infinite re-renders with proper dependency management
  useEffect(() => {
    let isMounted = true;

    const loadProjects = async () => {
      if (!isMounted) return;
      await fetchProjects();
    };

    loadProjects();

    return () => {
      isMounted = false;
    };
  }, []); // Empty dependency array - only run once on mount

  const handleRetry = () => {
    setRetryCount(prev => prev + 1);
    fetchProjects();
  };

  return (
    <div className="space-y-8">
      <div className="flex justify-between items-center">
        <div>
          <h2 className="text-3xl font-bold tracking-tight">Projects</h2>
          <p className="text-muted-foreground">Manage your Supabase instances.</p>
        </div>
        <button
          onClick={() => window.location.href = "/projects/new"}
          className="bg-primary text-white px-4 py-2 rounded-md font-medium flex items-center gap-2 hover:opacity-90 transition-opacity"
        >
          <Plus size={18} />
          New Project
        </button>
      </div>

      {loading ? (
        <div className="flex justify-center p-12">
          <RefreshCcw className="animate-spin text-muted-foreground" />
        </div>
      ) : error ? (
        <Alert variant="destructive">
          <AlertCircle className="h-4 w-4" />
          <AlertDescription className="flex items-center justify-between">
            <span>{error}</span>
            <Button
              variant="outline"
              size="sm"
              onClick={handleRetry}
              className="ml-4"
            >
              <RefreshCcw className="h-4 w-4 mr-2" />
              Retry
            </Button>
          </AlertDescription>
        </Alert>
      ) : projects.length === 0 ? (
        <div className="bg-card border rounded-lg p-12 text-center space-y-4">
          <div className="text-muted-foreground">No projects found.</div>
          <button
            onClick={() => window.location.href = "/projects/new"}
            className="text-primary font-medium hover:underline"
          >
            Create your first project
          </button>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {projects.map((project) => (
            <div key={project.id} className="bg-card border rounded-lg p-6 hover:shadow-md transition-shadow">
              <div className="flex justify-between items-start mb-4">
                <h3 className="font-semibold text-lg">{project.name || `project-${project.id.slice(0, 8)}`}</h3>
                <span className={`px-2 py-0.5 rounded text-xs font-medium ${project.status === "active" ? "bg-green-100 text-green-700" : "bg-yellow-100 text-yellow-700"
                  }`}>
                  {project.status}
                </span>
              </div>

              <div className="space-y-3 text-sm">
                <div className="flex justify-between">
                  <span className="text-muted-foreground">ID:</span>
                  <span className="font-mono text-xs">{project.id.slice(0, 8)}...</span>
                </div>
                {project.api_url && (
                  <div className="flex justify-between">
                    <span className="text-muted-foreground">API:</span>
                    <a href={project.api_url} target="_blank" className="text-primary hover:underline flex items-center gap-1">
                      Link <ExternalLink size={12} />
                    </a>
                  </div>
                )}
              </div>

              <div className="mt-6 flex gap-2">
                <button
                  onClick={() => window.location.href = `/projects/${project.id}`}
                  className="flex-1 text-center bg-muted py-2 rounded text-sm font-medium hover:bg-slate-200 transition-colors"
                >
                  Manage
                </button>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
