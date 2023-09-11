# Word of the Day - JapanesePod101 Scraper

Fetch the Japanese word of the day from [JapanesePod101](https://www.japanesepod101.com/japanese-phrases), along with additional details and downloadable audio examples.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Logging](#logging)
- [Contribution](#contribution)
- [Disclaimer](#disclaimer)
- [License](#license)

## Features

- Extracts the word of the day from JapanesePod101.
- Retrieves additional details like the date, yomigana, romaji, word meaning, and part of speech.
- Downloads high-quality audio examples for the main word and additional examples.

## Prerequisites

- Python 3.x
- Required Python modules: `requests`, `beautifulsoup4`

## Installation

1. Clone the repository:
```bash
git clone [https://github.com/Ukiyo-Server/wotd-jps]
```

2. Navigate to the directory and install the required Python modules:
```bash
cd path_to_directory
pip install -r requirements.txt
```

## Usage

To use the script, navigate to the directory and run:

```bash
python main.py
```

This will extract the word of the day along with its details and download the associated audio files.

## Logging

The script logs its activities and any errors encountered during its execution. The logs can be found in the `wotd_jps.log` file in the main directory.

## Contribution

Contributions, issues, and feature requests are welcome. Feel free to check the [issues page](#) if you want to contribute.

## Disclaimer

This script is for educational purposes only. Ensure you have the right to access and scrape the website. Always respect `robots.txt` and terms of service of the website. The structure of the website might change over time, so the script might need updates.

## License

This project is [MIT](https://choosealicense.com/licenses/mit/) licensed.

---
