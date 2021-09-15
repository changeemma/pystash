import click


@click.group()
def cli():
    pass


@cli.command()
def ls():
    click.echo(f"listing")


@cli.command()
@click.argument("key", type=click.STRING)
def fetch(key):
    click.echo(f"fetched {key}")


@cli.command()
@click.argument("key", type=click.STRING)
def update(key):
    click.echo(f"updated {key}")


@click.argument("key", type=click.STRING, default="", required=False)
@cli.command()
def logs(key):
    click.echo(f"showing logs for {key}")
