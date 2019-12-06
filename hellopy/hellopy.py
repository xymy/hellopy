import random

import click
from click.termui import _ansi_colors

colors = list(_ansi_colors)


def print_plain(message):
    click.echo(message)


def print_colorful(message):
    for c in message:
        fg = random.choice(colors)
        bg = random.choice(colors)
        click.secho(c, nl=False, fg=fg, bg=bg)
    click.echo()


@click.command()
@click.option('-p', '--plain', is_flag=True)
def main(plain):
    message = 'Hello, Python!'
    if plain:
        print_plain(message)
    else:
        print_colorful(message)


if __name__ == '__main__':
    main()  # pylint: disable=no-value-for-parameter
