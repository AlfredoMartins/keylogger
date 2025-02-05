from flask import Flask, Response, request
from service.db import read_logs, get_html_template, write_logs
import json, os, sys
from pathlib import Path

app = Flask(__name__)

@app.route("/")
def index():
    read_logs()
    return Response(get_html_template(), content_type="text/html")

@app.route('/log', methods=["POST"])
def add_log():
    data = request.get_json()
    if not data:
        return "Bad Request: Missing 'log_data'", 400
    
    write_logs(data)
    return "Success", 201

if __name__ == "__main__":
    # Listen on all available interfaces (0.0.0.0) and a specific port (8080)
    app.run(host="0.0.0.0", port=8080)