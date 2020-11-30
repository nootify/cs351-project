import pytest


@pytest.fixture()
def mock_xss_input():
    attacks = [
        r"""<img onmouseover="alert('this page is vulnerable to XSS')">""",
        r"<script>alert('this page is vulnerable to XSS');</script>",
    ]
    return attacks


@pytest.fixture()
def mock_normal_input():
    user_input = [
        "Hello World",
        "0123456789",
    ]
    return user_input


class TestPages:
    @pytest.mark.parametrize("route", ["/", "/bad", "/good"])
    def test_access_page(self, client, route):
        page = client.get(route)
        if route == "/":
            assert b"CS351 Demo" in page.data
        else:
            assert b"Direct access not allowed." in page.data


class TestForms:
    @pytest.mark.parametrize(
        "route,input_form", [("/bad", "bad-input"), ("/good", "good-input")]
    )
    def test_form_xss_input(self, client, mock_xss_input, route, input_form):
        for xss_input in mock_xss_input:
            page = client.post(route, data={input_form: xss_input})
            assert xss_input.encode("ascii") not in page.data

    @pytest.mark.parametrize(
        "route,input_form", [("/bad", "bad-input"), ("/good", "good-input")]
    )
    def test_form_normal_input(self, client, mock_normal_input, route, input_form):
        for user_input in mock_normal_input:
            page = client.post(route, data={input_form: user_input})
            assert user_input.encode("ascii") in page.data
