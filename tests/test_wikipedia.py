from hypermodern.wikipedia import get_random_page


def test_get_random_page_with_specific_language(mock_requests_get):
    get_random_page(language="de")
    assert "de.wikipedia.org" in str(mock_requests_get.call_args.args)

