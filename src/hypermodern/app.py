from textwrap import fill

import click

from hypermodern import __version__ as version
from hypermodern import wikipedia


@click.command()
@click.option(
    "--language", 
    "-l", 
    default="en", 
    help="Choose an ISO-639 code for language", 
    metavar="LANG", 
    show_default=True
)
@click.version_option(version)
def main(language):
    click.secho(f"Hello, this is hypermodern {version}!", fg="green")

    data = wikipedia.get_random_page(language=language)

    click.secho(data["title"], fg="yellow")
    click.secho(fill(data["extract"]))

