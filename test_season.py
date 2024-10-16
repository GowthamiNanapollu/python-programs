from seasons import verify,convert

def test_convert():
    assert convert(2023,9,21) == "Five hundred twenty-seven thousand forty minutes"
    assert convert(2022,9,21)== "One million, fifty-two thousand, six hundred forty minutes"
