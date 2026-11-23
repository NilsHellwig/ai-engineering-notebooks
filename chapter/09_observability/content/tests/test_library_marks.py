import sys

import pytest

from library import late_fee


@pytest.mark.skip(reason="Multi-branch libraries aren't modeled yet - tracked as a future feature.")
def test_transferring_a_book_between_branches():
    ...


@pytest.mark.skipif(sys.version_info >= (3, 0), reason="demo: always true on Python 3, so this always skips")
def test_something_that_only_ever_ran_on_python_2():
    assert True


@pytest.mark.xfail(reason="fee cap at 5 EUR hasn't been implemented yet")
def test_late_fee_is_capped_at_five_euros():
    assert late_fee(100) == pytest.approx(5.0)


@pytest.mark.slow
def test_a_slower_integration_style_check():
    # Marked @pytest.mark.slow, a custom marker registered in content/pytest.ini,
    # so a quick local run can skip it with `-m "not slow"` while CI still runs it.
    catalog = {str(isbn): isbn % 2 == 0 for isbn in range(2000)}
    assert len(catalog) == 2000
