from flask import Flask, jsonify
from pelister_ai import PelisterAI
from stibera_ai import StiberaAI

app = Flask(__name__)
pelister = PelisterAI()
stibera = StiberaAI()

@app.route('/')
def home():
    return "StiberaCommerce AI system is running."

@app.route('/run')
def run_ai():
    trending = pelister.fetch_trending_products()
    result = stibera.publish_products(trending)
    return jsonify(result)

@app.route('/health')
def health():
    return jsonify(status="ok")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)