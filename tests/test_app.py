from click.testing import CliRunner
from pytest import fixture

from hypermodern import app


@fixture
def runner():
    return CliRunner()


@fixture
def mock_requests_get(mocker):
    mock = mocker.patch("hypermodern.app.get")
    mock.return_value.__enter__.return_value.json.return_value = {
        "title": "title",
        "extract": "extract"
    }

    return mock


def test_main_pass(runner, mock_requests_get):
    result = runner.invoke(app.main)
    assert result.exit_code == 0


def test_main_requests_get_is_called(runner, mock_requests_get):
    result = runner.invoke(app.main)
    assert mock_requests_get.called


def test_main_requests_wikipedia_api(runner, mock_requests_get):
    result = runner.invoke(app.main)
    assert "en.wikipedia.org/api" in str(mock_requests_get.call_args.args)


def test_main_check_content(runner, mock_requests_get):
    result = runner.invoke(app.main)
    assert "title" in result.output and "extract" in result.output


def test_main_request_failed(runner, mock_requests_get):
    mock_requests_get.side_effect = Exception()
    result = runner.invoke(app.main)
    assert result.exit_code != 0

