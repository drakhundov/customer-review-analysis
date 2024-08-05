import click
import parser


@click.group()
def cli():
    pass


@cli.command("cur", help="select needed currencies")
@click.option("--from-cur", prompt=f"From")
@click.option("--to-cur", prompt=f"To")
def money(from_cur, to_cur):
    click.echo("Currency now: " + str(parser.get_currency(from_cur, to_cur)))


@cli.command("last", help="show last usd-azn and usd-rub")
def last():
    click.echo(
        "Dollar To Ruble: {currency}".format(currency=parser.get_currency("usd", "rub"))
    )
    click.echo(
        "Dollar To Manat: {currency}".format(currency=parser.get_currency("usd", "azn"))
    )


if __name__ == "__main__":
    cli()
