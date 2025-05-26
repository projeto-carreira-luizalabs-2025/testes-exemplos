class SomeServiceException(Exception):
    """
    Alguma exceção
    """


class SomeService:

    def do_something(self, some: dict) -> dict:
        some["more_data"] = "more data"
        count = some.get("count", 0)
        for i in range(count):
            count += count
        some["count"] = count

        return count

    def create(self, some: dict) -> int:
        if "field" not in some:
            raise SomeServiceException()
        data = some["field"]
        return data
