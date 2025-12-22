"use client";

import { useEffect } from "react";
import { useRouter } from "next/navigation";
import { Loader2 } from "lucide-react";

export default function ProjectsRedirect() {
    const router = useRouter();

    useEffect(() => {
        router.replace("/org");
    }, [router]);

    return (
        <div className="flex h-screen items-center justify-center">
            <Loader2 className="animate-spin text-muted-foreground" />
        </div>
    );
}
