# Keylogger

## Overview
This project is a keylogger application that logs keystrokes from a client machine and sends them to a server for storage and retrieval. It includes a Flask-based server for log storage and retrieval, a client-side keylogger, and utility functions for managing client identifiers and communication.

## ⚠️ Warning

> ‼️‼️ ☠️ ‼️‼️ <strong> This project is intended for educational and ethical use only. It must not be used for unauthorized or malicious activities. The developers are not responsible for any misuse of this software. Ensure compliance with legal and ethical standards before deployment. </strong> 

## Components

### 1. Server (`app.py`)
The Flask server provides endpoints to log and retrieve data.

#### Endpoints:
- `GET /` - Serves an HTML page displaying the stored logs.
- `POST /log` - Receives log data from clients and stores it.

#### Dependencies:
- `Flask`
- `json`
- `os`
- `sys`
- `Pathlib`

#### Execution:
Run the server using:
```sh
python app.py
```
The server listens on `0.0.0.0:8080`.

### 2. Database Handler (`service/db.py`)
Handles reading and writing log data.

#### Functions:
- `read_logs(url='storage/logs.json')`: Reads log data from a JSON file.
- `write_logs(new_data, url='storage/logs.json')`: Writes new log data.
- `get_html_template()`: Generates an HTML interface to display logs.

### 3. Client Keylogger (`app_client.py`)
A client-side script that captures keyboard input and sends it to the server.

#### Key Features:
- Uses `pynput.keyboard` to listen for key presses.
- Simulates an installation process as a distraction.
- Sends logged keystrokes to the server.

#### Execution:
Run the client with:
```sh
python app_client.py
```

### 4. Utility Functions (`utils/utils.py`)
Helper functions for generating client IDs and sending data.

#### Functions:
- `create_id()`: Generates a unique client identifier.
- `send_to_server()`: Sends captured logs to the server.
- `print_log(key)`: Formats and logs keystrokes.

### Installation & Setup
#### Prerequisites
- Python 3.x
- Required libraries:
  ```sh
  pip install flask pynput requests
  ```

#### Running the Application
1. Start the Flask server:
   ```sh
   python app.py
   ```
2. Run the keylogger on the client machine:
   ```sh
   python app_client.py
   ```

### Security Considerations
This project logs keystrokes and transmits them to a remote server. Ensure compliance with legal and ethical standards before deployment.

