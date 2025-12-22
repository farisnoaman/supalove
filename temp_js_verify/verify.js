
const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');
const path = require('path');

async function main() {
    console.log("Starting verification...");

    let config;
    try {
        const configPath = path.resolve(__dirname, '../scripts/test_config.json');
        console.log("Reading config from:", configPath);
        const configRaw = fs.readFileSync(configPath, 'utf8');
        config = JSON.parse(configRaw);
    } catch (e) {
        console.error("Could not read config. Please run 'python3 scripts/get_test_config.py > scripts/test_config.json' first.");
        console.error(e.message);
        process.exit(1);
    }

    // Config has:
    // api_url (PostgREST)
    // auth_url (GoTrue)

    console.log("Targeting APIs:");
    console.log("  REST (PostgREST):", config.api_url);
    console.log("  AUTH (GoTrue):   ", config.auth_url);

    // Standard Supabase Client Initialization
    // We use the REST URL as the "Supabase URL" base, hoping it works for DB at least.
    const supabase = createClient(config.api_url, config.anon_key);

    console.log("\n--- TEST 1: Database Connection ---");
    // PostgREST is expected to be at /rest/v1/ by the client.
    // Our PostgREST is at /
    try {
        // We try to query a system table or just a non-existent one to check connectivity
        // 'pg_catalog' queries aren't usually allowed over PostgREST standard
        // checking a simple select.
        const { data, error } = await supabase.from('anything').select('*').limit(1);

        if (error) {
            console.log("Result: ERROR");
            console.log("Message:", error.message);
            console.log("Hint: If error is 404, it means path mapping is wrong.");
        } else {
            console.log("Result: SUCCESS (Data retrieved)");
        }
    } catch (e) {
        console.log("Result: EXCEPTION");
        console.log(e.message);
    }

    console.log("\n--- TEST 2: Auth Connection (Real Request) ---");
    try {
        // Attempt to sign in (random creds, just checking if endpoint is reached)
        const { data, error } = await supabase.auth.signInWithPassword({
            email: 'test@example.com',
            password: 'password123'
        });

        if (error) {
            console.log("Result: ERROR");
            console.log("Message:", error.message);
            console.log("Status:", error.status); // HTTP Status
        } else {
            console.log("Result: SUCCESS");
        }
    } catch (e) {
        console.log("Result: EXCEPTION");
        console.log(e.message);
    }

    console.log("\n--- ANALYSIS ---");
    console.log("If tests failed with 404 text or similar, it confirms that a Gateway is needed");
    console.log("to route /rest/v1 -> PostgREST and /auth/v1 -> GoTrue.");
}

main();
