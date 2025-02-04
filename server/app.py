from flask import Flask, Response, request
from service.db import read_logs, get_html_template, write_logs

app = Flask(__name__)

@app.route("/")
def index():
    log_data = read_logs()
    return Response(get_html_template(log_data), content_type="text/html")

@app.route('/log', methods=["POST"])
def add_log():
    data = request.json.get('log_data')
    if not data:
        return "Bad Request: Missing 'log_data'", 400
    
    write_logs(data)
    return "Success", 201

if __name__ == "__main__":
    app.run(port=5000)