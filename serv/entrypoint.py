import json

import click

from serv.app import init_app, create_app
from serv.config import load_config

app = init_app(create_app(load_config()))


@app.cli.command()
def swagger():
    """Export swagger file"""
    click.echo(json.dumps(app.spec.to_dict(), indent=4))
