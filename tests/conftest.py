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

