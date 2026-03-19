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

