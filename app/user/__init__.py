import csv

from flask import Blueprint

from ..models import User

bp = Blueprint('user', __name__, url_prefix='/user')

from . import routes


#@bp.cli.command('extract_users')
#def extract_users():
#    users = User.query.all()

#    with open('users.csv', mode='w', newline='') as file:
#        fieldnames = ['username', 'email', 'full_name', 'post_count']
#        writer = csv.DictWriter(file, fieldnames=fieldnames)

#        writer.writeheader()
#       for user in users:
#            writer.writerow({
#                'username': user.username,
#                'email': user.email,
#               'full_name': user.full_name,
#                'post_count': len(user.posts)
#           })
