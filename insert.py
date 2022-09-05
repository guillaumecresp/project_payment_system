import click

@click.command()
@click.option('--verbose', is_flag=True, help="Enables verbose mode.")
@click.option('--name', '-n', multiple=True, help="Name of the user.")
@click.password_option()
def cli(verbose, name, password):
    if verbose:
        click.echo('Verbose mode is on')
    click.echo("HelloWorld")
    for n in name:
        click.echo('Bye {0}'.format(n))
    click.echo('Password is: {0}'.format(password))
