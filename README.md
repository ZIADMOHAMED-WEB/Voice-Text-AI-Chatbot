# 🗣️ Voice & Text AI Chatbot using Meta LLaMA-3 + TTS/STT

A CLI-based interactive chatbot and call-bot built using `meta-llama/Llama-3.2-3B-Instruct`, supporting both **voice and text inputs**. The bot uses Google Speech Recognition for STT (speech-to-text) and `pyttsx3` for offline TTS (text-to-speech).

---

## 🚀 Features

- 🎤 Speech-to-text with Google Web Speech API
- 🤖 Text generation using Meta's LLaMA-3 via Hugging Face
- 🔊 Offline text-to-speech via `pyttsx3`
- 🧠 Context-aware NLP pipeline powered by Transformers
- ✅ Simple CLI with interactive voice/text modes

---

## 🧰 Requirements

Install the dependencies:

```bash
pip install SpeechRecognition
pip install torch torchvision torchaudio
pip install pyttsx3
pip install pyaudio
pip install transformers huggingface_hub
Linux only: You may also need the following system packages:

bash
Copy
Edit
sudo apt update && sudo apt install -y espeak-ng portaudio19-dev
🔐 Hugging Face Token
This script requires a Hugging Face access token to load the LLaMA model.

Get your token from: https://huggingface.co/settings/tokens

Replace this line in the script:

python
Copy
Edit
HUGGINGFACE_TOKEN = "***********************"
🤖 Model Used
Model: meta-llama/Llama-3.2-3B-Instruct

Pipeline: text-generation from Hugging Face Transformers

🖥️ How It Works
User selects text or voice input.

If voice is selected, Google Speech API transcribes the audio.

The transcribed or typed text is passed to LLaMA-3.

The generated response is printed and spoken aloud using pyttsx3.

▶️ Usage
bash
Copy
Edit
python chatbot_voice_text.py
Press 1 to chat via text

Press 2 to chat via microphone

Press 3 to exit

🗣️ Example CLI Interaction
bash
Copy
Edit
Choose Input Mode:
1️⃣ Text
2️⃣ Voice
3️⃣ Exit

Enter your choice (1/2/3): 1

Enter your message: Tell me a joke

🤖 Bot: Why don't scientists trust atoms? Because they make up everything.
📋 Notes
You can modify the generate_response() function to prepend your custom topic prompt or restrict to specific domains.

STT uses Google's free online speech-to-text engine; internet is required for that part.

🔐 Safety & Filtering
You can hardcode a check in the generate_response() function to filter the response:

python
Copy
Edit
if "EXPECTED_TOPIC_KEYWORD" not in bot_reply:
    bot_reply = "I only respond to questions about XYZ topic. Please stay on topic."
📄 License
This project is a prototype and uses third-party models. Please refer to the Meta and Google licensing terms for the models and APIs used.
