from um import count


def test_um_lower():
    assert count("um? yummy um..") == 2
    assert count("Um..") == 1



def test_um_upper():
    assert count("Um, thanks for the album, Um, thanks, um...") == 3
    assert count("UM.. uM") == 2


def test_um_count():
    assert count("hello yummy") == 0
    assert count("hai vanitha um ") == 1
