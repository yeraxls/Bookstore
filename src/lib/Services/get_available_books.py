
from src.lib.Services.get_all_books import get_all_books
from src.models.book import book

def get_available_books():
    books_list = get_all_books()
    return [i for i in books_list if i.stock > 0]
