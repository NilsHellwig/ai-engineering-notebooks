import pytest

from library import Book, Library


@pytest.fixture
def library():
    """A fresh Library with one book already added - most tests here just want this."""
    lib = Library()
    lib.add(Book("978-0-13-468599-1", "The Pragmatic Programmer"))
    return lib


def test_fixture_gives_a_ready_to_use_library(library):
    assert library.checkout("978-0-13-468599-1").title == "The Pragmatic Programmer"


@pytest.fixture
def checked_out_library(library):
    """A fixture can request another fixture - this builds on `library` above."""
    library.checkout("978-0-13-468599-1")
    return library


def test_fixtures_can_build_on_other_fixtures(checked_out_library):
    assert checked_out_library._books["978-0-13-468599-1"].checked_out is True


@pytest.fixture
def tracked_resource():
    log = ["setup"]
    yield log
    log.append("teardown")  # runs only after the test using this fixture has returned


def test_yield_fixture_teardown_runs_after_the_test(tracked_resource):
    # only "setup" has happened so far - the "teardown" append above hasn't run yet,
    # since the code after `yield` only executes once this test function returns
    assert tracked_resource == ["setup"]


_module_setup_count = {"n": 0}


@pytest.fixture(scope="module")
def shared_catalog():
    """scope="module": built once, reused by every test in this file."""
    _module_setup_count["n"] += 1
    lib = Library()
    lib.add(Book("978-0-13-468599-1", "The Pragmatic Programmer"))
    lib.add(Book("978-1-59327-584-6", "Python Crash Course"))
    return lib


def test_module_scoped_fixture_first_use(shared_catalog):
    assert _module_setup_count["n"] == 1
    assert shared_catalog.checkout("978-1-59327-584-6").title == "Python Crash Course"


def test_module_scoped_fixture_is_reused_not_rebuilt(shared_catalog):
    # same fixture instance as the test above - setup only ran once for this whole file
    assert _module_setup_count["n"] == 1


_autouse_log = []


@pytest.fixture(autouse=True)
def record_test_start():
    """autouse=True: applied to every test in this file automatically, never requested by name."""
    _autouse_log.append("started")


def test_autouse_fixture_ran_without_being_requested():
    assert _autouse_log[-1] == "started"
