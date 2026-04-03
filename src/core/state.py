
import json

STATE_FILE = "state.json"


def load_state():
    try:
        with open(STATE_FILE, "r") as handle:
            return json.load(handle)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return None


def save_state(state):
    try:
        with open(STATE_FILE, "w") as handle:
            json.dump(state, handle)
    except Exception as e:
        print(f"Error saving state: {e}")
