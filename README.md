# 🎙️ Voice Cloning + Text-to-Speech Pipeline (Minimax API)

This project demonstrates a complete pipeline for **AI-based voice cloning and text-to-speech (TTS)** using Python and API integration.

It allows you to:
- Upload a voice sample 🎤  
- Clone the voice 🧠  
- Generate speech from text in that cloned voice 🔊  

---

## 🚀 Features

- ✅ Voice sample upload (audio → file_id)
- ✅ Optional prompt audio for better voice quality
- ✅ Voice cloning using AI models
- ✅ Text-to-speech generation using cloned voice
- ✅ Base64 audio decoding and file saving
- ✅ Error handling for API responses

---

## 🧠 How It Works

### Step 1: Upload Voice Sample
- Upload a `.mp3` or `.wav` file
- Get a `file_id`

### Step 2: (Optional) Upload Prompt Audio
- Short sample (3–5 sec)
- Improves tone/style of generated voice

### Step 3: Clone Voice
- Use `file_id` + optional `prompt_file_id`
- Generate a custom `voice_id`

### Step 4: Generate Speech
- Input text
- Output = speech in cloned voice

---

## 📁 Project Structure

voice_cloner/
│── main.py
│── my_voice.wav # Main voice sample (10–60 sec)
│── sample.wav # Optional prompt audio
│── output.mp3 # Generated output


---

## ⚙️ Installation

### 1. Clone repo
```bash
git clone https://github.com/your-username/voice-cloner.git
cd voice-cloner
2. Create virtual environment
python -m venv venv
venv\Scripts\activate
3. Install dependencies
pip install requests
🔑 Setup API Key

You can either:

Option 1 (Recommended)

Set environment variable:

setx MINIMAX_API_KEY "your_api_key_here"

Restart terminal after this.

Option 2 (Quick Test)

Directly paste in code:

API_KEY = "your_api_key_here"
🧑‍💻 Usage
Run the script
python main.py
📌 Example Input Text
Hey, yeh meri cloned voice hai. Ab main AI ke through bol raha hoon.
🎧 Output

Generated file: output.mp3

Plays in VLC or any media player

⚠️ Important Notes

Voice sample must be:

Minimum 10 seconds

Clear audio (low noise)

Supported formats:

.mp3, .wav, .m4a

Voice cloning may require API credits

🐞 Common Errors & Fixes
❌ FileNotFoundError

➡️ Make sure file name matches exactly in code

❌ API Key not found

➡️ Set environment variable or hardcode key

❌ Insufficient balance

➡️ Add credits to API account

❌ Audio not playing

➡️ Ensure base64 decoding is done correctly

🧠 Learnings

Difference between TTS and voice cloning

Handling API-based ML workflows

Working with audio data (upload, decode, playback)

Debugging real-world integration issues

🚀 Future Improvements

🎤 Real-time mic input

🤖 AI chatbot + voice response

🔄 Streaming audio output

🌐 Web interface for interaction

📌 Tech Stack

Python

Requests

AI Speech APIs

Audio Processing

🙌 Acknowledgements

Inspired by modern AI voice systems and real-world voice assistant applications.

📬 Connect

If you found this useful or want to collaborate, feel free to reach out!
