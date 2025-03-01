import os
import openai
from flask import Flask, request, render_template, redirect
from twilio.twiml.voice_response import VoiceResponse
import speech_recognition as sr
import google.cloud.texttospeech as tts
from pydub import AudioSegment
import json

app = Flask(__name__)

# Twilio API Credentials
TWILIO_CALL_FORWARDING_NUMBER = os.getenv("+447386808228")

# OpenAI API Key for Whisper + GPT
openai.api_key = os.getenv("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")

# Google Cloud Credentials for Text-to-Speech
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "tabeeb-ai-8e48ac00ea3d.json"

# Temporary storage for recorded audio
AUDIO_FILE = "recorded_audio.wav"

# Doctor Database (Simple JSON File Placeholder)
DOCTOR_DB = "doctors.json"


if not os.path.exists(DOCTOR_DB):
    with open(DOCTOR_DB, "w") as f:
        json.dump({}, f)

def load_doctors():
    """Load the doctor database from a JSON file."""
    with open(DOCTOR_DB, "r") as f:
        return json.load(f)

def save_doctors(doctors):
    """Save the doctor database to a JSON file."""
    with open(DOCTOR_DB, "w") as f:
        json.dump(doctors, f, indent=4)

@app.route("/")
def home():
    return "Tabeeb AI is running! Call your Twilio number to test."

### Handle Incoming Call & Record Symptoms
@app.route("/voice", methods=["POST"])
def voice():
    """Handles incoming Twilio voice calls"""
    response = VoiceResponse()
    
    # Ask user to describe symptoms in Pashto
    response.say("د طبي مرستې لپاره، مهرباني وکړئ خپل نښې بیان کړئ.", voice="Polly.Zayd")  # Polly.Zayd is an Arabic voice, best for Pashto
    response.record(max_length=30, timeout=5, play_beep=True, recording_status_callback="/process_audio")
    
    return str(response)


### Process Recorded Audio & Convert Speech to Text
@app.route("/process_audio", methods=["POST"])
def process_audio():
    """Handles recorded voice message, converts speech to text, and generates AI response"""
    recording_url = request.form["RecordingUrl"]  # Get Twilio's recording URL

    # Download recorded audio
    os.system(f"curl -o {AUDIO_FILE} {recording_url}")

    # Convert audio to text (Using OpenAI Whisper)
    recognizer = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio_data = recognizer.record(source)
        symptoms_text = recognizer.recognize_google(audio_data, language="ps")  # Set Whisper to Pashto

    # Get AI Diagnosis Response
    ai_response = get_medical_advice(symptoms_text)

    # Convert AI response to speech
    audio_response_file = text_to_speech(ai_response)

    # Play AI Response
    response = VoiceResponse()
    response.play(audio_response_file)

    # If the AI detects a severe case, forward to a doctor
    if "urgent" in ai_response.lower() or "emergency" in ai_response.lower():
        response.say("دا یو جدي حالت دی، موږ تاسو د یو ډاکټر سره نښلوو.")
        doctor_number = get_available_doctor()
        if doctor_number:
            response.dial(doctor_number)
        else:
            response.say("اوس مهال هیڅ ډاکټران شتون نلري، مهرباني وکړئ نږدې روغتون ته لاړ شئ.")

    return str(response)


### AI Symptom Checker (Pashto-Based)
def get_medical_advice(symptoms_text):
    """Uses GPT-4 to analyze symptoms and suggest treatment in Pashto"""
    prompt = f"""
    You are an AI medical assistant providing healthcare advice in **Pashto** for rural Afghanistan.
    A patient describes their symptoms: '{symptoms_text}'. 
    Respond **only in Pashto**, and keep your response **brief, culturally appropriate, and easy to understand**.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}]
    )

    return response["choices"][0]["message"]["content"]


### Convert AI Text Response to Speech (Pashto TTS)
def text_to_speech(text):
    """Converts AI-generated Pashto text to speech using Google TTS"""
    client = tts.TextToSpeechClient()
    synthesis_input = tts.SynthesisInput(text=text)
    
    # Try Pashto, fallback to Dari if unavailable
    try:
        voice = tts.VoiceSelectionParams(language_code="ps-PA", ssml_gender=tts.SsmlVoiceGender.MALE)
    except:
        voice = tts.VoiceSelectionParams(language_code="fa-AF", ssml_gender=tts.SsmlVoiceGender.MALE)

    audio_config = tts.AudioConfig(audio_encoding=tts.AudioEncoding.MP3)

    response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

    audio_filename = "ai_response.mp3"
    with open(audio_filename, "wb") as out:
        out.write(response.audio_content)

    return audio_filename


### Emergency Call Forwarding to Verified Doctors
@app.route("/emergency", methods=["POST"])
def emergency():
    """Routes the call to an available verified doctor"""
    response = VoiceResponse()
    doctor_number = get_available_doctor()

    if doctor_number:
        response.say("تاسو جدي روغتیايي ستونزې لرئ، موږ به تاسو د یو ډاکټر سره ونښلوو.", voice="Polly.Zayd")
        response.dial(doctor_number)
    else:
        response.say("بخښنه غواړو، هیڅ تصدیق شوی ډاکټر شتون نلري. مهرباني وکړئ نږدې روغتون ته لاړ شئ.")

    return str(response)


def get_available_doctor():
    """Finds an available verified doctor from the database"""
    doctors = load_doctors()
    for doctor, info in doctors.items():
        if info["verified"]:  # Check if doctor is verified
            return info["phone_number"]
    return None  # No available doctors


# Run Flask App
if __name__ == "__main__":
    app.run(debug=True)
