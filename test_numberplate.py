import plates


def test_length():
    assert plates.is_valid('a')==False
    assert plates.is_valid('Gowthami')==False
    assert plates.is_valid('hello')==True
    assert plates.is_valid('bye')==True


def test_alphabetical():
    assert plates.is_valid('0Queen')==False
    assert plates.is_valid('256hel')==False
    assert plates.is_valid('h2rooA')==False
    assert plates.is_valid('H0llo')==False
    assert plates.is_valid('hai')==True
    assert plates.is_valid('GO')==True
    assert plates.is_valid('72hello')==False
    assert plates.is_valid('459324')==False
    assert plates.is_valid('54uttr')==False


def test_specialchar():
    assert plates.is_valid('hello_1')==False
    assert plates.is_valid('azz@zz')==False
    assert plates.is_valid('$dol')==False


def test_numberchecking():
    assert plates.is_valid('AZZ034')==False
    assert plates.is_valid('HTR879')==True
    assert plates.is_valid('cs50')==True
    assert plates.is_valid('cs05')==False
    assert plates.is_valid('Gow590')==True
    assert plates.is_valid('cat340')==True
    assert plates.is_valid('hai72D')==False
    assert plates.is_valid(' hai ?')==False
