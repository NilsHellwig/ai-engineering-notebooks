import pytest

from library import Book, Library


@pytest.fixture
def stocked_library():
    """Shared with every test file in this folder - no import needed, pytest finds this automatically."""
    lib = Library()
    lib.add(Book("978-0-13-468599-1", "The Pragmatic Programmer"))
    lib.add(Book("978-1-59327-584-6", "Python Crash Course"))
    return lib
