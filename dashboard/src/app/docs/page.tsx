import { redirect } from "next/navigation";
import fs from "fs";
import path from "path";

export default function DocsPage() {
    const docsDir = path.join(process.cwd(), "..", "docs");
    let firstDoc = "";

    try {
        const files = fs.readdirSync(docsDir).filter(f => f.endsWith(".md"));
        if (files.length > 0) {
            firstDoc = files[0].replace(".md", "").toLowerCase();
        }
    } catch (e) {
        console.error("Failed to read docs directory", e);
    }

    if (firstDoc) {
        redirect(`/docs/${firstDoc}`);
    }

    return (
        <div className="flex items-center justify-center min-h-[50vh]">
            <div className="text-center">
                <h1 className="text-2xl font-bold">No documentation found</h1>
                <p className="text-muted-foreground mt-2">Please check the docs/ directory in the project root.</p>
            </div>
        </div>
    );
}
