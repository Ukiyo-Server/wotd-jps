const axios = require('axios');
const { JSDOM } = require('jsdom');
const fs = require('fs');
const path = require('path');

// Helper function to download a file given a URL and output path.
async function downloadFile(url, outputPath) {
  try {
    const response = await axios({
      url,
      method: 'GET',
      responseType: 'stream',
    });
    return new Promise((resolve, reject) => {
      const writer = fs.createWriteStream(outputPath);
      response.data.pipe(writer);
      writer.on('finish', () => {
        console.log(`Downloaded: ${outputPath}`);
        resolve();
      });
      writer.on('error', (err) => {
        console.error(`Error writing file ${outputPath}: ${err}`);
        reject(err);
      });
    });
  } catch (error) {
    console.error(`Error downloading ${url}: ${error}`);
    throw error;
  }
}

// Function to fetch and parse the data.
async function fetchData() {
  try {
    // Fetch the page.
    const response = await axios.get('https://www.japanesepod101.com/japanese-phrases/#word_page');
    const html = response.data;

    // Parse the HTML using jsdom.
    const dom = new JSDOM(html);
    const document = dom.window.document;

    // Locate the div element with the "data-wordday" attribute.
    const element = document.querySelector('div[data-wordday]');
    if (!element) {
      console.error('Element with data-wordday not found.');
      return null;
    }

    // Extract the encoded JSON string from the attribute.
    const encodedData = element.getAttribute('data-wordday');

    // Decode HTML entities using a temporary textarea element.
    const temp = document.createElement('textarea');
    temp.innerHTML = encodedData;
    const decodedData = temp.value;

    // Parse the decoded JSON string into an object.
    const jsonData = JSON.parse(decodedData);
    console.warn('Data fetched successfully.');
    return jsonData;
  } catch (error) {
    console.error('Error during fetching data:', error);
    return null;
  }
}

// Function to download files using the fetched data.
async function downloadFiles(jsonData) {
  try {
    if (!jsonData) {
      console.error('No data to download.');
      return;
    }

    // Download the main audio_target as "word-of-the-day.mp3".
    await downloadFile(jsonData.audio_target, path.join(__dirname, 'word-of-the-day.mp3'));

    // Download the main audio_english as "meaning.mp3".
    // await downloadFile(jsonData.audio_english, path.join(__dirname, 'meaning.mp3'));

    // Download the main image_url_512 as "image.jpg".
    // await downloadFile(jsonData.image_url_512, path.join(__dirname, 'image.jpg'));

    // Download each sample's audio_target as "1.mp3", "2.mp3", etc.
    // if (Array.isArray(jsonData.samples)) {
    //   for (let i = 0; i < jsonData.samples.length; i++) {
    //     const sample = jsonData.samples[i];
    //     const filename = `${i + 1}.mp3`;
    //     await downloadFile(sample.audio_target, path.join(__dirname, filename));
    //   }
    // } else {
    //   console.warn('No samples found in the data.');
    // }

    console.log('All downloads completed successfully.');
  } catch (error) {
    console.error('Error during downloading files:', error);
  }
}

// Main function to orchestrate fetching and downloading.
async function fetchAndDownload() {
  const jsonData = await fetchData();
  await downloadFiles(jsonData);
}

// Start the process.
// fetchAndDownload();
// fetchData().then(data => {
//   console.log(data);
// });

module.exports = { fetchData };