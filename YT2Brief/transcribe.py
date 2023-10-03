import tempfile
from youtube_transcript_api import YouTubeTranscriptApi


class Transcribe:
    def __init__(self, url) -> None:
        # https://www.youtube.com/watch?v=5NZ4EYkSCcs
        try:
            self.url = url.split("?")[1].split("&")[0].split("=")[1]
        except:
            self.url = None

    def transcribe(self):

        if self.url is None:
            return None
        srt = YouTubeTranscriptApi.get_transcript(self.url)

        transcript = ""

        for i in srt:
            transcript += i["text"] + " "

        transcript = transcript.replace("\n", " ")

        transcript_file = tempfile.NamedTemporaryFile(
            mode="w", delete=False, suffix=".txt"
        )

        transcript_file.write(transcript)

        return transcript_file.name
