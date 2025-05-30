from fastapi.testclient import TestClient
from backend.app import news_store
from backend.app import app
from config import STUDENT_ID

client = TestClient(app)

def test_get_empty_sources():
    news_store.clear()
    res = client.get(f"/sources/{STUDENT_ID}")
    assert res.status_code == 200
    assert res.json() == {"sources": []}

def test_add_and_get_source():
    news_store.clear()
    res1 = client.post(f"/sources/{STUDENT_ID}", json={"url": "https://example.com/rss"})
    assert res1.status_code == 200
    assert "https://example.com/rss" in res1.json()["sources"]
    res2 = client.get(f"/sources/{STUDENT_ID}")
    assert "https://example.com/rss" in res2.json()["sources"]
    # assert res2.json()["sources"] == ["https://example.com/rss"]
