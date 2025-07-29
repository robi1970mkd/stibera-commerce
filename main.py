
from flask import Flask, jsonify
from stibera_ai import StiberaAI
from pelister_ai import PelisterAI

app = Flask(__name__)
stibera = StiberaAI()
pelister = PelisterAI()

@app.route("/")
def home():
    return jsonify({"status": "Stibera Commerce AI System is Live"})

@app.route("/scan")
def scan_products():
    result = pelister.fetch_trending_products()
    return jsonify({"result": result})

@app.route("/check")
def ethical_check():
    result = stibera.check_ethics()
    return jsonify({"ethics": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
