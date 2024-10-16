from numb3rs import validate

def test_negativenums():
    assert validate("-2.-2.122.-122") == False
    assert validate("1.22.33.-122") == False


def test_greaternums():
    assert validate("276.234.453.232") == False
    assert validate("112.3.2.2") == True
    assert validate("212.345.265.295") == False


