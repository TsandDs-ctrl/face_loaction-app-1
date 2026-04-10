from flask import Flask, request, render_template
import os
import json
from datetime import datetime

app = Flask(__name__)

LOC_DIR = "locations"
os.makedirs(LOC_DIR, exist_ok=True)

# Webseite anzeigen
@app.route("/")
def index():
    return render_template("index.html")

# Standort speichern
@app.route("/save_location", methods=["POST"])
def save_location():
    data = request.json
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(LOC_DIR, f"standort_{timestamp}.json")

    with open(filename, "w") as f:
        json.dump(data, f)

    print("Gespeichert:", filename)
    return "OK"

# Start
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)