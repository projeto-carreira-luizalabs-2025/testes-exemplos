import pytest
from pytest_httpx import HTTPXMock

from app.some_http_integration import IdMagaluHealthIntegration


@pytest.mark.asyncio
async def test_should_fake_idmagalu(httpx_mock: HTTPXMock):
    current_response_body = json={"meu": True}
    httpx_mock.add_response(url=IdMagaluHealthIntegration.API_HEALTHCHECK,json=current_response_body)
    integration = IdMagaluHealthIntegration()
    resp = await integration.healthchek()
    assert "meu" in resp
        
    await integration.close()