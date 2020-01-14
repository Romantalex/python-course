from Divisor_master import Simple

def test_Simple():
    assert Simple(13) == True
    assert Simple(25) == False
    assert Simple(33) == False
    assert Simple(17) == True
    assert Simple(121) == False

from Divisor_master import alldiv

def test_alldiv():
    assert alldiv(15) == [1, 3, 5, 15]
    assert alldiv(38) == [1, 2, 19, 38]
    assert alldiv(456) == [1, 2, 3, 4, 6, 8, 12, 19, 24, 38, 57, 76, 114, 152, 228, 456]
    assert alldiv(719) == [1, 719]
    assert alldiv(917) == [1, 7, 131, 917]

from Divisor_master import max_simple_div

def test_maxsdiv():
    assert max_simple_div(123) == 41
    assert max_simple_div(264) == 11
    assert max_simple_div(339) == 113
    assert max_simple_div(445) == 89
    assert max_simple_div(692) == 173