from pytest import mark
from requests import RequestException

from hypermodern import app
from hypermodern.wikipedia import get_random_page


@mark.e2e
def test_main_pass(runner):
    result = runner.invoke(app.main)
    assert result.exit_code == 0


def test_main_pass_mocked(runner, mock_requests_get):
    result = runner.invoke(app.main)
    assert result.exit_code == 0


def test_main_requests_get_is_called(runner, mock_requests_get):
    runner.invoke(app.main)
    assert mock_requests_get.called


def test_main_requests_wikipedia_api(runner, mock_requests_get):
    runner.invoke(app.main)
    assert "en.wikipedia.org/api" in str(mock_requests_get.call_args.args)


def test_main_check_content(runner, mock_requests_get):
    result = runner.invoke(app.main)
    assert "title" in result.output and "extract" in result.output


def test_main_request_failed(runner, mock_requests_get):
    mock_requests_get.side_effect = Exception()
    result = runner.invoke(app.main)
    assert result.exit_code != 0


def test_main_prints_on_failed_request(runner, mock_requests_get):
    mock_requests_get.side_effect = RequestException()
    result = runner.invoke(app.main)
    print(result.output)
    assert "Error" in result.output


def test_main_with_specific_language(runner, mock_get_random_page):
    language = "pt"
    runner.invoke(app.main, [f"--language={language}"])
    assert mock_get_random_page.called_with(language=language)

