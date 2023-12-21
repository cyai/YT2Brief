import tempfile
from youtube_transcript_api import YouTubeTranscriptApi


class Transcribe:
    def __init__(self, url):
        self.video_id = self.extract_video_id(url)

    def extract_video_id(self, url):
        try:
            params = url.split("?")[1].split("&")
            for param in params:
                key, value = param.split("=")
                if key == "v":
                    return value
        except:
            return None

    def transcribe(self):
        if not self.video_id:
            return None

        try:
            srt = YouTubeTranscriptApi.get_transcript(self.video_id)

            transcript = " ".join([i["text"] for i in srt])

            transcript = transcript.replace("\n", " ")

            with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".txt") as transcript_file:
                transcript_file.write(transcript)

            return transcript_file.name

        except Exception as e:
            print(f"An error occurred: {e}")
            return None
