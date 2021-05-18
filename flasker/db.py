import click
from flask import current_app, g
from flask.cli import with_appcontext
from . import create_app
from .mysql import db
from .models import User, Post


def init_db():
    app = create_app()
    db.init_app(app)
    db.create_all()


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    app.cli.add_command(init_db_command)