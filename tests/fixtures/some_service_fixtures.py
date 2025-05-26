from app.some_service import SomeService
from pytest import fixture

@fixture
def a_some_service() -> SomeService:
    service = SomeService()
    return service