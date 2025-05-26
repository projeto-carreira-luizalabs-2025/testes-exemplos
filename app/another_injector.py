from typing import Any

from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject
from pydantic import BaseModel


class AnotherRepository:
    def __init__(self):
        self.db = {}

    def insert(self, key: str, value: Any):
        self.db[key] = value

    def get(self, key: str) -> Any:
        value = self.db[key]
        return value


class AnotherEntity(BaseModel):
    seller_id: str
    sku: str
    value: int


class AnotherService:
    def __init__(self, another_repository: AnotherRepository):
        self.repository = another_repository

    @classmethod
    def get_another_key(cls, another: AnotherEntity) -> str:
        another_key = cls.mount_another_key(another.seller_id, another.seller_id)
        return another_key

    @staticmethod
    def mount_another_key(seller_id: str, sku: str) -> str:
        another_key = f"{seller_id},{sku}"
        return another_key

    @staticmethod
    def get_another_data(another: AnotherEntity) -> dict:
        another_data = {"value": another.value}
        return another_data

    def insert(self, another: AnotherEntity) -> str:

        another_key = self.get_another_key(another)
        another_data = another.model_dump()
        self.repository.insert(another_key, another_data)
        return another_key

    def get_by_seller_id_and_sku(
        self, seller_id: str, sku: str
    ) -> AnotherEntity | None:

        another_id = self.mount_another_key(seller_id, sku)


class Container(containers.DeclarativeContainer):

    repository = providers.Singleton(AnotherRepository)
    service = providers.Factory(AnotherService, repository)


class AnotherSchema(BaseModel):
    seller: str | None = None
    product_id: str | None = None
    a_value: int | None = None


class AnotherInsertUseCase:

    @inject
    @staticmethod
    def insert(
        another: dict | AnotherSchema, service: AnotherService = Provide[Container.service]
    ) -> str:
        if isinstance(another, dict):
            another = AnotherSchema(**another)
        # XXX Validar entrada: há seller_id, há sku, há valor?

        another_entity = AnotherEntity(
            seller_id=another.seller, sku=another.product_id, value=another.a_value
        )
        another_key = service.insert(another_entity)
        
        return another_key
