from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/health")
def health():
    return jsonify(status="ok")

@app.route("/metrics")
def metrics():
    return "my_app_requests_total 42\n"