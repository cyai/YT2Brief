from transcribe import Transcribe

url = "https://www.youtube.com/watch?v=5NZ4EYkSCcs"

transcribe = Transcribe(url)

print(transcribe.transcribe())
