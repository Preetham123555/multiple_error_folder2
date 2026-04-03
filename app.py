
from src.core.state import load_state, save_state
from src.api.client import fetch_items


def main():
    state = load_state()
    if state is None:
        state = {}
    if not isinstance(state, dict):
        state = {}
    items = fetch_items()
    total = 0
    for item in items:
        total = total + item.get("value", 0)
    if "total" not in state:
        state["total"] = total
    else:
        state["total"] = total
    save_state(state)
    print("done", total)


if __name__ == "__main__":
    main()
