from calcul import add,divide,is_even 
import pytest
def test_add():
    assert add(10,3) ==  13

def test_divide():
    with pytest.raises(ValueError) as exc_info:
        divide(10,0)
    assert str(exc_info.value)== "Division par zéro impossible"

def test_is_even():
        assert is_even(2) == True
        