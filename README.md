# @idleboy/wotd-jps

Fetch the Japanese word of the day from [JapanesePod101](https://www.japanesepod101.com/japanese-phrases), along with additional details and downloadable audio examples.

## Installation

To install, run:

```sh
npm i @idleboy/wotd-jps
```

## Usage

To fetch the Japanese word of the day and download associated files, you can use the provided functions.

### Fetching the Word of the Day

You can fetch the word of the day using the `getWotd` function:

```js
const { getWotd } = require('./lib/wotd');

getWotd().then(data => {
  console.log(data);
});
```

You'll get something similar to this:

```json
{
  date: '2025-03-17',
  dictionary_id: '135414',
  flashcard_id: '2320483',
  text: '感染',
  audio_target: 'https://d1pra95f92lrn3.cloudfront.net/audio/226725.mp3',
  audio_english: 'https://d1pra95f92lrn3.cloudfront.net/audio/87946.mp3',
  image_url: 'https://d1pra95f92lrn3.cloudfront.net/media/thumb/9457_fit288.jpg',
  image_url_512: 'https://d1pra95f92lrn3.cloudfront.net/media/thumb/9457_fit512.jpg',
  english: 'infection',
  meaning: 'the pathological state resulting from the invasion of the body by pathogenic microorganisms',
  class: 'noun',
  distracting_words: [ 'graveyard', 'diarrhea', 'cough' ],
  is_add_wordbank: false,
  kana: 'かんせん',
  romanization: 'kansen',
  samples: [
    {
      audio_target: 'https://d1pra95f92lrn3.cloudfront.net/audio/226726.mp3',
      audio_english: 'https://d1pra95f92lrn3.cloudfront.net/audio/86003.mp3',
      text: '彼女が抗生物質を飲み始めたら、感染部位は良くなった。',
      english: 'The infection improved when she started taking an antibiotic.',
      kana: 'かのじょがこうせいぶっしつをのみはじめたら、かんせんぶいはよくなった。',
      romanization: 'Kanojo ga kōsei busshitsu o nomi hajimetara, kansen bui wa yoku natta.'
    },
    {
      audio_target: 'https://d1pra95f92lrn3.cloudfront.net/audio/226728.mp3',
      audio_english: 'https://d1pra95f92lrn3.cloudfront.net/audio/86005.mp3',
      text: '皮膚感染',
      english: 'skin infection',
      kana: 'ひふかんせん',
      romanization: 'hifu kansen'
    },
    {
      audio_target: 'https://d1pra95f92lrn3.cloudfront.net/audio/226727.mp3',
      audio_english: 'https://d1pra95f92lrn3.cloudfront.net/audio/86004.mp3',
      text: '重度の感染',
      english: 'severe infection',
      kana: 'じゅうどのかんせん',
      romanization: 'jūdo no kansen'
    }
  ]
}
```

### Fetching and Downloading Files

To fetch the word of the day and download the associated files, use the `getWotdAndDownload` function:

```js
const { getWotdAndDownload } = require('./lib/wotd');

getWotdAndDownload();
```

## License

This project is licensed under the Attribution-ShareAlike 4.0 International License. See the [LICENSE](LICENSE) file for details.
