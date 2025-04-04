# 🎥 YouTube Video Transcriber + AI Summary Generator

This project is a complete Python-based AI pipeline that:

✅ Extracts audio from MP4/MP3 videos  
✅ Transcribes speech to text using [OpenAI Whisper](https://github.com/openai/whisper)  
✅ Generates YouTube-style **titles** and **summaries** using [Ollama](https://ollama.com) with the **LLaMA 3** model  

No API keys. No cloud costs. 100% local & privacy-friendly!

---

## 🚀 Features

- 🎙️ Speech-to-text via Whisper
- 🤖 Title + Summary generation using LLaMA 3
- 🎞️ MP4 & MP3 support
- 🧼 Automatically deletes temporary audio files
- 🖥️ Runs locally (Ollama) — no cloud dependencies

---

## 🛠️ Tech Stack

- Python 3
- [Whisper](https://github.com/openai/whisper)
- [Ollama](https://ollama.com)
- ffmpeg (for audio extraction)
- requests

---

## 🧪 Demo Output

**Input:** Sample MP4 video  
**Output:**

🎬 Title: The Future of AI in Everyday Life

📝 Summary: In this video, we explore the rise of artificial intelligence and how it’s impacting industries, communication, and the way we live. From GPT models to automation in business, learn how AI is reshaping our world.



---

## ⚙️ How to Use

1. Clone this repo:

```bash
git clone https://github.com/ShadabAhmedkhan/yt-video-transcriber-ai.git
cd yt-video-transcriber-ai

2. Install dependencies:
pip install ffmpeg-python
pip install requests
pip install openai-whisper

3. Install ffmpeg & add to your system PATH

4. Pull and run LLaMA 3 locally via Ollama:
ollama pull llama3
ollama run llama3

5. Run the script:
python  ollama_api.py

📁 File Structure
ollama_api.py          # Main script
SampleVideo.mp4        # Test input
output_audio.wav       # Temp audio (auto-deleted)
README.md              # Project docs
requirements.txt       # Python dependencies

✅ Requirements
Python 3.8+
ffmpeg installed & in PATH
Ollama installed locally
Whisper is installed via pip

💡 Future Ideas
Auto-process a full folder of videos
Email or Slack daily summaries
Generate SRT subtitles
Frontend web uploader (Flask/FastAPI)

📜 License
MIT License. Free to use, fork, and improve 🚀

🙌 Let's Connect
Built by https://linkedin.com/in/shadabahmedkhan
Feel free to ⭐ star the repo or contribute ideas!
