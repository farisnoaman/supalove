import { serve } from "https://deno.land/std@0.177.0/http/server.ts";

console.log("Live Functions Runtime v1.0.0");

serve(async (req) => {
    const url = new URL(req.url);

    // This is a placeholder router.
    // In a real implementation, this would look up the function code from the database
    // or file system based on the path, and dynamic import() it.

    if (url.pathname === "/health") {
        return new Response("OK", { status: 200 });
    }

    // Basic echo for testing
    if (url.pathname.startsWith("/echo")) {
        const body = await req.text();
        return new Response(`Echo: ${body}`, { status: 200 });
    }

    return new Response("Supalove Functions Routine. Deploy a function to see it here.", { status: 404 });
});
