# Tabeeb.ai: AI-Powered Voice Assistant for Medical Triage

Tabeeb.ai is an **AI-powered voice assistant designed for remote medical triage**, focusing on accessibility for underserved communities. Developed during the MTF Hackathon, this system allows users to describe symptoms over traditional phone calls, providing an immediate and crucial entry point into healthcare, particularly for those without smartphone or internet access.

## Features

  * **Voice-First Medical Triage:** Processes patient queries via phone calls using advanced natural language processing (NLP) model APIs.
  * **Multilingual Support:** Integrates custom Pashto and Dari language models, enabling symptom descriptions in native languages for low-literacy users.
  * **Robust Accessibility:** Architected a voice-first backend to ensure functionality and accessibility through basic feature phones, bypassing the need for smartphones or internet.
  * **Scalable Architecture:** Designed for robustness and potential expansion to serve a wide user base.

## Technologies Used

  * **Backend:** Python
  * **Voice/Telephony:** Twilio
  * **Natural Language Processing (NLP):** OpenAI API
  * **Language Models:** Pashto and Dari specific models

## Project Status

This project was developed during the MTF Hackathon (March 2025) where it secured **3rd Place**. It represents a proof-of-concept for accessible AI in healthcare.

## How to Run (Conceptual)

As a hackathon project, deployment setup can be complex. This project primarily relies on Twilio integration and custom NLP model hosting.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/tabeeb-ai.git
    cd tabeeb-ai
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Configure Twilio & NLP models:** (Details depend on specific setup, requiring Twilio credentials and model loading paths.)
4.  **Run the backend server:**
    ```bash
    python app.py
    ```
