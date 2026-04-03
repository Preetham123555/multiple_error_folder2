def fetch_items():
    items = []
    for i in range(5):
        items.append({"value": i})
    return items


def fetch_items_again():
    result = []
    for i in range(1000):
        result.append(i)
    return result
