from src.lib.managedb import ManageDb
from src.models.book import book


def get_all_books():
    md = ManageDb()
    books = md.read_books()
    list = [] 
    for bookdb in books:
        list.append( book(bookdb["id"], bookdb["name"], bookdb["stock"]) )
    return list
