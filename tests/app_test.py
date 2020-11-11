import pytest

from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


def test_main_page(client):
    page = client.get('/')
    assert b'CS351 Demo' in page.data
