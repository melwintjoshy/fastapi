from fastapi import Body, FastAPI

app = FastAPI()

books =[{"id": 1, "title" : "Meditations", "author" : "Marcus Aurelius", "rating": 10},
        {"id": 2, "title" : "Obstacle is the way", "author" : "Ryan Holiday", "rating": 8},
        {"id": 3, "title" : "The Daily Stoic", "author" : "Ryan Holiday", "rating": 9},
        {"id": 4, "title" : "Persistence", "author" : "Ryan Holiday", "rating": 7}]

@app.get("/books")
def get_all_books():
    return books

@app.get("/books/{id}")
def say(id):
    for book in books:
        if id in book:
            return book

# @app.get("/books/{author}")
# def read_author_by_path_parameter(author: str):
#     res = []
#     for book in books:
#         if book.get("author").casefold() == author.casefold():
#             res.append(book)
#     return res

       
@app.get("/books/")
def read_author_by_query(author: str):
    books_by_author = []
    for book in books:
        if book.get("author").casefold() == author.casefold():
            books_by_author.append(book)
    return books_by_author   

@app.get("/books/{author}/")
def read_author_by_pathparam_rating_by_query(author: str, rating : int):
    res = []
    for book in books:
        if book.get("author").casefold() == author.casefold() and int(book.get("rating")) == rating:
            res.append(book)
    return res

@app.post("/books/create_new_book")
def create(new_book = Body()):
    books.append(new_book)

@app.put("/books/update_book")
def update_book(updated_book = Body()):
    for i in range(len(books)):
        if updated_book.get("id") == books[i].get("id"):
            books[i] = updated_book

@app.delete("/books/delete_book/{id}")
def delete_book(id : int):
    for i in range(len(books)):
        if id == books[i].get("id"):
            del books[i]
            break