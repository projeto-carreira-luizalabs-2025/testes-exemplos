import pytest
from unittest.mock import Mock

def test_should_validate_none_is_none():
    value = None
    assert value is None

def test_should_validate_value_is_positive():
    value = 1
    assert value is not None
    assert value > 0, "Valor deveria ser positivo"

    
def test_should_validate_list_has_a_value():
    my_list = [1, 2, 3]
    assert my_list is not None
    assert len(my_list) == 3
    assert my_list == [1, 2, 3]
    
def test_should_raise_exception():
    x = 0
    with pytest.raises(ZeroDivisionError):
        a = 10 / x
        assert False, "Não deveria chegar aqui"
    
class SampleException(Exception):
    """
    ...
    """
    
class Sample:
    def do(self):
        return 1

def test_should_mock(mocker):
    s = Sample()
    assert s.do() == 1
    
    s = Mock(sepec=Sample)
    s.do.side_effect = SampleException("Deu ruin")
    
    with pytest.raises(SampleException):
        s.do()
