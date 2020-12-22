from click import ClickException
from requests import get, RequestException


def get_random_page(language="en"):
    API_URL = f"https://{language}.wikipedia.org/api/rest_v1/page/random/summary"

    try:
        with get(API_URL) as response:
            response.raise_for_status()
            return response.json()
    except RequestException as exception:
        raise ClickException(str(exception))

