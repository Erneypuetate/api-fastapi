from pymongo.mongo_client import MongoClient 

uri='mongodb://root:example@localhost:27017'

conn=MongoClient(uri)

def exists_book(book):
    cursor = conn.erney.books.count_documents(book)
    if cursor > 0:
        return True
    else:
        return False



