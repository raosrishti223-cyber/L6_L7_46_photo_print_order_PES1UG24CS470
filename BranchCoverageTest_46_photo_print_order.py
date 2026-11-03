import pytest

from photo_print_order import (
    extra_print_charge,
    order_valid,
    dispatch_status
)


# Extra print charge: branch tests

def test_unknown_print_size():
    with pytest.raises(ValueError):
        extra_print_charge("10x12", 10, "matte", False)


def test_negative_copies():
    with pytest.raises(ValueError):
        extra_print_charge("4x6", -5, "matte", False)


def test_non_member():
    assert extra_print_charge("4x6", 25, "matte", False) == 20


def test_member():
    assert extra_print_charge("4x6", 26, "matte", True) == 4


def test_member_8x10():
    assert extra_print_charge("8x10", 15, "matte", True) == 20


def test_no_extra_prints():
    assert extra_print_charge("4x6", 15, "matte", False) == 0


def test_matte_finish():
    assert extra_print_charge("4x6", 25, "matte", False) == 20


def test_other_finish():
    assert extra_print_charge("4x6", 25, "glossy", False) == 35


def test_extra_not_above_50():
    assert extra_print_charge("4x6", 70, "matte", False) == 200


def test_extra_above_50_matte():
    assert extra_print_charge("4x6", 75, "matte", False) == 330


def test_extra_above_50_canvas():
    assert extra_print_charge("4x6", 75, "canvas", False) == 770


# Order validity: branch tests

def test_rush_order_valid():
    assert order_valid(10, 50, True) is True


def test_rush_order_invalid():
    assert order_valid(10, 51, True) is False


def test_non_rush_large_file():
    assert order_valid(30, 100, False) is False


def test_non_rush_small_file():
    assert order_valid(10, 100, False) is True


def test_non_rush_maximum_copies():
    assert order_valid(10, 500, False) is True


def test_non_rush_exceeds_maximum():
    assert order_valid(10, 501, False) is False


# Dispatch status: branch tests

def test_framed_on_time():
    assert dispatch_status(24, True, False) == "on_time"


def test_unframed_on_time():
    assert dispatch_status(12, False, False) == "on_time"


def test_international_on_time():
    assert dispatch_status(48, True, True) == "on_time"


def test_domestic_tight():
    assert dispatch_status(18, True, False) == "tight"


def test_international_tight():
    assert dispatch_status(42, True, True) == "tight"


def test_dispatch_missed():
    assert dispatch_status(10, True, False) == "missed"


def test_unframed_international():
    assert dispatch_status(36, False, True) == "on_time"