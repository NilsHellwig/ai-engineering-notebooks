import pytest

from library import is_library_open, late_fee


@pytest.mark.parametrize("hour", [8, 12, 21])
def test_library_is_open_during_business_hours(hour):
    assert is_library_open("Tuesday", hour) is True


@pytest.mark.parametrize("hour", [0, 7, 22, 23])
def test_library_is_closed_outside_business_hours(hour):
    assert is_library_open("Tuesday", hour) is False


@pytest.mark.parametrize(
    "day,hour,expected",
    [
        pytest.param("Sunday", 12, False, id="closed-on-sunday"),
        pytest.param("Monday", 9, True, id="open-monday-morning"),
        pytest.param("Saturday", 21, True, id="open-saturday-evening"),
    ],
)
def test_library_hours_by_day(day, hour, expected):
    assert is_library_open(day, hour) is expected


# Stacking two @parametrize decorators multiplies the cases: 3 days x 2 hours = 6 tests
@pytest.mark.parametrize("day", ["Monday", "Wednesday", "Friday"])
@pytest.mark.parametrize("hour", [10, 20])
def test_open_on_every_weekday_at_these_hours(day, hour):
    assert is_library_open(day, hour) is True


@pytest.mark.parametrize(
    "days_late,expected_fee",
    [
        (0, 0.0),
        (1, 0.20),
        pytest.param(-3, 0.0, id="negative-days-late-is-not-a-refund"),
    ],
)
def test_late_fee_parametrized(days_late, expected_fee):
    assert late_fee(days_late) == pytest.approx(expected_fee)
