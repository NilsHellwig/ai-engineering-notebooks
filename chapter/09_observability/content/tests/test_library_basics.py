import pytest

from library import AlreadyCheckedOutError, Book, BookNotFoundError, Library, late_fee


def test_checkout_returns_the_book():
    library = Library()
    library.add(Book("978-0-13-468599-1", "The Pragmatic Programmer"))

    book = library.checkout("978-0-13-468599-1")

    assert book.title == "The Pragmatic Programmer"
    assert book.checked_out is True


def test_checkout_unknown_isbn_raises():
    library = Library()

    with pytest.raises(BookNotFoundError, match="978-0-00-000000-0"):
        library.checkout("978-0-00-000000-0")


def test_checkout_already_checked_out_raises():
    library = Library()
    library.add(Book("978-0-13-468599-1", "The Pragmatic Programmer"))
    library.checkout("978-0-13-468599-1")

    with pytest.raises(AlreadyCheckedOutError):
        library.checkout("978-0-13-468599-1")


def test_late_fee_uses_approx_for_the_float_result():
    # 7 days late at 0.20 EUR/day - comparing floats with == is fragile, pytest.approx isn't
    assert late_fee(7) == pytest.approx(1.4)


def test_no_fee_when_not_late():
    assert late_fee(0) == 0.0
    assert late_fee(-3) == 0.0
