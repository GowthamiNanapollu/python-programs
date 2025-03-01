import pytest
from working import convert


def test_convert():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"


def test_convert_value_error():
    with pytest.raises(ValueError):
        convert("9:90 AM to 5:00 PM")


def test_value_error_to():
    with pytest.raises(ValueError):
        convert("10:20 AM 3:00 PM")
