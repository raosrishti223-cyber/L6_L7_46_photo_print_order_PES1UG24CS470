import pytest

from photo_print_order import (
    extra_print_charge,
    order_valid,
    dispatch_status
)


# =====================================
# 1. EXTRA PRINT CHARGE TEST CASES
# =====================================

def test_included_prints():
    assert extra_print_charge("4x6", 15, "matte", False) == 0


def test_extra_prints_matte():
    assert extra_print_charge("4x6", 25, "matte", False) == 20


def test_extra_prints_glossy():
    assert extra_print_charge("5x7", 20, "glossy", False) == 35


def test_member_discount():
    assert extra_print_charge("4x6", 26, "matte", True) == 4


def test_8x10_member():
    assert extra_print_charge("8x10", 15, "matte", True) == 20


def test_large_extra_prints():
    assert extra_print_charge("4x6", 75, "matte", False) == 330


def test_canvas_large_order():
    assert extra_print_charge("4x6", 75, "canvas", False) == 770


def test_canvas_small_order():
    assert extra_print_charge("4x6", 25, "canvas", False) == 35


def test_unknown_size():
    with pytest.raises(ValueError):
        extra_print_charge("10x12", 10, "matte", False)


def test_negative_copies():
    with pytest.raises(ValueError):
        extra_print_charge("4x6", -1, "matte", False)


def test_member_no_extra_prints():
    assert extra_print_charge("4x6", 25, "matte", True) == 0


def test_member_large_order():
    assert extra_print_charge("4x6", 80, "matte", True) == 330


# =====================================
# 2. ORDER VALIDITY TEST CASES
# =====================================

def test_normal_valid_order():
    assert order_valid(10, 100, False) is True


def test_rush_valid_order():
    assert order_valid(10, 40, True) is True


def test_rush_invalid_order():
    assert order_valid(10, 60, True) is False


def test_large_file():
    assert order_valid(30, 100, False) is False


def test_maximum_normal_order():
    assert order_valid(10, 500, False) is True


def test_exceeds_maximum_order():
    assert order_valid(10, 501, False) is False


def test_file_at_limit():
    assert order_valid(25, 100, False) is True


# =====================================
# 3. DISPATCH STATUS TEST CASES
# =====================================

def test_framed_on_time():
    assert dispatch_status(24, True, False) == "on_time"


def test_unframed_on_time():
    assert dispatch_status(12, False, False) == "on_time"


def test_international_on_time():
    assert dispatch_status(48, True, True) == "on_time"


def test_dispatch_tight():
    assert dispatch_status(20, True, False) == "tight"


def test_unframed_tight():
    assert dispatch_status(7, False, False) == "tight"


def test_international_tight():
    assert dispatch_status(42, True, True) == "tight"


def test_dispatch_missed():
    assert dispatch_status(10, True, False) == "missed"


def test_international_missed():
    assert dispatch_status(35, True, True) == "missed"