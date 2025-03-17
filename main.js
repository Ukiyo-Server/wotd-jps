const { fetchData } = require('./lib/wotd.js');
const { sendDiscordMessage } = require('./lib/discord.js');

async function main() {
    // Fetch the data
    const data = await fetchData();
    if (!data) {
        console.error('Failed to fetch data.');
        return;
    }

    // Format the content
    let messageContent = `<@&937579201551290419> - ${data.date}\n# ${data.text}\n${data.english} (*${data.class}*)\n-# ||${data.kana}, ${data.romanization}||\n## Examples:`;
    data.samples.forEach((sample) => {
        messageContent += `\n- ${sample.text}\n-# ||${sample.kana}||\n-# ||${sample.romanization}||\n${sample.english}\n`;
    });

    // Send the message to the Discord channel
    await sendDiscordMessage(messageContent);
    // console.log(messageContent);
}

// Start the process
main();