import click

from . import __version__


@click.command()
@click.version_option(version=__version__)
def main():
    """A Python CLI to open a web page from a Git repository."""
    click.echo("Hello, world!")
