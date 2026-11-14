"""Notes API — a tiny Flask service for the Jenkins Docker CI/CD lab (Lab 6)."""
import os

from flask import Flask, jsonify, request

app = Flask(__name__)
_notes = []
_next_id = 1


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.get("/api/notes")
def list_notes():
    return jsonify(notes=_notes)


@app.post("/api/notes")
def add_note():
    global _next_id
    body = request.get_json(silent=True) or {}
    text = (body.get("text") or "").strip()
    if not text:
        return jsonify(error="text is required"), 400
    note = {"id": _next_id, "text": text}
    _next_id += 1
    _notes.append(note)
    return jsonify(note=note), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
