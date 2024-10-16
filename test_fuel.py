import pytest
import fuel

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        fuel.convert('1/0')
        pytest.skip(input("fraction"))



def test_convert_value_error_handling():
        with pytest.raises(ValueError):
            fuel.convert('5/2')
            pytest.skip(input("fraction"))


def test_convert():
    assert fuel.convert('1/3')==33



def test_gauge():
    assert fuel.gauge(99)=='F'
    assert fuel.gauge(1)=="E"
    assert fuel.gauge(67)==67
