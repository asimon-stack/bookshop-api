from pydantic import BaseModel, Field


class BookCreate(BaseModel):
    """Model for creating a new book."""

    title: str = Field(
        description="The title of the book.",
        examples=["The Hobbit"],
        min_length=1
    )

    author: str = Field(
        description="The author of the book.",
        examples=["J.R.R. Tolkien"],
        min_length=1
    )

    isbn: str = Field(
        description="The unique ISBN of the book.",
        examples=["9780547928227"],
        min_length=10,
        max_length=13
    )

    genre: str = Field(
        description="The genre or category of the book.",
        examples=["Fantasy"],
        min_length=1
    )

    publisher: str = Field(
        description="The publisher of the book.",
        examples=["HarperCollins"],
        min_length=1
    )

    publication_year: int = Field(
        description="The year in which the book was published.",
        examples=[1937],
        ge=1
    )

    price: float = Field(
        description="The selling price of the book in EUR.",
        examples=[19.99],
        ge=0
    )

    stock_quantity: int = Field(
        description="The number of copies currently available in stock.",
        examples=[5],
        ge=0
    )


class Book(BookCreate):
    """Model representing a complete book record."""

    id: int = Field(
        description="The unique identifier assigned to the book.",
        examples=[1]
    )


class BookUpdate(BaseModel):
    """Model for partially updating a book."""

    title: str | None = Field(default=None, description="Updated book title.")
    author: str | None = Field(default=None, description="Updated author.")
    isbn: str | None = Field(default=None, description="Updated unique ISBN.")
    genre: str | None = Field(default=None, description="Updated book genre.")
    publisher: str | None = Field(default=None, description="Updated publisher.")
    publication_year: int | None = Field(default=None, description="Updated publication year.")
    price: float | None = Field(default=None, description="Updated price in EUR.")
    stock_quantity: int | None = Field(default=None, description="Updated stock quantity.")
