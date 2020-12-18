from click import command, secho, version_option

from hypermodern import __version__ as version

@command()
@version_option(version)
def main():
    secho(f"Hello, this is hypermodern {version}!", fg="green")

