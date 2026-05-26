require('dotenv').config();

const { init } = require("@heyputer/puter.js/src/init.cjs");

async function main() {

    const puter = init({
        token: process.env.PUTER_TOKEN
    });

    const response = await puter.ai.chat(
        "Reply with: Qwen via Puter is operational."
    );

    console.log("\n=== RESPONSE ===\n");
    console.log(response);
}

main().catch(console.error);