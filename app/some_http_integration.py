from httpx import AsyncClient


class IdMagaluHealthIntegration:
    API_HEALTHCHECK = "https://id.magalu.com/account/healthcheck"

    def __init__(self):
        self.api_client = AsyncClient()
        
    async def close(self):
        await self.api_client.aclose()

    async def healthchek(self) -> dict:

        api_resp = await self.api_client.get(self.API_HEALTHCHECK)
        api_resp.raise_for_status()
        data = api_resp.json()

        return data
