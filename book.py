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
    published_year : int

    def __init__(self, id, title, author, description, rating, published_year):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_year = published_year
    
class BookRequest(BaseModel):
    id : Optional[int] = None
    title : str = Field(min_length=3)
    author : str
    description : str
    rating : int = Field(lt=11, gt=0)
    published_year : int 

    # model_config = {
    #     "json_schema_extra": {
    #         "example" : {
    #             "title" : "Book Title goes here",
    #             "author" : "Author Name goes here",
    #             "description" : "Description of book goes here",
    #             "rating" : "Enter a value between 0 and 10"
    #         }
    #     }
    # }

books = [
        Book(1, "Meditations", "Marcus Aurelius", "great read!", 10, 1900),
        Book(2, "Letters from a Stoic", "Seneca", "new perspectives unlocked!", 8, 2000),
        Book(3, "Selected Discourses", "Epictetus", "awesome", 9, 1890),
        Book(4, "Deep Work", "Unknown", "really helpful", 9, 2015),
        Book(5, "Can't hurt me", "David Goggins", "not my type", 4, 2018)
        ]

@app.get("/books")
def get_all_books():
    return books

@app.get("/books/")
def get_book_by_rating(rating : int):
    res = []
    for book in books:
        if rating == book.rating:
            res.append(book)
    return res
            

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

@app.put("/books/update_book")
def update_book(updated_book : BookRequest):
    for i in range(len(books)):
        if books[i].id == updated_book.id:
            books[i] = updated_book

@app.delete("/books/delete_book")
def delete_book(id : int):
    for i in range(len(books)):
        if id == books[i].id:
            del books[i]
            break

@app.get("/books/{published_year}")
def get_books_by_published_year(published_year : int):
    res = []
    for book in books:
        if published_year == book.published_year:
            res.append(book)
    return res
