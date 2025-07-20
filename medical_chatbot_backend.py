# required libraries
import os
import base64
import logging
import platform
import subprocess
from io import BytesIO

import speech_recognition as sr
from pydub import AudioSegment
from gtts import gTTS
from groq import Groq
import elevenlabs
from elevenlabs.client import ElevenLabs
from dotenv import load_dotenv


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~STEP 1 (Patient's input - Voice & Image)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# fetching Groq & ElevenLabs api key (Load keys from .env)
load_dotenv()
GROQ_KEY = os.getenv("GROQ_API_KEY")
ELEVEN_KEY = os.getenv("ELEVEN_API_KEY")

# converting/encoding an image file to the required format
def image_to_base64(path):
    with open(path, "rb") as img:  #rb - read binary format
        return base64.b64encode(img.read()).decode("utf-8")

# Setup logging for CLI only
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

# recording an audio from user end
def capture_microphone(output_file="recorded_input.mp3"):
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as mic:
            logging.info("Listening... please describe your symptoms.")
            recognizer.adjust_for_ambient_noise(mic, duration=1)
            recorded = recognizer.listen(mic, timeout=20)
            raw_wav = recorded.get_wav_data()
            audio = AudioSegment.from_wav(BytesIO(raw_wav))
            audio.export(output_file, format="mp3", bitrate="128k")
            logging.info(f"Voice saved to: {output_file}")
    except Exception as err:
        logging.error(f"Mic recording failed: {err}")

# converting patient's speech/voice to text for transcription 
def convert_speech_to_text(file_path):
    client = Groq(api_key=GROQ_KEY)
    with open(file_path, "rb") as audio_file:
        response = client.audio.transcriptions.create(
            model="whisper-large-v3",
            file=audio_file,
            language="en"
        )
    return response.text





# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~STEP 2 (response generated using Groq API)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# getting text output by passing patient's input (LLM Diagnosis)
def get_doctor_response(text_prompt, image_base64=None):
    client = Groq(api_key=GROQ_KEY)
    if image_base64:
        message = [{
            "role": "user",
            "content": [
                {"type": "text", "text": text_prompt},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_base64}"}}
            ]
        }]
    else:
        message = [{"role": "user", "content": text_prompt}]

    result = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=message
    )
    return result.choices[0].message.content





# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~STEP 3 (Doctor's Output as Audio file)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# setting up Text-to-Speech (TTS) model with gTTS
def speak_with_gtts(response_text, output_file="response_gtts.mp3"):
    try:
        gTTS(text=response_text, lang="en", slow=False).save(output_file)
        return output_file
    except Exception as e:
        logging.error(f"gTTS failed: {e}")
        return None

# setting up Text to Speech(TTS) model with ElevenLabs
def speak_with_elevenlabs(response_text, output_file="response_elevenlabs.mp3"):
    try:
        client = ElevenLabs(api_key=ELEVEN_KEY)
        audio = client.generate(
            text=response_text,
            voice="Samantha",
            output_format="mp3_22050_32",
            model="eleven_turbo_v2"
        )
        elevenlabs.save(audio, output_file)
        return output_file
    except Exception as e:
        logging.error(f"ElevenLabs TTS failed: {e}")
        return None

