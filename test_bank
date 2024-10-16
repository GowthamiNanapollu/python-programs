from bank import value


def test_hello():
    assert value('Hello')==0
    assert value('hello Gowthami')==0
    assert value('Hello_Gowthaami')==0
    assert value('hello_world')==0


def test_h():
    assert value('hai gowthami')==20
    assert value('hey gowthami')==20
    assert value('happyto see you')==20


def test_other():
    assert value('what you need sir')==100
    assert value('what  can I do you sir')==100
    assert value("what'sabig dealsir")==100
