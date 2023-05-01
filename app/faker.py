import click
from flask import Blueprint
from faker import Faker

from app import db
from app.models import User

bp = Blueprint('fake', __name__)
faker = Faker()


@bp.cli.command("users")
@click.argument('num', type=int)
def users(num):
    users = []
    for i in range(num):
        username = faker.user_name()
        email = faker.email()
        user = (
            db.session.query(User)
            .filter(
                User.username == username,
                User.email == email
            )
        ).first()

        if not user:
            user = User(
                username=username,
                email=email,
            )
            db.session.add(user)
            users.append(user)

    db.session.commit()
    print(num, 'users added.')
