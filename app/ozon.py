def create_book(title, author, price, availability, tags):
    return {
    'title': title,
    'author': author,
    'price': price,
    'available': availability,
    'tags': tags,
    }

def add_book(container, book):
    container.append(book)


# def list_books(container, page, page_size):
#     # page_size = 50
#     start = (page - 1) # для первой страницы стартуем с нуля
#     finish = start + page_size
#     return container[start:finish]

def search_books(container, search): # search - это строка поиска
    search_lowercased = search.strip().lower() #1. search.strip() 2. (результат search.strip вызывается для .lower)
    result = []
    for book in container:
        if search_lowercased in book['title'].lower():
            result.append(book)
            continue # не дает идти дальше на 28 строку

        if search_lowercased in book['author'].lower():
            result.append(book)
            continue

        if search_lowercased in book['tags'].lower():
            result.append(book)
            continue # сейчас она не нужна, но может пригодиться если будем добавлять новое условие
    return result

