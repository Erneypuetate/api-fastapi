from fastapi import APIRouter
from config.mongo_db import conn, exists_book, findBook, findBooks
from models.model import Book

router=APIRouter()




@router.get("/books")
async def find_books():
    try:
        books=conn.erney.books.find()
        listBooks=findBooks(books)
        return listBooks
    except Exception as e:
        print(e)
        return {"Hello": "these are all books"}


@router.get("/books/book/{id_book}")
async def find_book(id_book:int):
    print(id_book)
    try:
        book=conn.erney.books.find_one({'id_book':id_book})
        
        return findBook(book)
    except Exception as e:
        print(e)
        return {"Hello": "this is one book"}

@router.post("/create-book")
async def create_book(book: Book):
    new_book=dict(book)
   
    if not exists_book(new_book):
        try:
            print(type(new_book))
            conn.erney.books.insert_one(new_book)
            print("book inserted corrently")
            return book
        except Exception as e:
            print(e)
            return "error inserting book"
    else:
        return "the book already exists"



@router.put("/books/book/{id_book}")
async def update_book(id_book: int, updated_book: Book):
    try:
        book = conn.erney.books.find_one({'id_book': id_book})
        
        
        if not book:
            return 'book not find'

        result = conn.erney.books.update_one(
            {'id_book': id_book},
            {'$set': updated_book.dict()}
        )

        # Verificar si se actualizó correctamente
        if result.modified_count == 1:
            # Devolver el libro actualizado
            return {"message": "Book updated successfully"}
        else:
            # Si no se modificó ningún registro, devolver un error 500
            return 'not update'
    except Exception as e:
        print(e)
        # Si ocurre un error, devolver un error 500
        return 'error'



@router.delete("/books/book/{id_book}")
async def delete_book(id_book: int):
    try:
        
        book = conn.erney.books.find_one({'id_book': id_book})
        
        if book:
            conn.erney.books.delete_one({'id_book': id_book})
            return {"message": "Book deleted successfully"}
        else:
            return {'massage':'book not exists'}
    except Exception as e:
        print(e)
        return {'delete':'successful'}




