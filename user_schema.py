from pydantic import BaseModel, Field


class BookBody(BaseModel):
    title: str = Field(description="Title of the book.", examples=["The Hobbit"])
    author: str = Field(description="Author of the book.", examples=["J.R.R. Tolkien"])
    isbn: str = Field(description="Unique ISBN of the book.", examples=["9780547928227"])
    price: float = Field(description="Price in EUR.", examples=[19.99])
    stock_quantity: int = Field(description="Number of copies in stock.", examples=[5])


class Book(BookBody):
    id: int = Field(description="ID assigned by the server.", examples=[1])
