import * as React from "react"
import { cn } from "@/lib/utils"

export interface BadgeProps extends React.HTMLAttributes<HTMLDivElement> {
    variant?: "default" | "success" | "warning" | "danger" | "secondary" | "outline"
}

const Badge = React.forwardRef<HTMLDivElement, BadgeProps>(
    ({ className, variant = "default", ...props }, ref) => {
        const variantStyles = {
            default: "bg-primary/10 text-primary border-primary/20",
            success: "bg-emerald-500/10 text-emerald-600 border-emerald-500/20",
            warning: "bg-amber-500/10 text-amber-600 border-amber-500/20",
            danger: "bg-destructive/10 text-destructive border-destructive/20",
            secondary: "bg-muted text-muted-foreground border-border",
            outline: "bg-background text-foreground border-border",
        } as const

        return (
            <div
                ref={ref}
                className={cn(
                    "inline-flex items-center rounded-full border px-2.5 py-0.5 text-xs font-semibold transition-colors",
                    variantStyles[variant],
                    className
                )}
                {...props}
            />
        )
    }
)
Badge.displayName = "Badge"

export { Badge }
