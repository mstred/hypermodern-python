from textwrap import fill

from click import command, secho, version_option
from requests import get

from hypermodern import __version__ as version

API_URL = "https://en.wikipedia.org/api/rest_v1/page/random/summary"

@command()
@version_option(version)
def main():
    secho(f"Hello, this is hypermodern {version}!", fg="green")

    with get(API_URL) as response:
        response.raise_for_status()
        data = response.json()

    secho(data["title"], fg="yellow")
    secho(fill(data["extract"]))

