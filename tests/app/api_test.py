from fastapi.testclient import TestClient
from fastapi import status


def test_shoul_get_root(api_client: TestClient):

    resp = api_client.get("/")
    assert resp is not None
    assert resp.status_code == status.HTTP_200_OK

    resp_body = resp.json()
    assert "version" in resp_body
