
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



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~UI~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

with gr.Blocks(theme=gr.themes.Soft(primary_hue="teal"), css="""
    body {
        background-color: #fdfdfd;
        font-family: 'Segoe UI', sans-serif;
        animation: fadein 1s ease-in;
    }
    .title {
        font-size: 2.5rem;
        font-weight: 700;
        color: #008080;
        margin-bottom: 0.3em;
        animation: slideInTop 0.7s ease-out;
    }
    .subtitle {
        font-size: 1.2rem;
        color: #555;
        margin-bottom: 1em;
        animation: fadein 2s ease-in;
    }
    .section-label {
        font-weight: 700;
        color: #444;
        margin-top: 10px;
        animation: slideInLeft 0.5s ease-in;
    }
    .gradio-container {
        max-width: 900px;
        margin: auto;
        padding: 40px 20px;
    }
    .gr-button {
        transition: all 0.3s ease-in-out;
        transform: scale(1);
    }
    .gr-button:hover {
        background: linear-gradient(135deg, #00bcd4, #00838f) !important;
        transform: scale(1.05);
    }

    @keyframes fadein {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    @keyframes slideInTop {
        from { transform: translateY(-20px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }
    @keyframes slideInLeft {
        from { transform: translateX(-20px); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
""") as app:

    with gr.Column():
        gr.HTML("<div class='title'>🩺 Virtual Medical Assistant</div>")
        gr.HTML("<div class='subtitle'>Your voice & image-powered health companion.</div>")

        with gr.Row():
            with gr.Column():
                gr.HTML("<div class='section-label'>🎤 Speak Your Symptoms</div>")
                audio_input = gr.Audio(sources=["microphone"], type="filepath", label=None)

            with gr.Column():
                gr.HTML("<div class='section-label'>🖼️ Upload Medical Image (optional)</div>")
                image_input = gr.Image(type="filepath", label=None)

        submit_button = gr.Button("🔍 Analyze", variant="primary")

        with gr.Row():
            with gr.Column():
                transcript_output = gr.Textbox(label="What you said", lines=2, max_lines=4, interactive=False)

            with gr.Column():
                doctor_text_output = gr.Textbox(label="Doctor’s Response", lines=2, max_lines=4, interactive=False)

        gr.HTML("<div class='section-label'>🔊 Doctor's Voice Reply</div>")
        voice_output = gr.Audio(label=None, autoplay=True)

        submit_button.click(
            fn=handle_patient_input,
            inputs=[audio_input, image_input],
            outputs=[transcript_output, doctor_text_output, voice_output]
        )

app.launch(share=True)
