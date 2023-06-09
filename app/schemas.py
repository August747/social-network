from marshmallow import EXCLUDE, fields
from marshmallow.fields import Nested
from marshmallow_sqlalchemy import SQLAlchemyAutoSchemaOpts, SQLAlchemyAutoSchema

from app import db
from app.models import User, Profile, Post, Like


class BaseOpts(SQLAlchemyAutoSchemaOpts):
    """
    Base schema configurations:
        * session
        * unknown
    """

    def __init__(self, meta, ordered=False):
        if not hasattr(meta, "sqla_session"):
            meta.sqla_session = db.session
        if not hasattr(meta, "unknown"):
            meta.unknown = EXCLUDE
        if not hasattr(meta, "load_instance"):
            meta.load_instance = True
        if not hasattr(meta, "include_fk"):
            meta.include_fk = True
        super(BaseOpts, self).__init__(meta, ordered=ordered)


class BaseSchema(SQLAlchemyAutoSchema):
    """
    Base configured schema class
    """
    OPTIONS_CLASS = BaseOpts


class ProfileSchema(BaseSchema):
    class Meta:
        model = Profile


class UserSchema(BaseSchema):
    class Meta:
        model = User
        exclude = ('password',)

    profile = Nested(ProfileSchema(), many=False)


class PostSchema(BaseSchema):
    class Meta:
        model = Post


class PostListSchema(BaseSchema):
    class Meta:
        model = Post


class LikeSchema(BaseSchema):
    class Meta:
        model = Like

    user_id = fields.Integer(required=True)
    post_id = fields.Integer(required=True)
