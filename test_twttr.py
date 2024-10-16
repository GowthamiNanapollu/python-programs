from twttr import shorten


def test_vowels():
    assert shorten("hai")=='h'
    assert shorten("twitter")=="twttr"



def test_consonants():
    assert shorten("crpty")=="crpty"
    assert shorten('fly')=='fly'


def test_capitalvowels():
    assert shorten("HELLO")=='HLL'
    assert shorten('SUPER')=='SPR'




def test_numbers():
    assert shorten('cs50')=='cs50'
    assert shorten('hell0')=='hll0'



def test_punctuation():
    assert shorten('what is your Name ?')=='wht s yr Nm ?'
    assert shorten('Hello!')=='Hll!'
