import os

import library


def test_ask_librarian_without_hitting_the_real_ollama_server(monkeypatch):
    def fake_ask_librarian_llm(question: str) -> str:
        return "The library is open Monday-Saturday, 8:00-22:00."

    monkeypatch.setattr(library, "ask_librarian_llm", fake_ask_librarian_llm)

    answer = library.ask_librarian_llm("What are the library's opening hours?")

    assert "Monday-Saturday" in answer


def test_monkeypatch_setenv_is_automatically_undone(monkeypatch):
    monkeypatch.setenv("LLM_HOST", "203.0.113.42")
    assert os.environ["LLM_HOST"] == "203.0.113.42"
    # no explicit cleanup needed - monkeypatch restores the original value (or unsets
    # the variable entirely, if it wasn't set before) the moment this test returns
