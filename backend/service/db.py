url = 'storage/logs.txt'

def read_logs():
    output = []
    
    try:
        with open(url, 'r') as file:
            for line in file:
                output.append(line.strip())
    
    except FileNotFoundError:
        print(f"Error: The file '{url}' was not found.")
        return "Error: Log file not found."
    except IOError:
        print(f"Error: Could not read the file '{url}'.")
        return "Error: Unable to read log file."
    
    return "\n".join(output)

def write_logs(data):
    try:
        with open(url, 'a') as file:
            file.write(data + "\n")
    except IOError:
        print(f"Error: Could not write to the file '{url}'.")


def get_html_template(data):
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
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🔐 Keylogger Logs</h1>
            <pre>{data}</pre>
        </div>
    </body>
    </html>"""
        
    return html_content