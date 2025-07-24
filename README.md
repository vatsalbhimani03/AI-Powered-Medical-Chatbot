# AI-Powered-Medical-Chatbot

An interactive AI-powered medical assistant that leverages voice, and image inputs to help users understand general health concerns. 
This tool integrates speech recognition (Speech-To-Text & Text-To-Speech), natural language processing (NLP), and computer vision to simulate basic doctor-patient interactions. 
Designed for accessibility and user engagement, the chatbot aims to provide concise, educational responses—especially for common symptoms and visual cues like rashes or X-rays—without replacing professional care.

> ❗ **Note:** This is not a diagnostic tool. It is designed for **educational and demonstration purposes only**.

## 🔍 Core Features

- 🎤 **Voice Input**: Users can speak symptoms using a microphone.
- 🖼️ **Image Upload**: Users can upload medical images (e.g., rashes, X-rays).
- 💬 **AI Response**: Uses LLM to generate concise, easy-to-understand medical feedback.
- 🔊 **Voice Output**: Responses are spoken back using realistic TTS.
  
---
## 💡 AI-Powered Medical Chatbot – Demo Output

### 🔷 Voice + Image Input  
![With Voice and Image Input](Output/With%20Voice%20and%20Image%20input.jpg)
---
### 🔷 Only Voice Input  
![With only Voice Input](Output/With%20only%20Voice%20input.jpg)
---
### 🔷 Only Image Input  
![With only Image Input](Output/With%20only%20Image%20input.jpg)
---
## 💡 AI-Powered Medical Chatbot – Architecture
![Architecture](Output/Chatbot%20Architecture.png)
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

## 🔐 API Keys (Required)

To run the chatbot, you must provide your own API keys:

### ➤ Required APIs:

- **Groq API Key**: Used for LLM-based text and image processing.
- **ElevenLabs API Key (optional gTTS)**: Used for generating realistic voice output.

### ➤ Setup `.env` File

Create a `.env` file in the root directory and add your keys like this:

```env
GROQ_API_KEY=your_groq_api_key_here
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here


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
## Final command to run the file
#### Activate the environment (exit & rerun every time after changing .env file)
```bash
pipenv shell
```
#### Run both files
```bash
python medical_chatbot_backend.py
python medical_chatbot_frontend.py
```
---

## 📦 Manual Package Installation 

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
