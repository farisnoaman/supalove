import fs from "fs";
import path from "path";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import { notFound } from "next/navigation";

interface DocPageProps {
    params: Promise<{ slug: string }>;
}

export default async function DocPage({ params }: DocPageProps) {
    const { slug } = await params;
    const docsDir = path.join(process.cwd(), "..", "docs");

    // Find the file that matches the slug (case insensitive)
    const files = fs.readdirSync(docsDir);
    const fileName = files.find(f => f.replace(".md", "").toLowerCase() === slug.toLowerCase());

    if (!fileName) {
        return notFound();
    }

    const filePath = path.join(docsDir, fileName);
    const content = fs.readFileSync(filePath, "utf8");

    return (
        <article className="prose prose-emerald dark:prose-invert max-w-none prose-headings:font-bold prose-headings:tracking-tight prose-a:text-emerald-500 hover:prose-a:text-emerald-600 prose-img:rounded-xl prose-img:shadow-xl">
            <ReactMarkdown remarkPlugins={[remarkGfm]}>
                {content}
            </ReactMarkdown>
        </article>
    );
}
