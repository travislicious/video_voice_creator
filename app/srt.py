import assemblyai as aai

# If the API key is not set as an environment variable named
# ASSEMBLYAI_API_KEY, you can also set it like this:

def generate_captions(voice, name):
        
    aai.settings.api_key = "17c6c70f15c54233bf88aceea061e8de"

    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(voice)

    srt = transcript.export_subtitles_srt()

    # Save it to a file
    with open(f"subtitles/{name}.srt", "w", encoding='utf-8') as f:
        f.write(srt)