"use client";

import { useOrg } from "@/components/providers/org-provider";
import { useRouter } from "next/navigation";
import { useEffect } from "react";
import { Loader2 } from "lucide-react";

export default function OrgRedirect() {
    const { orgs, isLoading } = useOrg();
    const router = useRouter();

    useEffect(() => {
        if (!isLoading) {
            if (orgs.length > 0) {
                // Default to the first org's projects
                router.replace(`/org/${orgs[0].id}/projects`);
            } else {
                // No orgs, prompt to create one
                router.replace("/settings/organization");
            }
        }
    }, [orgs, isLoading, router]);


    return (
        <div className="flex h-screen items-center justify-center">
            <Loader2 className="animate-spin text-muted-foreground" />
        </div>
    );
}
