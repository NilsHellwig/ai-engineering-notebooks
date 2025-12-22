import pytest

from library import Book, Library


@pytest.mark.demo_fail
def test_a_deliberately_wrong_assertion():
    library = Library()
    library.add(Book("978-0-13-468599-1", "The Pragmatic Programmer"))

    book = library.checkout("978-0-13-468599-1")

    # Deliberately wrong - the real title has no "2nd Edition" in it. This fails so you
    # can see a genuine assertion-rewrite diff in the terminal output below.
    assert book.title == "The Pragmatic Programmer, 2nd Edition"


@pytest.fixture
def broken_fixture():
    raise RuntimeError("Simulated: the database connection could not be established.")
    yield  # never reached


@pytest.mark.demo_fail
def test_uses_a_fixture_that_fails_during_setup(broken_fixture):
    # never reached - broken_fixture raises before this test body runs at all,
    # which is exactly why pytest reports this as an ERROR, not a FAILED
    assert True
