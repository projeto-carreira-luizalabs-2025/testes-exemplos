from typing import Iterator
from unittest import mock

from pytest import fixture, raises

import app.another_injector as anoher_injector_module
from app.another_injector import (
    AnotherInsertUseCase,
    AnotherRepository,
    AnotherSchema,
    AnotherService,
    Container,
)


class AnotherFakeException(Exception):
    """
    Exceção para o teste.
    """


class TestAnotherInjector:

    @fixture
    def another_container(self) -> Iterator[Container]:
        container = Container()
        container.reset_override()
        container.wire(modules=[anoher_injector_module.__name__])
        try:
            yield container
        finally:
            container.unwire()

    @fixture
    def some_seller_input(self) -> dict:
        input = {"seller": "seller01", "product_id": "product01", "a_value": 1_0_1}
        return input

    def test_should_insert_data_but_we_mocked_repository(
        self, another_container: Container, some_seller_input: dict
    ):
        repo = mock.Mock(AnotherRepository)
        # Estou testando AnotherService e "desconsiderando" o repositorio
        with another_container.repository.override(repo):
            output = AnotherInsertUseCase.insert(some_seller_input)
            # assert output is not None
            assert output is not None
            assert some_seller_input["seller"] in output

    def test_should_raise_an_exception_because_I_tell_you_later(
        self, another_container: Container, some_seller_input: dict
    ):
        repo = mock.Mock(AnotherRepository)
        repo.insert.side_effect = AnotherFakeException("Temos um problema aqui")
        
        with another_container.repository.override(repo):
            with raises(AnotherFakeException):
                AnotherInsertUseCase.insert(some_seller_input)
            
