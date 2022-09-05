import click

@click.group()
def cli():
    pass

@cli.group()
def paypal():
    pass

@cli.group()
def card():
    pass

@click.command()
def sub():
    print("payment accepted")

@click.command()
def extra_pack():
    print("payment accepted")

paypal.add_command(sub)
card.add_command(sub)
paypal.add_command(extra_pack)
card.add_command(extra_pack)

if __name__ == '__main__':
    cli()