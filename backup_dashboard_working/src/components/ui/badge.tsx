import * as React from "react"
import { cn } from "@/lib/utils"

export interface BadgeProps extends React.HTMLAttributes<HTMLDivElement> {
    variant?: "default" | "success" | "warning" | "danger" | "secondary"
}

const Badge = React.forwardRef<HTMLDivElement, BadgeProps>(
    ({ className, variant = "default", ...props }, ref) => {
        const variantStyles = {
            default: "bg-primary/10 text-primary border-primary/20",
            success: "bg-green-100 text-green-700 border-green-200",
            warning: "bg-yellow-100 text-yellow-700 border-yellow-200",
            danger: "bg-red-100 text-red-700 border-red-200",
            secondary: "bg-muted text-muted-foreground border-border",
        }

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
