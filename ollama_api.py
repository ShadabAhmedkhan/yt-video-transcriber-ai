import whisper
import requests
import ffmpeg
import os

# Add ffmpeg to PATH manually
os.environ["PATH"] += os.pathsep + "C:\\ffmpeg\\ffmpeg-7.1.1-full_build\\bin"

# Load the Whisper model
model = whisper.load_model("base")

API_URL = "http://localhost:11434/api/generate"

def extract_audio_from_video(video_file):
    audio_file = 'output_audio.wav'
    ffmpeg.input(video_file).output(audio_file).run(overwrite_output=True)
    return audio_file

def transcribe_audio(file_path):
    result = model.transcribe(file_path, fp16=False)
    return result['text']

def generate_title_summary(transcript):
    headers = {
        'Content-Type': 'application/json',
    }

    prompt = f"""
    You are a helpful AI assistant. Based on the following transcript, generate:
    1. A catchy YouTube-style title
    2. A brief summary (2–4 lines)

    Transcript:
    {transcript}
    """

    response = requests.post(API_URL, json={
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }, headers=headers)

    result = response.json()
    return result.get("response", "No response")

def process_video(video_file):
    audio_file = extract_audio_from_video(video_file)
    transcript = transcribe_audio(audio_file)
    os.remove(audio_file)  # Clean up
    summary = generate_title_summary(transcript)
    return summary

# Example usage
video_file = 'SampleVideo.mp4'
summary = process_video(video_file)
print("Generated Title & Summary:\n")
print(summary)
