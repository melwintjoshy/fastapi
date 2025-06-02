from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional
app = FastAPI()

class Book:
    id : int
    title : str
    author : str
    description : str
    rating : int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
    
class BookRequest(BaseModel):
    id : Optional[int] = None
    title : str = Field(min_length=3)
    author : str
    description : str
    rating : int = Field(lt=11, gt=0)

books = [
        Book(1, "Meditations", "Marcus Aurelius", "great read!", 10),
        Book(2, "Letters from a Stoic", "Seneca", "new perspectives unlocked!", 8),
        Book(3, "Selected Discourses", "Epictetus", "awesome", 9),
        Book(4, "Deep Work", "Unknown", "really helpful", 9),
        Book(5, "Can't hurt me", "David Goggins", "not my type", 4)
        ]

@app.get("/books")
def get_all_books():
    return books

@app.post("/books/create_new_book")
def create_new_book(book_request : BookRequest):
    new_book = Book(**book_request.model_dump())
    books.append(find_id(new_book))

def find_id(book: Book):
    if len(books) > 0:
        book.id = books[-1].id + 1
    else:
        book.id = 1
    return book
