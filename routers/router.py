from fastapi import APIRouter
from config.mongo_db import conn, exists_book
from models.model import Book

router=APIRouter()




@router.get("/books")
async def find_books():
    try:
        conn.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
    return {"Hello": "these are all books"}


@router.get("/books/book/{id}")
async def find_book():
    return {"Hello": "this is one book"}

@router.post("/create-book")
async def create_book(book: Book):
    book=dict(book)
    print(book)
   
    if not exists_book(book):
        try:
            conn.erney.books.insert_one(**book)
            print("book inserted corrently")
            return book
        except Exception as e:
            print(e)
            return "error inserting book"
    else:
        return "the book already exists"


@router.put("/books/book/update/{id}")
async def update_book():
    return {"Hello": "book update"}


@router.delete("/books/book/delete/{id}")
async def read_root():
    return {"Hello": "book delete"}



