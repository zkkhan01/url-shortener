from httpx import AsyncClient
from app.main import app
import pytest

@pytest.mark.asyncio
async def test_create_and_fetch():
    async with AsyncClient(app=app, base_url="http://t") as ac:
        r = await ac.post("/shorten", params={"code":"x","url":"https://example.com"})
        assert r.status_code==200
        r = await ac.get("/x", follow_redirects=False)
        assert r.status_code in (302,307)
