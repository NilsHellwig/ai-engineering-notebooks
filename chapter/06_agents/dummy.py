"""Dummy data for the university library MCP server.

This is a small, made-up dataset with three related entities, similar to tables
in a database:

- AUTHORS:  one row per author
- MEMBERS:  one row per library member (a student or staff member who can borrow books)
- BOOKS:    one row per book, referencing an author via "author_id" and, if
            currently checked out, a member via "borrowed_by"
"""

AUTHORS = [
    {"author_id": 1, "name": "Thomas H. Cormen", "birth_year": 1956, "nationality": "American"},
    {"author_id": 2, "name": "Stuart Russell", "birth_year": 1962, "nationality": "British"},
    {"author_id": 3, "name": "Lisa A. Urry", "birth_year": 1961, "nationality": "American"},
    {"author_id": 4, "name": "David J. Griffiths", "birth_year": 1942, "nationality": "American"},
    {"author_id": 5, "name": "Sheldon Axler", "birth_year": 1949, "nationality": "American"},
    {"author_id": 6, "name": "Ian Goodfellow", "birth_year": 1985, "nationality": "American"},
]

MEMBERS = [
    {"member_id": 1, "name": "Anna Fischer", "department": "Computer Science", "member_since": 2023},
    {"member_id": 2, "name": "Ben Weber", "department": "Physics", "member_since": 2022},
    {"member_id": 3, "name": "Clara Schmidt", "department": "Biology", "member_since": 2024},
    {"member_id": 4, "name": "David Wagner", "department": "Mathematics", "member_since": 2021},
]

BOOKS = [
    {
        "isbn": "978-0-262-03384-8",
        "title": "Introduction to Algorithms",
        "author_id": 1,
        "subject": "Computer Science",
        "year": 2009,
        "available": True,
        "borrowed_by": None,
        "due_date": None,
    },
    {
        "isbn": "978-0-13-468599-1",
        "title": "Artificial Intelligence: A Modern Approach",
        "author_id": 2,
        "subject": "Computer Science",
        "year": 2020,
        "available": False,
        "borrowed_by": 1,
        "due_date": "2026-08-14",
    },
    {
        "isbn": "978-0-321-97362-8",
        "title": "Campbell Biology",
        "author_id": 3,
        "subject": "Biology",
        "year": 2016,
        "available": True,
        "borrowed_by": None,
        "due_date": None,
    },
    {
        "isbn": "978-0-8153-4432-2",
        "title": "Molecular Biology of the Cell",
        "author_id": 3,
        "subject": "Biology",
        "year": 2014,
        "available": False,
        "borrowed_by": 3,
        "due_date": "2026-08-02",
    },
    {
        "isbn": "978-0-13-035399-3",
        "title": "Introduction to Electrodynamics",
        "author_id": 4,
        "subject": "Physics",
        "year": 2017,
        "available": True,
        "borrowed_by": None,
        "due_date": None,
    },
    {
        "isbn": "978-1-4704-3568-9",
        "title": "Linear Algebra Done Right",
        "author_id": 5,
        "subject": "Mathematics",
        "year": 2015,
        "available": False,
        "borrowed_by": 4,
        "due_date": "2026-07-30",
    },
    {
        "isbn": "978-0-262-04616-9",
        "title": "Deep Learning",
        "author_id": 6,
        "subject": "Computer Science",
        "year": 2016,
        "available": True,
        "borrowed_by": None,
        "due_date": None,
    },
]
