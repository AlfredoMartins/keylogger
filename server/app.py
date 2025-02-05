from flask import Flask, Response, request
from service.db import read_logs, get_html_template, write_logs
import json, os, sys

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

BASE_URL = "https://codetyperpro.pythonanywhere.com"

if __name__ == "__main__":
    BASE_URL = "0.0.0.0"
    app.run(host=BASE_URL, port=5000)