import requests

def search(title, limit=5):
    payload = {'title': title, 'limit': limit}
    r = requests.get('http://openlibrary.org/search.json', params=payload)
    if r.status_code != 200:
        return [], r.status_code
    response = r.json()
    return response['docs'], r.status_code

def cover(book, size="M"):
    if 'cover_i' not in book:
        return ''
    cover_id = book["cover_i"]
    size = size.upper()
    if size not in ("S", "M", "L"):
        raise Exception(f"invalid cover size {size}")
    return f"http://covers.openlibrary.org/b/id/{cover_id}-{size}.jpg"