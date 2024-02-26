import requests
from bs4 import BeautifulSoup
import os
import logging

# Setting up logging
logging.basicConfig(
    filename="wotd_jps.log", level=logging.INFO, format="%(asctime)s - %(message)s"
)


def extract_data():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Referer": "https://www.google.com/",
        "Accept": "text/html",
        "Accept-Language": "en-US",
        "Accept-Encoding": "gzip",
    }

    url = "https://www.japanesepod101.com/japanese-phrases"
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Content extraction
        word = soup.select_one(
            "#wotd-widget > div.r101-wotd-widget__section--first > div.r101-wotd-widget__word-row > div.r101-wotd-widget__word"
        ).text.strip()
        audio_element = soup.select_one(
            "#wotd-widget > div.r101-wotd-widget__section--first > div.r101-wotd-widget__word-row > div.r101-wotd-widget__audio.r101-audio-player--a.js-audio-player"
        )
        audio_url = (
            audio_element["data-audio"]
            if audio_element and "data-audio" in audio_element.attrs
            else None
        )
        date = soup.select_one(
            "#wotd-widget > div.r101-wotd-widget__header > div > button.r101-wotd-widget__date-picker.js-wotd-widget-picker"
        ).text.strip()
        yomigana = soup.select_one(
            "#wotd-widget > div.r101-wotd-widget__section--first > div.r101-wotd-widget__additional-row > div.r101-wotd-widget__additional-field.kana"
        ).text.strip()
        romaji = soup.select_one(
            "#wotd-widget > div.r101-wotd-widget__section--first > div.r101-wotd-widget__additional-row > div.r101-wotd-widget__additional-field.romaji"
        ).text.strip()
        words_meaning = soup.select_one(
            "#wotd-widget > div.r101-wotd-widget__section--first > div.r101-wotd-widget__english"
        ).text.strip()
        part_of_speech = soup.select_one(
            "#wotd-widget > div.r101-wotd-widget__section--first > div.r101-wotd-widget__class"
        )
        part_of_speech = part_of_speech.text.strip() if part_of_speech else None
        example1 = soup.select_one(
            "#wotd-widget > div:nth-child(3) > div.r101-wotd-widget__word-row > div.r101-wotd-widget__word"
        ).text.strip()
        example1_yomigana = soup.select_one(
            "#wotd-widget > div:nth-child(3) > div.r101-wotd-widget__additional-field.kana"
        ).text.strip()
        example1_romaji = soup.select_one(
            "#wotd-widget > div:nth-child(3) > div.r101-wotd-widget__additional-field.romaji"
        ).text.strip()
        example1_meaning = soup.select_one(
            "#wotd-widget > div:nth-child(3) > div.r101-wotd-widget__english"
        ).text.strip()

        example2_elem = soup.select_one(
            "#wotd-widget > div:nth-child(4) > div.r101-wotd-widget__word-row > div.r101-wotd-widget__word"
        )
        example2 = example2_elem.text.strip() if example2_elem else None

        example2_yomigana_elem = soup.select_one(
            "#wotd-widget > div:nth-child(4) > div.r101-wotd-widget__additional-field.kana"
        )
        example2_yomigana = (
            example2_yomigana_elem.text.strip() if example2_yomigana_elem else None
        )
        example2_romaji_elem = soup.select_one(
            "#wotd-widget > div:nth-child(4) > div.r101-wotd-widget__additional-field.romaji"
        )
        example2_romaji = (
            example2_romaji_elem.text.strip() if example2_romaji_elem else None
        )
        example2_meaning_elem = soup.select_one(
            "#wotd-widget > div:nth-child(4) > div.r101-wotd-widget__english"
        )
        example2_meaning = (
            example2_meaning_elem.text.strip() if example2_meaning_elem else None
        )

        # Additional audio selectors
        example1_elem = soup.select_one(
            "#wotd-widget > div:nth-child(3) > div.r101-wotd-widget__word-row > div.r101-wotd-widget__audio.r101-audio-player--a.js-audio-player"
        )
        example1_mp3 = (
            example1_elem["data-audio"]
            if example1_elem and "data-audio" in example1_elem.attrs
            else None
        )

        example2_elem = soup.select_one(
            "#wotd-widget > div:nth-child(4) > div.r101-wotd-widget__word-row > div.r101-wotd-widget__audio.r101-audio-player--a.js-audio-player"
        )
        example2_mp3 = (
            example2_elem["data-audio"]
            if example2_elem and "data-audio" in example2_elem.attrs
            else None
        )

        return (
            word,
            audio_url,
            date,
            yomigana,
            romaji,
            words_meaning,
            part_of_speech,
            example1,
            example1_yomigana,
            example1_romaji,
            example1_meaning,
            example1_mp3,
            example2,
            example2_yomigana,
            example2_romaji,
            example2_meaning,
            example2_mp3,
        )

    except requests.Timeout:
        logging.error("The request timed out")
        print("The request timed out")
        return
    except requests.TooManyRedirects:
        logging.error("Too many redirects. The URL might be incorrect.")
        print("Too many redirects. The URL might be incorrect.")
        return
    except requests.RequestException as e:
        logging.error(f"Network error: {e}")
        print(f"Network error: {e}")
        return
    except Exception as e:
        logging.error(f"Error parsing the page: {e}")
        print(f"Error parsing the page: {e}")
        return


def download_word_audio(audio_url, filename):
    filepath = os.path.join(os.getcwd(), filename)

    try:
        response = requests.get(audio_url, stream=True, timeout=10)
        response.raise_for_status()

        with open(filepath, "wb") as audio_file:
            for chunk in response.iter_content(chunk_size=8192):
                audio_file.write(chunk)

        print(f"Audio saved as {filename}")
        return filepath
    except IOError as e:
        logging.error(
            f"IO error (disk issues, maybe out of space or permission denied): {e}"
        )
        print(f"IO error (disk issues, maybe out of space or permission denied): {e}")
        return None
    except requests.RequestException as e:
        logging.error(f"Network error while downloading audio: {e}")
        print(f"Network error while downloading audio: {e}")
        return None
    except Exception as e:
        logging.error(f"Error saving audio file: {e}")
        print(f"Error saving audio file: {e}")
        return None


def main_function():
    data = extract_data()
    if data:
        (
            word,
            main_audio,
            date,
            yomigana,
            romaji,
            words_meaning,
            part_of_speech,
            example1,
            example1_yomigana,
            example1_romaji,
            example1_meaning,
            example1_mp3,
            example2,
            example2_yomigana,
            example2_romaji,
            example2_meaning,
            example2_mp3,
        ) = data

        # Handling possible missing data
        output_data = {
            "word": word,
            "date": date,
            "yomigana": yomigana,
            "romaji": romaji,
            "words_meaning": words_meaning,
            "example1": example1,
            "example1_yomigana": example1_yomigana,
            "example1_romaji": example1_romaji,
            "example1_meaning": example1_meaning,
            "example2": example2,
            "example2_yomigana": example2_yomigana,
            "example2_romaji": example2_romaji,
            "example2_meaning": example2_meaning,
        }
        if part_of_speech:
            output_data["part_of_speech"] = part_of_speech

        print("Extracted Data:", output_data)

        # Download main audio
        download_word_audio(main_audio, "word_of_the_day.mp3")

        # Download example audios if available
        if example1_mp3:
            download_word_audio(example1_mp3, "example_1.mp3")
        if example2_mp3:
            download_word_audio(example2_mp3, "example_2.mp3")


main_function()
