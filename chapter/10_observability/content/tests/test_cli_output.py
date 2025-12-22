def notify_checkout(title: str) -> None:
    print(f"Checked out: {title}")


def test_capsys_captures_printed_output(capsys):
    notify_checkout("The Pragmatic Programmer")

    captured = capsys.readouterr()
    assert captured.out == "Checked out: The Pragmatic Programmer\n"
    assert captured.err == ""
