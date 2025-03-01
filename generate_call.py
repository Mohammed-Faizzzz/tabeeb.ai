import os
from google.cloud import texttospeech

# ✅ Set Google Cloud Credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "tabeeb-ai-8e48ac00ea3d.json"

# ✅ Initialize Google Text-to-Speech Client
client = texttospeech.TextToSpeechClient()

# ✅ Patient's Call in Pashto (But Read Out in Arabic Voice)
patient_text = """
سلام ډاکټر صیب، زه درې ورځې راهیسې نس ناستی لرم، بدن مې کمزوری شوی او ستړی احساسوم.
او هم زه ډېر تږی یم او د خولې وچوالی لرم. زه باید څه وکړم؟
"""

# ✅ Convert Text to Speech (Using Arabic as a Workaround)
synthesis_input = texttospeech.SynthesisInput(text=patient_text)

voice = texttospeech.VoiceSelectionParams(
    language_code="ar-XA",  # ✅ Use Arabic (widely understood in Afghanistan)
    name="ar-XA-Wavenet-D",  # ✅ Male voice
    ssml_gender=texttospeech.SsmlVoiceGender.MALE
)

audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.LINEAR16)

# ✅ Generate the Speech
response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

# ✅ Save as test_call.wav
with open("test_call.wav", "wb") as out:
    out.write(response.audio_content)

print("✅ test_call.wav generated successfully! Listen to it to ensure it works.")
