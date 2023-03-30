from app.auth import bp
from flask import render_template
from .forms import LoginForm

@bp.route("/")
def index():
    return "hello from auth"


@bp.route("/login")
def login():
    form = LoginForm()
    return render_template("auth/login.html", form=form)
