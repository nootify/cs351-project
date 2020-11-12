import pytest

from app import app


@pytest.fixture()
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


@pytest.fixture()
def mock_input():
    return "test"


class TestPages:
    def test_main_page(self, client):
        page = client.get("/")
        assert b"Hello World" in page.data

    def test_bad_page(self, client):
        page = client.get("/bad")
        assert b"Direct access not allowed." in page.data

    def test_good_page(self, client):
        page = client.get("/good")
        assert b"Direct access not allowed." in page.data

    def test_fixme_page(self, client):
        page = client.get("/fixme")
        assert b"Please fix me." in page.data


class TestForms:
    def test_bad_form(self, client, mock_input):
        page = client.post("/bad", data={"bad-input": mock_input})
        assert mock_input.encode("ascii") in page.data

    def test_good_form(self, client, mock_input):
        page = client.post("/good", data={"good-input": mock_input})
        assert mock_input.encode("ascii") in page.data

    def test_fixme_form(self, client, mock_input):
        page = client.post("/fixme", data={"fixme-input": mock_input})
        assert mock_input.encode("ascii") in page.data
