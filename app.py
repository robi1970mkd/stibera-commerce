
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    return f"Shopify secret is: {os.getenv('SHOPIFY_APP_SECRET', 'Not set')}"

if __name__ == '__main__':
    app.run()
