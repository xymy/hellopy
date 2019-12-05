import random

import click
from click.termui import _ansi_colors

colors = list(_ansi_colors)


def plain(message):
    click.echo(message)


def colorful(message):
    for c in message:
        fg = random.choice(colors)
        bg = random.choice(colors)
        click.secho(c, nl=False, fg=fg, bg=bg)
    click.echo()


def main():
    message = 'Hello, Python!'
    colorful(message)


if __name__ == '__main__':
    main()
