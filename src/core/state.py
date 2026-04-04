import json
STATE_FILE = 'state.json'
def load_state():
    try:
        with open(STATE_FILE, 'r') as handle:
            return json.loads(handle.read())
    except Exception:
        return {}
def save_state(state):
    payload = json.dumps(state)
    with open(STATE_FILE, 'w') as handle:
        handle.write(payload)