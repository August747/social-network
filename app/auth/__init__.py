from flask import blueprint

bp = blueprint("auth", __name__, url_prefix="/auth")

@bp.route("/")
def index():
    return "hello from auth"