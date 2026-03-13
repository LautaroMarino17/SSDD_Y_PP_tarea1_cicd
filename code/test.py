from calculadora import sum

def test_sum():
    assert sum(2, 3) == 5

def test_sum_negativos():
    assert sum(-2, -3) == -5

def test_sum_mixto():
    assert sum(-2, 3) == 1