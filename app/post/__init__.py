import csv

import click
from flask import Blueprint

from ..models import Post, User

bp = Blueprint('post', __name__, url_prefix='/post')

from . import routes


@bp.cli.command('extract_posts')
@click.argument('user_id')
def extract_posts(user_id):
    user = User.query.get(user_id)

    if user:
        filename = f'{user.username}_posts.csv'
        posts = user.posts

        with open(filename, mode='w', newline='') as file:
            fieldnames = ['Post Title', 'Likes count', 'Dislikes count', 'Post Created at']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            for post in posts:
                writer.writerow({
                    'Post Title': post.title,
                    'Likes count': Post.likes_count,
                    'Dislikes count': post.dislikes_count,
                    'Post Created at': post.created_at
                })

#       print(f'Posts extracted successfully to {filename}!')
#    else:
#        print('User not found.')
