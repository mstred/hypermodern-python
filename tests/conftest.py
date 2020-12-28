from click.testing import CliRunner
from pytest import fixture


@fixture
def runner():
    return CliRunner()


@fixture
def mock_requests_get(mocker):
    mock = mocker.patch("hypermodern.wikipedia.get")
    mock.return_value.__enter__.return_value.json.return_value = {
        "title": "title",
        "extract": "extract"
    }

    return mock


@fixture
def mock_get_random_page(mocker):
    return mocker.patch("hypermodern.wikipedia.get_random_page")


def pytest_configure(config):
    config.addinivalue_line("markers", "e2e: mark as end-to-end test")

