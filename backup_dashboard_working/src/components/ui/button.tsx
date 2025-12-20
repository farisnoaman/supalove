import * as React from "react"
import { cn } from "@/lib/utils"

export interface ButtonProps
    extends React.ButtonHTMLAttributes<HTMLButtonElement> {
    variant?: "default" | "secondary" | "ghost" | "danger" | "outline"
    size?: "default" | "sm" | "lg" | "icon"
}

const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
    ({ className, variant = "default", size = "default", ...props }, ref) => {
        const variantStyles = {
            default: "bg-primary text-white hover:opacity-90",
            secondary: "bg-muted text-foreground hover:bg-slate-200",
            ghost: "hover:bg-muted hover:text-foreground",
            danger: "bg-red-600 text-white hover:bg-red-700",
            outline: "border border-input hover:bg-muted",
        }

        const sizeStyles = {
            default: "h-10 px-4 py-2",
            sm: "h-8 px-3 text-sm",
            lg: "h-12 px-8",
            icon: "h-10 w-10",
        }

        return (
            <button
                className={cn(
                    "inline-flex items-center justify-center rounded-md font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-primary disabled:opacity-50 disabled:pointer-events-none",
                    variantStyles[variant],
                    sizeStyles[size],
                    className
                )}
                ref={ref}
                {...props}
            />
        )
    }
)
Button.displayName = "Button"

export { Button }
