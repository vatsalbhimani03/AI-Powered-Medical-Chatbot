
import os
import gradio as gr
from medical_chatbot_backend import (
    image_to_base64, get_doctor_response, convert_speech_to_text, speak_with_elevenlabs, speak_with_gtts
)

instruction = (
    "You are acting as a human doctor for educational use. "
    "If a patient describes symptoms, reply briefly (max 3 sentences) without AI disclaimers. "
    "Use clear language and avoid numbers or markdown. Be concise and start immediately with a diagnosis."
)

def handle_patient_input(audio_path, image_path):
    transcript = "No voice input provided"
    response = "Please provide an image or speak your symptoms."
    audio_output_path = None

    if audio_path:
        transcript = convert_speech_to_text(audio_path)
    
    if image_path and transcript:
        encoded = image_to_base64(image_path)
        query = f"{instruction}\n\nSymptoms: {transcript}"
        response = get_doctor_response(query, image_base64=encoded)

    elif audio_path:
        query = f"{instruction}\n\nSymptoms: {transcript}"
        response = get_doctor_response(query)

    elif image_path:
        prompt = instruction + "\n\nPlease examine the uploaded medical image."
        encoded = image_to_base64(image_path)
        response = get_doctor_response(prompt, image_base64=encoded)

    audio_output_path = speak_with_elevenlabs(response)
    # audio_output_path = speak_with_gtts(response)

    return transcript, response, audio_output_path

with gr.Blocks(theme=gr.themes.Soft(primary_hue="blue")) as app:
    gr.Markdown("## 🩺 AI Medical Assistant with Voice & Vision")

    with gr.Row():
        audio_input = gr.Audio(sources=["microphone"], type="filepath", label="🎤 Your Voice")
        image_input = gr.Image(type="filepath", label="🖼️ Optional Medical Image")

    transcript_output = gr.Textbox(label="📝 Transcribed Input")
    doctor_text_output = gr.Textbox(label="🧑‍⚕️ Doctor's Diagnosis")
    voice_output = gr.Audio(label="🔊 Listen to Doctor's Response")

    submit_button = gr.Button("Submit")
    submit_button.click(
        fn=handle_patient_input,
        inputs=[audio_input, image_input],
        outputs=[transcript_output, doctor_text_output, voice_output]
    )

app.launch()
