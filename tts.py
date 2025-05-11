#!pip install SpeechRecognition
#!pip install torch torchvision torchaudio
#!pip install pyttsx3
#!sudo apt update && sudo apt install espeak-ng -y
#!sudo apt update && sudo apt install -y portaudio19-dev
#!pip install pyaudio

import os
import torch
import speech_recognition as sr
import pyttsx3
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# Set Hugging Face token securely
HUGGINGFACE_TOKEN = "***********************"  # Replace with your actual token

if not HUGGINGFACE_TOKEN:
    raise ValueError("Hugging Face API token is missing!")

# Define model name
MODEL_NAME = "meta-llama/Llama-3.2-3B-Instruct"

# Load model and tokenizer with error handling
try:
    print("🔄 Loading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, token=HUGGINGFACE_TOKEN)

    print("🔄 Loading model...")
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        device_map="auto",
        token=HUGGINGFACE_TOKEN,
        trust_remote_code=True
    )

    print("✅ Model & tokenizer loaded successfully!")

    # Create NLP pipeline
    nlp_pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer)
except Exception as e:
    raise RuntimeError(f"Error loading model: {e}")

# Initialize TTS engine
tts_engine = pyttsx3.init()

def generate_response(prompt):
    """****************************************""" #put your actual prompt for your specific use case
    """Generates a response using the NLP model."""
    topic_prompt = f"************************. {prompt}"
    
    try:
        response = nlp_pipeline(
            topic_prompt, 
            max_length=100, 
            do_sample=True, 
            truncation=True, 
            pad_token_id=tokenizer.eos_token_id  # Explicitly setting this to suppress the warning
        )
        print(f"DEBUG: Raw Response from Model: {response}")
        bot_reply = response[0]['generated_text']
        
        # Safety check - ensure response is about your case
        if "*********************" not in bot_reply:
            bot_reply = "I only discuss *********, . Please ask about him."

        return bot_reply
    except Exception as e:
        return f"Error generating response: {e}"



def recognize_speech():
    """Captures and transcribes speech using Google STT."""
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Sorry, I could not understand the audio."
    except sr.RequestError:
        return "Error with speech recognition service."
    except Exception as e:
        return f"Speech recognition error: {e}"

def speak_text(text):
    """Converts text to speech using pyttsx3."""
    try:
        tts_engine.say(text)
        tts_engine.runAndWait()
    except Exception as e:
        print(f"Error with text-to-speech: {e}")

# ---- RUN CLI APP ----
if __name__ == "__main__":
    print("\n🚀  Chatbot & Call Bot (CLI Version)")

    while True:
        print("\nChoose Input Mode:")
        print("1️⃣ Text")
        print("2️⃣ Voice")
        print("3️⃣ Exit")

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            user_input = input("\nEnter your message: ").strip()
            if user_input:
                response = generate_response(user_input)
                print(f"🤖 Bot: {response}")
                speak_text(response)

        elif choice == "2":
            print("\n🎤 Speak now...")
            user_input = recognize_speech()
            print(f"🎙️ You said: {user_input}")

            response = generate_response(user_input)
            print(f"🤖 Bot: {response}")
            speak_text(response)

        elif choice == "3":
            print("\n👋 Exiting... Goodbye!")
            break

        else:
            print("\n⚠️ Invalid choice! Please enter 1, 2, or 3.")
