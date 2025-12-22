"use client";

import { Check, ChevronsUpDown, Building2, Plus } from "lucide-react";
import { cn } from "@/lib/utils";
import { Button } from "@/components/ui/button";
import {
    Command,
    CommandEmpty,
    CommandGroup,
    CommandInput,
    CommandItem,
    CommandList,
    CommandSeparator,
} from "@/components/ui/command";
import {
    Popover,
    PopoverContent,
    PopoverTrigger,
} from "@/components/ui/popover";
import { useOrg } from "@/components/providers/org-provider";
import { useState } from "react";
import { useRouter } from "next/navigation";

export function OrgSwitcher({ className }: { className?: string }) {
    const { orgs, currentOrg, switchOrg } = useOrg();
    const [open, setOpen] = useState(false);
    const router = useRouter();

    if (!currentOrg) {
        return (
            <Button
                variant="outline"
                role="combobox"
                className={cn("w-[200px] justify-between", className)}
                onClick={() => router.push("/settings/organization")}
            >
                <div className="flex items-center gap-2 text-muted-foreground">
                    <Building2 className="mr-2 h-4 w-4" />
                    Create Organization...
                </div>
            </Button>
        )
    }

    return (
        <Popover open={open} onOpenChange={setOpen}>
            <PopoverTrigger asChild>
                <Button
                    variant="outline"
                    role="combobox"
                    aria-expanded={open}
                    className={cn("w-[200px] justify-between", className)}
                >
                    <div className="flex items-center gap-2 truncate">
                        <div className="p-1 bg-primary/10 rounded flex items-center justify-center">
                            <Building2 className="h-4 w-4 text-primary" />
                        </div>
                        <span className="truncate max-w-[120px]">{currentOrg.name}</span>
                    </div>
                    <ChevronsUpDown className="ml-2 h-4 w-4 shrink-0 opacity-50" />
                </Button>
            </PopoverTrigger>
            <PopoverContent className="w-[200px] p-0">
                <Command>
                    <CommandInput placeholder="Search organization..." />
                    <CommandList>
                        <CommandEmpty>No organization found.</CommandEmpty>
                        <CommandGroup heading="Organizations">
                            {orgs.map((org) => (
                                <CommandItem
                                    key={org.id}
                                    onSelect={() => {
                                        switchOrg(org.id);
                                        setOpen(false);
                                    }}
                                    className="text-sm"
                                >
                                    <Check
                                        className={cn(
                                            "mr-2 h-4 w-4",
                                            currentOrg.id === org.id ? "opacity-100" : "opacity-0"
                                        )}
                                    />
                                    {org.name}
                                </CommandItem>
                            ))}
                        </CommandGroup>
                        <CommandSeparator />
                        <CommandGroup>
                            <CommandItem
                                onSelect={() => {
                                    router.push("/settings/organization"); // Or a modal
                                    setOpen(false);
                                }}
                                className="cursor-pointer text-primary"
                            >
                                <Plus className="mr-2 h-4 w-4" />
                                Create Organization
                            </CommandItem>
                        </CommandGroup>
                    </CommandList>
                </Command>
            </PopoverContent>
        </Popover>
    );
}
