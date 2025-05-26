from app.some_service import SomeService
from pytest import raises

def test_should_not_create_a_none_service():
    ss = SomeService()
    with raises(TypeError):
        ss.create(None)
        assert False, "Não deveria criar None"
        

def test_shoud_create_a_valid_service(a_some_service: SomeService):
    assert a_some_service is not None
    data_value = "value"
    ret = a_some_service.create({"count": 1, "field": data_value})
    assert ret is not None
    assert ret == data_value