import os
import time
from dotenv import load_dotenv
from flask import Flask, render_template, send_file

app = Flask(__name__)

# ✅ Load API Keys from .env
load_dotenv()

PATIENT_AUDIO = "static/test_call.wav"

PATIENT_TEXT_PS = "زه تب لرم، زما بدن درد کوي او زه ډېر ستړی یم. همداراز، زه د اشتها له لاسه ورکولو سره مخ یم او زما ګیډه درد کوي."
PATIENT_TEXT_EN = "I have a fever, my body aches, and I feel very tired. Additionally, I have lost my appetite, and my stomach hurts."

AI_RESPONSE_PS = "تاسو ته امکان لري چې د ویروسي ناروغۍ لکه زکام یا انفلوینزا سره مخ یئ. مهرباني وکړئ ډيرې اوبه وڅښئ، آرام وکړئ، او که تبه دوام ولري یا درد زیات شي، نو نږدې روغتیايي مرکز ته لاړ شئ."
AI_RESPONSE_EN = "You may have a viral illness such as a cold or flu. Please drink plenty of fluids, rest, and if the fever persists or the pain worsens, visit a nearby healthcare center."

AI_AUDIO_FILE = "static/ai_response.mp3"

@app.route("/")
def home():
    return """Tabeeb AI is running! Visit <a href='/demo'>/demo</a> to simulate a patient call."""

@app.route("/demo")
def demo_call():
    """First Page: Shows the patient audio and transcript with a button to trigger AI analysis."""
    return render_template("demo.html", 
                           patient_audio=PATIENT_AUDIO,
                           patient_text_ps=PATIENT_TEXT_PS, 
                           patient_text_en=PATIENT_TEXT_EN)

@app.route("/processing")
def processing():
    """Loading screen while AI is 'analyzing'."""
    return render_template("loading.html")

@app.route("/result")
def demo_result():
    """Final Page: Displays both the patient's call and AI's response."""
    time.sleep(3)  # ⏳ Simulate processing delay

    return render_template("result.html", 
                           patient_audio=PATIENT_AUDIO,
                           patient_text_ps=PATIENT_TEXT_PS, 
                           patient_text_en=PATIENT_TEXT_EN,
                           ai_audio=AI_AUDIO_FILE,
                           ai_response_ps=AI_RESPONSE_PS, 
                           ai_response_en=AI_RESPONSE_EN)

# ✅ Run Flask App
if __name__ == "__main__":
    app.run(debug=True)
