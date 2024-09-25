from Selenium8_TDD import *
#
# def test_basic():
#     assert mnozenie(3, 5) == 15
#     assert mnozenie(1, 5) == 5
#     assert mnozenie(0.4, 10) == 4
#
# def test_1():
#     assert mnozenie(100, 1.1) == 110
#
# def test_2():
#     assert mnozenie(100, 0) == 0
#
# def test_3():
#     assert mnozenie(1, 2.2) == 2.2
#
# def test_4():
#     assert mnozenie('Mama', 5) == None

def test_11():
    assert fizzbuzz(1) == 1
    assert fizzbuzz(2) == 2
    assert fizzbuzz(3) == 'Fiss'
    assert fizzbuzz(4) == 4
    assert fizzbuzz(5) == 'Buzz'
    assert fizzbuzz(6) == 'Fiss'
    assert fizzbuzz(9) == 'Fiss'
    assert fizzbuzz(15) == 'FissBuzz'

def test_21():
    assert fizzbuzz('Mama') == None
    assert fizzbuzz(0) == None
    assert fizzbuzz(4.3) == 4
    assert fizzbuzz(4.8) == 4
    assert fizzbuzz('4') == 4
    assert fizzbuzz(None) == None
    assert fizzbuzz(-3) == None


