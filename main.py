from fastapi import APIRouter, FastAPI, HTTPException
from user_schema import BookBody, Book

app = FastAPI(
    title="Bookshop Catalog",
    version="0.1.0",
    description="REST-API für die Ressource Book. Eine Version: `/api/v1`. Speicher ist ein Dictionary.",
)

router = APIRouter(prefix="/api/v1", tags=["Books"])


books: dict[int, Book] = {
    1: Book(id=1, title="The Hobbit", author="J.R.R. Tolkien", isbn="9780547928227", price=19.99, stock_quantity=5),
    2: Book(id=2, title="1984", author="George Orwell", isbn="9780451524935", price=12.50, stock_quantity=8),
    3: Book(id=3, title="Dune", author="Frank Herbert", isbn="9780441172719", price=18.90, stock_quantity=6),
}
next_id = 4


@router.post("/books", status_code=201, summary="Book anlegen")
def create_book(body: BookBody) -> Book:
    """Legt ein Buch an.

    Die Id vergibt der Server. Der Body trägt die Buchdaten.

    ```json
    {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "isbn": "9780141439518",
        "price": 14.90,
        "stock_quantity": 3
    }
    ```

    Antwort **201**: Das angelegte Buch mit Id.
    """
    global next_id

    for book in books.values():
        if book.isbn == body.isbn:
            raise HTTPException(status_code=409, detail="ISBN already exists")

    book = Book(id=next_id, **body.model_dump())
    books[book.id] = book
    next_id += 1
    return book


@router.get("/books", summary="Alle Books lesen")
def list_books() -> list[Book]:
    """Liest alle Bücher.

    Antwort **200**, eine Liste von Büchern.
    """
    return list(books.values())


@router.get("/books/isbn/{isbn}", summary="Book über ISBN lesen")
def read_book_by_isbn(isbn: str) -> Book:
    """Sucht ein Buch über seine ISBN.

    Die ISBN steht im Pfad.

    Antwort **200**: Das gefundene Buch.
    """
    for book in books.values():
        if book.isbn == isbn:
            return book

    raise HTTPException(status_code=404, detail="Book not found")


@router.get("/books/{book_id}", summary="Einen Book lesen")
def read_book(book_id: int) -> Book:
    """Liest ein Buch. Die Id steht im Pfad.

    Antwort **200**: Das gefundene Buch.
    """
    if book_id in books:
        return books[book_id]
    else:
        raise HTTPException(status_code=404, detail="Book not found")


@router.put("/books/{book_id}", summary="Book ersetzen")
def replace_book(book_id: int, body: BookBody) -> Book:
    """Ersetzt den Eintrag. Die Id bleibt die aus dem Pfad.

    Der Body trägt alle Buchdaten.

    Antwort **200**: Das ersetzte Buch.
    """
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")

    for book in books.values():
        if book.isbn == body.isbn and book.id != book_id:
            raise HTTPException(status_code=409, detail="ISBN already exists")

    current = books[book_id]
    book = Book(id=current.id, **body.model_dump())
    books[book_id] = book
    return book


@router.delete("/books/{book_id}", status_code=204, summary="Book löschen")
def delete_book(book_id: int) -> None:
    """Entfernt das Buch. Die Id steht im Pfad.

    Antwort **204**. Kein Body.
    """
    del books[book_id]


app.include_router(router)