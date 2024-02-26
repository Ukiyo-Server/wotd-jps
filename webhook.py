# this is a script to send webhook to discord
import requests
import json
import logging
from wotd.main import extract_data, download_word_audio

# Load configuration from config.json
with open("config.json", "r") as file:
    config = json.load(file)

    webhook_url = config["webhook_url"]
    error_webhook_url = config["error_webhook_url"]

# Setup logging
logging.basicConfig(
    filename="discord_webhook.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
)


def send_to_discord(data, *audio_files):
    global webhook_url  # This ensures we're using the global variable
    content = (
        f"> New <@&937579201551290419>! for {data['date']}\n"
        "\n"
        f"> # **Word:** {data['word']}\n"
        f"> **Yomigana:** {data['yomigana']}\n"
        f"> **Romaji:** {data['romaji']}\n"
        f"> **Meaning:** {data['words_meaning']}\n"
        f"> **Part of the speech:** {data['part_of_speech']}\n"
        "\n"
        f"> ## Example 1:\n"
        f"> <a:Arrow:939136140622069791> {data['example1']}\n"
        f"> **Yomigana:** {data['example1_yomigana']}\n"
        f"> **Romaji:** {data['example1_romaji']}\n"
        f"> **Meaning:** {data['example1_meaning']}\n"
    )

    if data["example2"] is not None:
        content += (
            "\n"
            f"> ## Example 2:\n"
            f"> <a:Arrow:939136140622069791> {data['example2']}\n"
            f"> **Yomigana:** {data['example2_yomigana']}\n"
            f"> **Romaji:** {data['example2_romaji']}\n"
            f"> **Meaning:** {data['example2_meaning']}\n"
        )

    files = [(f.split("/")[-1], open(f, "rb")) for f in audio_files if f]

    response = requests.post(
        webhook_url,
        data={"content": content},
        files={f"file{i+1}": file for i, file in enumerate(files)},
    )

    # Close the file objects
    for _, file_obj in files:
        file_obj.close()

    if response.status_code != 204:
        logging.error(f"Failed to send data to Discord: {response.text}")
        print(f"Failed to send data to Discord: {response.text}")


if __name__ == "__main__":
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
        audio_paths = []

        audio_main_path = download_word_audio(main_audio, "word_of_the_day.mp3")
        if audio_main_path:
            audio_paths.append(audio_main_path)

        if example1_mp3:
            audio_example1_path = download_word_audio(example1_mp3, "example_1.mp3")
            if audio_example1_path:
                audio_paths.append(audio_example1_path)

        if example2_mp3:
            audio_example2_path = download_word_audio(example2_mp3, "example_2.mp3")
            if audio_example2_path:
                audio_paths.append(audio_example2_path)

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

        send_to_discord(output_data, *audio_paths)
