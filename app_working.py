# # import os
# # from dotenv import load_dotenv
# # import openai
# # from flask import Flask, request
# # import speech_recognition as sr
# # import google.cloud.texttospeech as tts
# # import json

# # app = Flask(__name__)

# # # OpenAI API Key for GPT-4
# # load_dotenv()
# # openai_api_key = os.getenv("OPENAI_API_KEY")

# # # Google Cloud Credentials for Text-to-Speech
# # os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "tabeeb-ai-8e48ac00ea3d.json"

# # # Path to Pre-Recorded Pashto Call
# # AUDIO_FILE = "test_call.wav"

# # @app.route("/")
# # def home():
# #     return "Tabeeb AI is running! Visit /demo to simulate a patient call."

# # ### Process Pre-Recorded Pashto Patient Call
# # @app.route("/demo", methods=["GET"])
# # def demo_call():
# #     """Simulates an AI medical diagnosis for a Pashto-speaking patient"""
    
# #     # Load Pre-Recorded Pashto Audio
# #     recognizer = sr.Recognizer()
# #     with sr.AudioFile(AUDIO_FILE) as source:
# #         audio_data = recognizer.record(source)
# #         patient_text = recognizer.recognize_google(audio_data, language="ps")  # Transcribes Pashto speech

# #     print(f"🗣 Patient Said (Pashto): {patient_text}")

# #     # Get AI Medical Response in Pashto
# #     ai_response = get_medical_advice(patient_text)
# #     print(f"Tabeeb.ai (Pashto): {ai_response}")

# #     # Convert AI Response to Pashto Speech
# #     ai_audio_file = text_to_speech(ai_response)

# #     return f"""
# #     <h2>Patient Spoke in Pashto:</h2> <p>{patient_text}</p>
# #     <h2>Tabeeb.ai's Medical Response in Pashto:</h2> <p>{ai_response}</p>
# #     <h2>Listen to Tabeeb.ai's Response:</h2> <audio controls src="{ai_audio_file}"></audio>
# #     """

# # ### AI Symptom Checker (Pashto-Based)
# # def get_medical_advice(patient_text):
# #     """Uses GPT-4 to analyze symptoms and suggest treatment in Pashto"""
# #     prompt = f"""
# #     You are an AI medical assistant providing healthcare advice in **Pashto** for rural Afghanistan.
# #     A patient describes their symptoms: '{patient_text}'.
# #     Respond **only in Pashto**, and keep your response **brief, culturally appropriate, and easy to understand**.
# #     """

# #     response = openai.ChatCompletion.create(
# #         model="gpt-4",
# #         messages=[{"role": "system", "content": prompt}]
# #     )

# #     return response["choices"][0]["message"]["content"]

# # ### Convert AI Text Response to Pashto Speech (Google TTS)
# # def text_to_speech(text):
# #     """Converts AI-generated Pashto text to speech using Google TTS"""
# #     client = tts.TextToSpeechClient()
# #     synthesis_input = tts.SynthesisInput(text=text)
    
# #     try:
# #         voice = tts.VoiceSelectionParams(language_code="ps-PA", ssml_gender=tts.SsmlVoiceGender.MALE)
# #     except:
# #         voice = tts.VoiceSelectionParams(language_code="fa-AF", ssml_gender=tts.SsmlVoiceGender.MALE)

# #     audio_config = tts.AudioConfig(audio_encoding=tts.AudioEncoding.MP3)

# #     response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

# #     ai_audio_filename = "ai_response.mp3"
# #     with open(ai_audio_filename, "wb") as out:
# #         out.write(response.audio_content)

# #     return ai_audio_filename

# # # Run Flask App
# # if __name__ == "__main__":
# #     app.run(debug=True)

# import os
# from dotenv import load_dotenv
# import openai
# from flask import Flask, request, send_file
# import speech_recognition as sr
# import google.cloud.texttospeech as tts

# app = Flask(__name__)

# # ✅ Load API Keys from .env
# load_dotenv()
# openai_api_key = os.getenv("OPENAI_API_KEY")

# # ✅ Set Google Cloud Credentials for TTS
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "tabeeb-ai-8e48ac00ea3d.json"

# # ✅ Path to Pre-Recorded Pashto Call (test audio file)
# AUDIO_FILE = "test_call.wav"

# @app.route("/")
# def home():
#     return "✅ Tabeeb AI is running! Visit <a href='/demo'>/demo</a> to simulate a patient call."

# ### ✅ Process Pre-Recorded Pashto Patient Call
# # @app.route("/demo", methods=["GET"])
# # def demo_call():
# #     """Simulates an AI medical diagnosis for a Pashto-speaking patient"""
    
# #     recognizer = sr.Recognizer()
# #     try:
# #         with sr.AudioFile(AUDIO_FILE) as source:
# #             audio_data = recognizer.record(source)
# #             # patient_text = recognizer.recognize_google(audio_data, language="ps")  # ✅ Transcribe Pashto speech
# #     except sr.UnknownValueError:
# #         return "❌ Error: Google Speech Recognition could not understand the audio."
# #     except sr.RequestError:
# #         return "❌ Error: Could not connect to Google Speech API."

# #     print(f"🗣 Patient Said (Pashto): {patient_text}")

# #     # ✅ Get AI Medical Response in Pashto
# #     ai_response = get_medical_advice(patient_text)
# #     print(f"💬 Tabeeb.ai (Pashto): {ai_response}")

#     # # ✅ Convert AI Response to Speech (TTS)
#     # ai_audio_file = text_to_speech(ai_response)
    

#     # return f"""
#     # <h2>🗣 Patient Spoke in Pashto:</h2> <p>{patient_text}</p>

#     # <h2>💬 Tabeeb.ai's Medical Response in Pashto:</h2> <p>{ai_response}</p>
#     # <h2>🎧 Listen to Tabeeb.ai's Response:</h2> 
#     # <audio controls>
#     #     <source src="/static/ai_response.mp3" type="audio/mpeg">
#     #     Your browser does not support the audio element.
#     # </audio>
# #     """

# @app.route("/demo", methods=["GET"])
# def demo_call():
#     """Simulates a hardcoded AI medical diagnosis for a Pashto-speaking patient"""

#     # ✅ Hardcoded Patient Symptoms (Pashto & English)
#     patient_text_ps = "زه تب لرم، زما بدن درد کوي او زه ډېر ستړی یم. همداراز، زه د اشتها له لاسه ورکولو سره مخ یم او زما ګیډه درد کوي."
#     patient_text_en = "I have a fever, my body aches, and I feel very tired. Additionally, I have lost my appetite, and my stomach hurts."

#     # ✅ Hardcoded Doctor's Response (Pashto & English)
#     ai_response = get_medical_advice(patient_text_ps)
#     ai_response_ps = "تاسو ته امکان لري چې د ویروسي ناروغۍ لکه زکام یا انفلوینزا سره مخ یئ. مهرباني وکړئ ډيرې اوبه وڅښئ، آرام وکړئ، او که تبه دوام ولري یا درد زیات شي، نو نږدې روغتیايي مرکز ته لاړ شئ."
#     ai_response_en = "You may have a viral illness such as a cold or flu. Please drink plenty of fluids, rest, and if the fever persists or the pain worsens, visit a nearby healthcare center."

#     # ✅ Convert AI Response to Speech (TTS)
#     ai_audio_file = text_to_speech(ai_response)

#     return f"""
#     <h2>🗣 Patient Spoke in Pashto:</h2> 
#     <p><b>Pashto:</b> {patient_text_ps}</p>
#     <p><b>English Translation:</b> {patient_text_en}</p>
    
#     <h2>💬 Tabeeb.ai's Medical Response:</h2>
#     <p><b>Pashto:</b> {ai_response_ps}</p>
#     <p><b>English Translation:</b> {ai_response_en}</p>

#     <h2>🎧 Listen to Tabeeb.ai's Response:</h2> 
#     <audio controls>
#         <source src="/static/ai_response.mp3" type="audio/mpeg">
#         Your browser does not support the audio element.
#     </audio>
#     """

# ### ✅ AI Symptom Checker (Pashto-Based)
# def get_medical_advice(patient_text):
#     """Uses GPT-4 to analyze symptoms and suggest treatment in Pashto"""
#     prompt = f"""
#     You are an AI medical assistant providing healthcare advice in **Pashto** for rural Afghanistan.
#     A patient describes their symptoms: '{patient_text}'.
#     Respond **only in Pashto**, and keep your response **brief, culturally appropriate, and easy to understand**.
#     """

#     client = openai.OpenAI(api_key=openai_api_key)

#     response = client.chat.completions.create(
#         model="gpt-4",
#         messages=[{"role": "system", "content": prompt}]
#     )

#     return response.choices[0].message.content

# ### ✅ Convert AI Text Response to Speech (Arabic as a Workaround)
# def text_to_speech(text):
#     """Converts AI-generated Pashto text to speech using Google TTS (Arabic as fallback)"""
#     client = tts.TextToSpeechClient()
#     synthesis_input = tts.SynthesisInput(text=text)
    
#     # ❌ Google TTS does not support Pashto, so we use Arabic as a workaround
#     voice = tts.VoiceSelectionParams(language_code="ar-XA", name="ar-XA-Wavenet-D", ssml_gender=tts.SsmlVoiceGender.MALE)

#     audio_config = tts.AudioConfig(audio_encoding=tts.AudioEncoding.MP3)

#     response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

#     # ✅ Ensure "static/" directory exists
#     os.makedirs("static", exist_ok=True)

#     ai_audio_filename = "static/ai_response.mp3"
#     with open(ai_audio_filename, "wb") as out:
#         out.write(response.audio_content)

#     return ai_audio_filename  # ✅ Returns path to play in HTML

# # ✅ Run Flask App
# if __name__ == "__main__":
#     app.run(debug=True)

import os
import time
from dotenv import load_dotenv
import openai
from flask import Flask, render_template
import google.cloud.texttospeech as tts

app = Flask(__name__)

# ✅ Load API Keys from .env
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# ✅ Set Google Cloud Credentials for TTS
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "tabeeb-ai-8e48ac00ea3d.json"

# ✅ Hardcoded Patient Symptoms (Pashto & English)
PATIENT_TEXT_PS = "زه تب لرم، زما بدن درد کوي او زه ډېر ستړی یم. همداراز، زه د اشتها له لاسه ورکولو سره مخ یم او زما ګیډه درد کوي."
PATIENT_TEXT_EN = "I have a fever, my body aches, and I feel very tired. Additionally, I have lost my appetite, and my stomach hurts."

# ✅ Simulated AI Response (Pashto & English)
AI_RESPONSE_PS = "تاسو ته امکان لري چې د ویروسي ناروغۍ لکه زکام یا انفلوینزا سره مخ یئ. مهرباني وکړئ ډيرې اوبه وڅښئ، آرام وکړئ، او که تبه دوام ولري یا درد زیات شي، نو نږدې روغتیايي مرکز ته لاړ شئ."
AI_RESPONSE_EN = "You may have a viral illness such as a cold or flu. Please drink plenty of fluids, rest, and if the fever persists or the pain worsens, visit a nearby healthcare center."

# ✅ Generate Pashto TTS Audio for the AI Response
def generate_pashto_audio():
    """Creates an MP3 file for the AI response in Pashto using Google TTS"""
    client = tts.TextToSpeechClient()
    synthesis_input = tts.SynthesisInput(text=AI_RESPONSE_PS)

    # ❌ Google doesn't support Pashto, so using Arabic voice for closest match
    voice = tts.VoiceSelectionParams(language_code="ar-XA", name="ar-XA-Wavenet-D", ssml_gender=tts.SsmlVoiceGender.MALE)
    audio_config = tts.AudioConfig(audio_encoding=tts.AudioEncoding.MP3)

    response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

    output_file = "static/ai_response.mp3"
    os.makedirs("static", exist_ok=True)  # ✅ Ensure directory exists
    with open(output_file, "wb") as out:
        out.write(response.audio_content)
    
    return output_file

# Generate the audio file once so it's ready for the demo
AUDIO_FILE = generate_pashto_audio()

@app.route("/")
def home():
    return """✅ Tabeeb AI is running! Visit <a href='/demo'>/demo</a> to simulate a patient call."""

@app.route("/demo")
def demo_call():
    """Displays the demo UI with patient and AI response, with a simulated delay"""
    
    return render_template("loading.html")  # Show loading page first

@app.route("/result")
def demo_result():
    """Shows AI response after simulated processing delay"""
    time.sleep(2)  # ⏳ Simulate real AI processing time (5 seconds)
    
    return render_template("demo.html", 
                           patient_text_ps=PATIENT_TEXT_PS, 
                           patient_text_en=PATIENT_TEXT_EN,
                           ai_response_ps=AI_RESPONSE_PS, 
                           ai_response_en=AI_RESPONSE_EN,
                           audio_file=AUDIO_FILE)

# ✅ Run Flask App
if __name__ == "__main__":
    app.run(debug=True)
