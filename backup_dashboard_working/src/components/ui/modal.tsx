"use client";

import * as React from "react"
import { cn } from "@/lib/utils"
import { X } from "lucide-react"

interface ModalProps {
    open: boolean
    onOpenChange: (open: boolean) => void
    children: React.ReactNode
}

interface ModalContentProps {
    children: React.ReactNode
    className?: string
}

interface ModalHeaderProps {
    children: React.ReactNode
    className?: string
}

interface ModalTitleProps {
    children: React.ReactNode
    className?: string
}

interface ModalFooterProps {
    children: React.ReactNode
    className?: string
}

export function Modal({ open, onOpenChange, children }: ModalProps) {
    if (!open) return null

    return (
        <div className="fixed inset-0 z-50 flex items-center justify-center">
            {/* Backdrop */}
            <div
                className="fixed inset-0 bg-black/50 backdrop-blur-sm"
                onClick={() => onOpenChange(false)}
            />
            {/* Modal */}
            <div className="relative z-50">{children}</div>
        </div>
    )
}

export function ModalContent({ children, className }: ModalContentProps) {
    return (
        <div
            className={cn(
                "relative bg-background border rounded-lg shadow-lg p-6 w-full max-w-lg max-h-[90vh] overflow-y-auto",
                className
            )}
        >
            {children}
        </div>
    )
}

export function ModalHeader({ children, className }: ModalHeaderProps) {
    return (
        <div className={cn("flex flex-col space-y-1.5 mb-4", className)}>
            {children}
        </div>
    )
}

export function ModalTitle({ children, className }: ModalTitleProps) {
    return (
        <h2 className={cn("text-lg font-semibold", className)}>
            {children}
        </h2>
    )
}

export function ModalFooter({ children, className }: ModalFooterProps) {
    return (
        <div className={cn("flex justify-end gap-2 mt-6", className)}>
            {children}
        </div>
    )
}

export function ModalClose({ onClose }: { onClose: () => void }) {
    return (
        <button
            onClick={onClose}
            className="absolute right-4 top-4 rounded-sm opacity-70 hover:opacity-100 transition-opacity"
        >
            <X size={16} />
        </button>
    )
}
