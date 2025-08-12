from youtube_transcript_api import YouTubeTranscriptApi
from langchain.schema import Document
import re

def get_video_id(url):
    """Extract video ID from YouTube URL"""
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", url)
    return match.group(1) if match else None

def load_yt_transcript(url: str):
    """Load YouTube transcript - WORKING VERSION"""
    video_id = get_video_id(url)
    if not video_id:
        raise ValueError("Invalid YouTube URL")

    # Create API instance and fetch transcript
    api = YouTubeTranscriptApi()
    fetched_transcript = api.fetch(video_id)
    
    # Extract text from snippets
    text_parts = []
    for snippet in fetched_transcript.snippets:
        clean_text = snippet.text.replace('\n', ' ').strip()
        if clean_text:
            text_parts.append(clean_text)
    
    text = ' '.join(text_parts)
    
    return [Document(page_content=text)]