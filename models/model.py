from pydantic import BaseModel

class Book(BaseModel):
    id_book : int
    title : str
    author : str
    city : str
