from flask import Flask, render_template, request, jsonify
import pyttsx3
import threading
import os
app = Flask(__name__)

def speak(text):
    engine = pyttsx3.init()   # NEW engine each time
    engine.say(text)
    engine.runAndWait()
    engine.stop()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/speak", methods=["POST"])
def speak_api():
    data = request.json
    text = data.get("text", "").strip()

    if not text:
        return jsonify({"status": "error", "msg": "Empty text"})

    threading.Thread(target=speak, args=(text,), daemon=True).start()
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


