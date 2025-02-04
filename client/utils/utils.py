import uuid
import json
import os

def get_id():
    username = os.getenv("USER") or os.getenv("USERNAME") or "unknown_user"
    username = username.replace(' ', '_')
    id_part = uuid.uuid1().hex[:4]
    return f'{username}_{id_part}'

def create_id():
    url = 'storage/info.json'
    
    os.makedirs(os.path.dirname(url), exist_ok=True)

    try:
        with open(url, 'r+') as file:
            try:
                data = json.load(file)
                if 'id' in data:
                    return data['id']
            except json.JSONDecodeError:
                pass
    except FileNotFoundError:
        pass
    
    new_id = get_id()
    with open(url, 'w') as file:
        json.dump({"id": new_id}, file, indent=4)

    return new_id