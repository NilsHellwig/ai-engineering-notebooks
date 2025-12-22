"""A small MCP server for a (fictional) university library catalog.

MCP (Model Context Protocol) servers expose "tools" - regular Python functions -
over a standardized protocol, so any MCP-compatible client (an app, a notebook,
an LLM agent, ...) can discover and call them, without needing to import this
file directly. This is the same idea as passing a Python function as a tool to
an LLM (see the previous notebook), just decoupled into its own process.

We use the `fastmcp` library, which turns a decorated function into an MCP tool
automatically - reading the type hints for the parameter types, and the
docstring for the tool description, exactly like the `ollama` package did for
local tools in the previous notebook.

This file is not meant to be run interactively in a terminal - see 06_1_mcp.ipynb
for how a client starts and talks to it.
"""

from fastmcp import FastMCP

from dummy import AUTHORS, BOOKS, MEMBERS

mcp = FastMCP("University Library")


def _author_name(author_id: int) -> str:
    """Look up an author's name by id (internal helper, not a tool)."""
    for author in AUTHORS:
        if author["author_id"] == author_id:
            return author["name"]
    return "Unknown author"


def _member_name(member_id: int) -> str:
    """Look up a member's name by id (internal helper, not a tool)."""
    for member in MEMBERS:
        if member["member_id"] == member_id:
            return member["name"]
    return "Unknown member"


@mcp.tool()
def search_books(query: str) -> list[dict]:
    """Search the library catalog by title, subject, or author name.

    Args:
        query: A search term to match against title, subject, or author name (case-insensitive).

    Returns:
        A list of matching books, each with isbn, title, author, subject, year, and availability.
    """
    query_lower = query.lower()
    results = []
    for book in BOOKS:
        author_name = _author_name(book["author_id"])
        if (
            query_lower in book["title"].lower()
            or query_lower in book["subject"].lower()
            or query_lower in author_name.lower()
        ):
            results.append({
                "isbn": book["isbn"],
                "title": book["title"],
                "author": author_name,
                "subject": book["subject"],
                "year": book["year"],
                "available": book["available"],
            })
    return results


@mcp.tool()
def get_book_details(isbn: str) -> dict:
    """Get the full catalog entry for a book by its ISBN, including who currently has it if it's checked out.

    Args:
        isbn: The ISBN of the book.

    Returns:
        The book's full details, or an error message if the ISBN is not found.
    """
    for book in BOOKS:
        if book["isbn"] == isbn:
            details = {
                "isbn": book["isbn"],
                "title": book["title"],
                "author": _author_name(book["author_id"]),
                "subject": book["subject"],
                "year": book["year"],
                "available": book["available"],
            }
            if not book["available"]:
                details["borrowed_by"] = _member_name(book["borrowed_by"])
                details["due_date"] = book["due_date"]
            return details
    return {"error": f"No book found with ISBN {isbn}"}


@mcp.tool()
def get_author_books(author_name: str) -> list[dict]:
    """Get all books by a given author.

    Args:
        author_name: The author's name (or part of it, case-insensitive).

    Returns:
        A list of books by matching authors, each with isbn, title, and year.
    """
    query_lower = author_name.lower()
    matching_author_ids = {
        author["author_id"] for author in AUTHORS if query_lower in author["name"].lower()
    }
    return [
        {"isbn": book["isbn"], "title": book["title"], "year": book["year"]}
        for book in BOOKS
        if book["author_id"] in matching_author_ids
    ]


@mcp.tool()
def checkout_book(isbn: str, member_name: str) -> str:
    """Check out a book to a library member. Unlike the tools above, this one
    changes the catalog - only call it once the user has actually confirmed
    they want to borrow the book.

    Args:
        isbn: The ISBN of the book to check out.
        member_name: The name of the member borrowing the book (must be an existing member).

    Returns:
        A confirmation message, or an error if the book/member can't be found or the book is already checked out.
    """
    member = next((m for m in MEMBERS if m["name"].lower() == member_name.lower()), None)
    if member is None:
        return f"No member found named '{member_name}'."

    for book in BOOKS:
        if book["isbn"] == isbn:
            if not book["available"]:
                return f"'{book['title']}' is already checked out."
            book["available"] = False
            book["borrowed_by"] = member["member_id"]
            book["due_date"] = "2026-09-01"
            return f"'{book['title']}' has been checked out to {member['name']}, due {book['due_date']}."
    return f"No book found with ISBN {isbn}."


# Tools are for actions. A Resource is different: it exposes read-only data at a
# fixed address (a "URI"), similar to a file path or a database record - there
# are no arguments to fill in, a client just fetches whatever is there.
@mcp.resource("library://catalog")
def get_catalog() -> list[dict]:
    """The full library catalog, with author names already resolved."""
    return [
        {"isbn": book["isbn"], "title": book["title"], "author": _author_name(book["author_id"])}
        for book in BOOKS
    ]


# A Prompt is the third MCP primitive: a reusable, parameterized prompt template
# that lives on the server, so multiple clients can share the same well-tested
# wording instead of everyone writing their own.
@mcp.prompt()
def recommend_book(subject: str) -> str:
    """Generate a prompt asking for a book recommendation in a given subject."""
    return f"Recommend one book about {subject} from the library catalog, and briefly say why."


if __name__ == "__main__":
    # "stdio" transport means: talk to whichever client launched this script as a
    # subprocess, via standard input/output. See 06_1_mcp.ipynb for how that client
    # side works, and what other transports (e.g. "http") are for.
    mcp.run(transport="stdio", show_banner=False)
