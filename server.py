import os
from flask import Flask, request, jsonify, send_from_directory
import requests

app = Flask(__name__, static_folder=".", static_url_path="")

NVIDIA_API_KEY = os.environ["NVIDIA_API_KEY"]
NVIDIA_MODEL = "meta/llama-3.2-11b-vision-instruct"


@app.route("/")
def index():
    return send_from_directory(".", "index.html")


@app.route("/api/ask", methods=["POST"])
def ask():
    question = (request.get_json(silent=True) or {}).get("question", "").strip()
    if not question:
        return jsonify({"error": "Soru boş olamaz."}), 400

    response = requests.post(
        "https://integrate.api.nvidia.com/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {NVIDIA_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": NVIDIA_MODEL,
            "messages": [
                {
                    "role": "system",
                    "content": "Sen DersCep uygulamasında öğrencilere yardımcı olan bir ders asistanısın. Sorulara Türkçe, kısa ve adım adım anlaşılır şekilde cevap ver.",
                },
                {"role": "user", "content": question},
            ],
            "max_tokens": 600,
        },
        timeout=30,
    )

    if response.status_code != 200:
        return jsonify({"error": "AI servisine ulaşılamadı."}), 502

    data = response.json()
    answer = data["choices"][0]["message"]["content"]
    return jsonify({"answer": answer})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
