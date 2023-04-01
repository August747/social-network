from app.main import bp
from flask import render_template


@bp.route("/")
@bp.route("/index")
def index():
    context = {
        "user": {"username": "vlad"},
        "title": "Hillel"
    }
    return render_template("index.html", **context)
