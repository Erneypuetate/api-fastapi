from pymongo.mongo_client import MongoClient 

uri='mongodb://root:example@localhost:27017'

conn=MongoClient(uri)

def exists_book(book):
    cursor = conn.erney.books.count_documents({"id_book" : book['id_book']})
    print(cursor)
    if cursor > 0:
        return True
    else:
        return False

def findBook(book)-> dict:
    book={'id_book':book['id_book'],
        'title': book['title'],
        'author' : book['author'],
        'city' : book['city']
        }
    return book

def findBooks(books)-> list:
    list_books=[]
    for book in books:
        list_books.append(findBook(book))

    return list_books






