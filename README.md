
# YouTube Transcript Summarizer

## Overview
This Python script fetches the transcript of a YouTube video, saves it to a file, and then uses OpenAI's GPT-3.5-turbo model to generate a summary of the transcript.

## Features
- Fetch transcripts from YouTube videos
- Save transcripts to a local file
- Generate summaries using OpenAI's GPT-3.5-turbo model

## Prerequisites
- Python 3.6+
- OpenAI API key
- YouTube Data API credentials (not required for transcript fetching, but may be needed for other YouTube API functionalities)

## Installation
1. Clone this repository:
   ```
   git clone https://github.com/yourusername/youtube-transcript-summarizer.git
   cd youtube-transcript-summarizer
   ```

2. Install the required packages:
   ```
   pip install openai youtube-transcript-api
   ```

3. Set up your OpenAI API key:
   - Create a `.env` file in the project root
   - Add your API key: `OPENAI_API_KEY=your-api-key-here`

## Usage
1. Open the script in a text editor.

2. Replace the empty string in `video_id = ''` with the YouTube video ID you want to summarize.
   The video ID is the part of the YouTube URL after `v=`. For example, in `https://www.youtube.com/watch?v=dQw4w9WgXcQ`, the video ID is `dQw4w9WgXcQ`.

3. Replace the empty string in `os.environ['OPENAI_API_KEY'] = ''` with your actual OpenAI API key.

4. Run the script:
   ```
   python youtube_transcript_summarizer.py
   ```

5. The script will output the summary of the video transcript to the console.

## How it Works
1. The script uses the `youtube_transcript_api` to fetch the transcript of the specified YouTube video.
2. It saves the transcript to a file named `transcript.txt` in the same directory.
3. The transcript is then sent to OpenAI's GPT-3.5-turbo model for summarization.
4. The generated summary is printed to the console.

## Limitations
- The script currently only works with videos that have available transcripts.
- The quality of the summary depends on the clarity and coherence of the original transcript.
- Very long transcripts may be truncated due to token limits of the GPT-3.5-turbo model.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer
This tool is for educational and research purposes. Always respect YouTube's terms of service and content creators' rights when using this script.
