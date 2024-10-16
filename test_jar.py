import pytest
from jar import Jar

def test_str():
    jar=Jar()
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪"
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar=Jar()
    with pytest.raises(ValueError):
        jar.deposit(-1)

def test_withdraw():
    jar=Jar()
    jar.deposit(5)
    with pytest.raises(ValueError):
        jar.withdraw(6)

def test_init():
    with pytest.raises(ValueError):
        jar=Jar(-1)



