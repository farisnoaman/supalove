"use client"

import { ExternalLink, Database, Calendar } from "lucide-react"

interface Project {
  id: string
  name?: string
  status: string
  api_url?: string
  db_url?: string
  realtime_url?: string
  created_at: string
}

interface ProjectListProps {
  projects: Project[]
  onCreateProject?: () => void
}

export function ProjectList({ projects, onCreateProject }: ProjectListProps) {
  return (
    <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
      {projects.map((project) => (
        <div
          key={project.id}
          className="bg-card border rounded-lg p-6 hover:shadow-md transition-shadow"
        >
          <div className="flex justify-between items-start mb-4">
            <h3 className="font-semibold text-lg">
              {project.name || `project-${project.id.slice(0, 8)}`}
            </h3>
            <span
              className={`px-2 py-1 rounded-full text-xs font-medium ${
                project.status === "running"
                  ? "bg-green-100 text-green-700"
                  : project.status === "provisioning"
                  ? "bg-yellow-100 text-yellow-700"
                  : "bg-gray-100 text-gray-700"
              }`}
            >
              {project.status}
            </span>
          </div>

          <div className="space-y-2 text-sm text-muted-foreground mb-4">
            <div className="flex items-center gap-2">
              <Database className="h-4 w-4" />
              <span>{project.id.slice(0, 8)}</span>
            </div>
            <div className="flex items-center gap-2">
              <Calendar className="h-4 w-4" />
              <span>{new Date(project.created_at).toLocaleDateString()}</span>
            </div>
          </div>

          <div className="flex gap-2">
            <a
              href={`/projects/${project.id}`}
              className="flex-1 bg-primary text-primary-foreground px-3 py-2 rounded-md text-sm font-medium text-center hover:bg-primary/90 transition-colors"
            >
              Open
            </a>
            {project.api_url && (
              <a
                href={project.api_url}
                target="_blank"
                rel="noopener noreferrer"
                className="p-2 text-muted-foreground hover:text-foreground transition-colors"
                title="API URL"
              >
                <ExternalLink className="h-4 w-4" />
              </a>
            )}
          </div>
        </div>
      ))}
    </div>
  )
}