class BookNotFoundError(Exception):
    """Raised when an ISBN isn't in the library's catalog."""


class AlreadyCheckedOutError(Exception):
    """Raised when trying to check out a book that's already checked out."""


class Book:
    def __init__(self, isbn: str, title: str):
        self.isbn = isbn
        self.title = title
        self.checked_out = False


class Library:
    def __init__(self):
        self._books: dict[str, Book] = {}

    def add(self, book: Book) -> None:
        self._books[book.isbn] = book

    def checkout(self, isbn: str) -> Book:
        book = self._books.get(isbn)
        if book is None:
            raise BookNotFoundError(f"No book with ISBN {isbn}")
        if book.checked_out:
            raise AlreadyCheckedOutError(f"{book.title} is already checked out")
        book.checked_out = True
        return book

    def return_book(self, isbn: str) -> None:
        book = self._books.get(isbn)
        if book is None:
            raise BookNotFoundError(f"No book with ISBN {isbn}")
        book.checked_out = False


def is_library_open(day: str, hour: int) -> bool:
    """The library is open Monday-Saturday, 8:00-22:00 (same hours as 10_2_langsmith.ipynb's FAQ)."""
    if day == "Sunday":
        return False
    return 8 <= hour < 22


def late_fee(days_late: int, daily_rate: float = 0.20) -> float:
    """0.20 EUR/day, same rate as 10_2_langsmith.ipynb's FAQ. No cap on the fee yet."""
    if days_late <= 0:
        return 0.0
    return round(days_late * daily_rate, 2)


def ask_librarian_llm(question: str) -> str:
    """Would call the course's Ollama server in a real app - see the monkeypatch section below."""
    import os

    import openai

    client = openai.OpenAI(base_url=f"http://{os.environ['LLM_HOST']}:11434/v1", api_key="ollama")
    response = client.chat.completions.create(
        model="gemma4:26b",
        messages=[{"role": "user", "content": question}],
    )
    return response.choices[0].message.content
