# AI-Powered-Medical-Chatbot

An interactive AI-powered medical assistant that leverages voice, text, and potentially image inputs to help users understand general health concerns. 
This tool integrates speech recognition, natural language processing, and computer vision to simulate basic doctor-patient interactions. 
Designed for accessibility and user engagement, the chatbot aims to provide concise, educational responses—especially for common symptoms and visual cues like rashes or X-rays—without replacing professional care.

---

## Prerequisites

### Check Python & pip Installation

```bash
python3 --version     # Python 3.12.x or higher
pip3 --version        # pip 24.x.x or higher
```

### Upgrade pip (if needed)

```bash
pip3 install --upgrade pip
```

---

## 🔧 Step-by-Step Setup

### 1. Install Homebrew (macOS only)

```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
brew --version        # Homebrew 4.x.x
```

### 2. Install/Reinstall Python

```bash
brew install python
brew reinstall python@3.13   # Force update if needed
which python3                # /opt/homebrew/bin/python3
/opt/homebrew/bin/python3 --version  # Should show Python 3.13.x
```

---

## Virtual Environment Options

### Option 1: Using `pipenv` 
#### Install `pipenv`

```bash
pip/pip3 install pipenv
```

#### Create & Activate Environment

```bash
pipenv install
pipenv shell
```
---

### Option 2: Using `venv` and `pip` (Alternative method)

#### Create Virtual Environment

```bash
python -m venv venv
```

#### Activate Virtual Environment

**macOS/Linux:**

```bash
source venv/bin/activate
```

**Windows:**

```bash
venv\Scripts\activate
```

#### Install All Dependencies

```bash
pip install -r requirements.txt
```

---

## 📦 Manual Package Installation (if not using `requirements.txt`)

```bash
pipenv install gradio

pipenv install elevenlabs
pipenv install gtts

pipenv install pyaudio
pipenv install speechrecognition pydub
pipenv install pocketsphinx

pipenv install ffmpeg
pipenv install portaudio

pipenv install groq
```

---

## 🔄 Summary of Tools Used

| Tool/Library        | Purpose                                  |
|---------------------|------------------------------------------|
| `groq`              | API integration for advanced LLM models  |
| `gradio`            | Frontend Interface for the chatbot       |
| `gtts`              | Alternative text-to-speech (Google TTS)  |
| `elevenlabs`        | Text-to-speech audio output              |
| `pyaudio`           | Microphone input and audio playback      |
| `speechrecognition` | Convert voice to text                    |
| `pocketsphinx`      | Offline voice recognition engine         |
| `ffmpeg`            | Audio processing                         |
| `portaudio`         | Cross-platform audio I/O library         |


## 🧰 Tools and Libraries Used

| Tool/Library         | Purpose                                                                 |
|----------------------|-------------------------------------------------------------------------|
| `gradio`             | Builds the web-based UI for audio/image input and output                |
| `elevenlabs`         | Converts text to realistic speech using ElevenLabs API                  |
| `gtts`               | Alternative text-to-speech using Google TTS                             |
| `pyaudio`            | Captures microphone input for speech recognition                        |
| `portaudio`          | Audio interface backend required for PyAudio functionality              |
| `SpeechRecognition`  | Transcribes spoken input into text                                      |
| `pocketsphinx`       | Optional offline speech recognition backend                             |
| `ffmpeg`             | Handles audio format conversion internally (used by pydub, etc.)        |
| `opencv-python`      | (Optional) Enables image analysis with computer vision                  |
| `groq`               | Provides access to Groq LLMs for diagnosis and transcription            |
| `dotenv`             | Loads environment variables such as API keys from `.env` file           |
| `pydub`              | Processes and converts audio between formats like WAV and MP3           |
| `logging`            | Logs information and errors to the console                              |
| `base64`             | Encodes images into base64 for API use                                  |
