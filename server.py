
from flask import Flask, request, jsonify
import openai

openai.api_key = "sk-...your_openai_api_key_here..."

app = Flask(__name__)

@app.route("/recognize", methods=["POST"])
def recognize():
    if "audio" not in request.files:
        return jsonify({"error": "No audio file uploaded"}), 400

    audio_file = request.files["audio"]
    try:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        return jsonify({"text": transcript["text"]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
