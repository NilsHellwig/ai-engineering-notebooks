import json

from library import Book, Library


def export_catalog(library: Library, path) -> None:
    catalog = {isbn: book.title for isbn, book in library._books.items()}
    path.write_text(json.dumps(catalog))


def test_tmp_path_is_a_real_directory_on_disk(tmp_path):
    library = Library()
    library.add(Book("978-0-13-468599-1", "The Pragmatic Programmer"))

    backup_file = tmp_path / "catalog_backup.json"
    export_catalog(library, backup_file)

    assert backup_file.exists()
    assert json.loads(backup_file.read_text()) == {"978-0-13-468599-1": "The Pragmatic Programmer"}


def test_tmp_path_is_fresh_for_every_test(tmp_path):
    # a brand new, empty directory - nothing left over from the test above
    assert list(tmp_path.iterdir()) == []
