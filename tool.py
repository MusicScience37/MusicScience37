#!/usr/bin/env python3

import subprocess
import click
from pathlib import Path
from typing import Optional


THIS_DIR = Path(__file__).absolute().parent


SUPPORTED_LANGUAGES = ["ja", "en"]


@click.group()
def cli():
    pass


@cli.command()
def update():
    """Update translation files."""

    subprocess.run(
        [
            "sphinx-build",
            "-M",
            "gettext",
            "source",
            "build",
        ],
        check=True,
        cwd=str(THIS_DIR),
    )
    subprocess.run(
        [
            "sphinx-intl",
            "update",
            "-p",
            "../build/gettext",
            "-l",
            "en",
        ],
        check=True,
        cwd=str(THIS_DIR / "source"),
    )


@cli.command()
@click.option(
    "-l",
    "--language",
    default="ja",
    help="Language.",
    type=click.Choice(SUPPORTED_LANGUAGES, case_sensitive=True),
)
def build(language: str):
    """Build document."""

    subprocess.run(
        [
            "sphinx-build",
            "-M",
            "html",
            "source",
            f"build/{language}",
            "-D",
            f"language={language}",
        ],
        check=True,
        cwd=str(THIS_DIR),
    )


DEFAULT_PORTS = {
    "ja": 8880,
    "en": 8881,
}


@cli.command()
@click.option(
    "-l",
    "--language",
    default="ja",
    help="Language.",
    type=click.Choice(SUPPORTED_LANGUAGES, case_sensitive=True),
)
@click.option("-p", "--port", default=None, help="Port of the HTTP server.", type=int)
def view(language: str, port: Optional[int]):
    """View HTML files."""

    if port is None:
        port = DEFAULT_PORTS[language]

    subprocess.run(
        ["python3", "-m", "http.server", str(port)],
        check=False,
        cwd=str(THIS_DIR / "build" / str(language) / "html"),
    )


if __name__ == "__main__":
    cli()
