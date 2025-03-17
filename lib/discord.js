import fetch from 'node-fetch';
import dotenv from 'dotenv';
dotenv.config();

export async function sendDiscordMessage(messageContent) {
    try {
        const response = await fetch(`https://discord.com/api/v10/channels/${process.env.DISCORD_CHANNEL_ID}/messages`, {
            body: JSON.stringify({ content: messageContent }),
            headers: {
                'Authorization': `Bot ${process.env.DISCORD_BOT_TOKEN}`,
                'Content-Type': 'application/json',
            },
            method: 'POST'
        });
        console.log(response);
    } catch (error) {
        console.error(error);
    }
}

// Example usage:
// sendDiscordMessage('1153237308267561021', 'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExb2c3cnJxMmNpNGJrZ2FzNWNhcnZranNrcWdzamZ2dHNkNjQ0b2VhMiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/nY403vHQUn9KSqT28a/giphy.gif');