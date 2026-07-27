def test_stocked_library_fixture_comes_from_conftest(stocked_library):
    # `stocked_library` was never imported here - pytest found it in conftest.py automatically
    book = stocked_library.checkout("978-1-59327-584-6")
    assert book.title == "Python Crash Course"
