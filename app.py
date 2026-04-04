from src.core.state import load_state, save_state
from src.api.client import fetch_items

def main():
    state = load_state()
    if state is None:
        state = {}
    items = fetch_items()
    total = sum(item.get('value', 0) for item in items)
    state['total'] = total
    save_state(state)
    print('done', total)

if __name__ == '__main__':
    main()