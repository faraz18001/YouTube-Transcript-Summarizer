import os
from openai import OpenAI
from youtube_transcript_api import YouTubeTranscriptApi

# YouTube video ID
video_id = 'S8h_HSNc-8I'  # Replace with the actual video ID

# Fetch and process the transcript
transcript = YouTubeTranscriptApi.get_transcript(video_id)
transcript_text = ' '.join([t['text'] for t in transcript])

# Save the transcript to a file
with open('transcript.txt', 'w', encoding='utf-8') as f:
    f.write(transcript_text)

# Set up OpenAI client
os.environ['OPENAI_API_KEY'] = ''  # Replace with your actual API key
client = OpenAI()

# Generate summary
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant that summarizes YouTube video transcripts."},
        {"role": "user", "content": f"Please summarize the following YouTube video transcript:\n\n{transcript_text}"}
    ],
)

# Print the summary
print(response.choices[0].message.content)