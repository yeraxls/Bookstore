from fastapi import APIRouter

from src.lib.Services.get_all_books import get_all_books
from src.lib.Services.get_available_books import get_available_books


router = APIRouter(prefix="/books", tags=["books"], responses={404: {"message":"no encontrado¡"}})

@router.get('/books/get-all')
def getallbooks():
    return get_all_books()
@router.get('/books/get-available')
def getavailablebooks():
    return get_available_books()