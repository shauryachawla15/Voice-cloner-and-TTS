import requests
import os
import base64
print("DEBUG KEY:", os.environ.get("MINIMAX_API_KEY"))

API_KEY = ("YOUR_API_KEY")

upload_url = "https://api.minimax.io/v1/files/upload"
clone_url = "https://api.minimax.io/v1/voice_clone"

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

# ==============================
# 1️⃣ Upload main voice sample
# ==============================
with open("sample.wav", "rb") as f:
    files = {"file": ("sample.wav", f)}
    data = {"purpose": "voice_clone"}

    res = requests.post(upload_url, headers=headers, data=data, files=files)
    res.raise_for_status()

    file_id = res.json()["file"]["file_id"]
    print("✅ Voice File ID:", file_id)


# ==============================
# 2️⃣ Upload prompt audio (optional but improves quality)
# ==============================
with open("sample.wav", "rb") as f:
    files = {"file": ("sample.wav", f)}
    data = {"purpose": "prompt_audio"}

    res = requests.post(upload_url, headers=headers, data=data, files=files)
    res.raise_for_status()

    prompt_file_id = res.json()["file"]["file_id"]
    print("✅ Prompt File ID:", prompt_file_id)


# ==============================
# 3️⃣ Clone + Generate Voice
# ==============================
clone_payload = {
    "file_id": file_id,
    "voice_id": "my_custom_voice_1",   # you define this
    "clone_prompt": {
        "prompt_audio": prompt_file_id,
        "prompt_text": "Yeh awaaz natural aur smooth honi chahiye"
    },
    "text": "Hey, yeh meri cloned voice hai. Ab main AI ke through bol raha hoon.",
    "model": "speech-2.8-hd"
}

clone_headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

res = requests.post(clone_url, headers=clone_headers, json=clone_payload)

print("Status:", res.status_code)
print("Response:", res.text[:200])

res_json = res.json()

# ==============================
# 4️⃣ Save audio (IMPORTANT)
# ==============================
if res.status_code == 200 and res_json.get("base_resp", {}).get("status_code") == 0:

    audio_base64 = res_json["data"]["audio"]
    audio_bytes = base64.b64decode(audio_base64)

    with open("cloned_output.mp3", "wb") as f:
        f.write(audio_bytes)

    print("✅ Cloned voice saved as cloned_output.mp3")

else:
    print("❌ Error:", res_json)