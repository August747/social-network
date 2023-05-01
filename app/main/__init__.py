from flask import Blueprint

bp = Blueprint("main", __name__)
from . import routes


@bp.cli.command("hello")
def hello():
    print("hello from cli")
