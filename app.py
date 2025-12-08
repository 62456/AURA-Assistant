# app.py
from flask import Flask, request, jsonify, send_from_directory
from main import (
    model,
    tokenizer,
    label_encoder,
    data,
    social_media,
    schedule,
    openApp,
    closeApp,
    browsing,
    condition,
)
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import random

app = Flask(__name__)

@app.route("/")
def index():
    # serve index.html from same folder
    return send_from_directory(".", "index.html")


@app.route("/chat", methods=["POST"])
def chat():
    payload = request.get_json(force=True)
    msg = (payload.get("message") or "").lower()
    print("User said:", msg)

    reply = "I’m not sure how to respond to that."

    # 1) SOCIAL MEDIA (facebook / instagram / discord / whatsapp)
    if any(x in msg for x in ["facebook", "instagram", "discord", "whatsapp"]):
        social_media(msg)  # this should open browser as in main.py
        reply = f"Opening {msg} from Python backend."

    # 2) BROWSER (google / edge / general browsing)
    elif any(x in msg for x in ["open google", "google", "open edge", "edge browser"]):
        browsing(msg)  # your existing function in main.py
        reply = "Opening your browser (Google/Edge) from Python backend."

    # 3) APPS (calculator / notepad / paint)
    elif any(x in msg for x in ["open calculator", "open notepad", "open paint"]):
        openApp(msg)
        reply = "Opening application from the Python backend."

    elif any(x in msg for x in ["close calculator", "close notepad", "close paint"]):
        closeApp(msg)
        reply = "Closing application from the Python backend."

    # 4) SCHEDULE
    elif "schedule" in msg or "time table" in msg or "timetable" in msg:
        schedule()
        reply = "Reading today’s schedule from your timetable."

    # 5) SYSTEM CONDITION
    elif "system condition" in msg or "condition of the system" in msg:
        condition()
        reply = "I’ve checked the system condition and spoken it out."

    # 6) FALLBACK → ML MODEL (same logic as your main.py)
    else:
        seq = pad_sequences(
            tokenizer.texts_to_sequences([msg]),
            maxlen=20,
            truncating="post",
        )
        preds = model.predict(seq)
        tag = label_encoder.inverse_transform([np.argmax(preds)])[0]

        for intent in data["intents"]:
            if intent["tag"] == tag:
                reply = random.choice(intent["responses"])
                break

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)