import requests

def search(title, limit=10):
    payload = {'title': title, 'limit': limit}
    r = requests.get('http://openlibrary.org/search.json', params=payload)
    if r.status_code != 200:
        return [], r.status_code
    response = r.json()
    # for book in books:
    #     book['cover'] = openlibrary.cover(book)
    #     authors = book['author_name'] #Open Library returns a list of authors
    #     book['author'] = ", ".join(authors) if authors else "Anonymous"
    #     book['isbn'] = book['isbn'][0] #Open Library returns a list of isbns
    #Add Open Library Search  books = response['docs'] ...svbs
    return response['docs'], r.status_code

def cover(book, size="M"):
    if 'cover_i' not in book:
        return ''
    cover_id = book["cover_i"]
    size = size.upper()
    if size not in ("S", "M", "L"):
        raise Exception(f"invalid cover size {size}")
    return f"http://covers.openlibrary.org/b/id/{cover_id}-{size}.jpg"