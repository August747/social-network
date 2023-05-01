from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    validators,
    PasswordField,
    BooleanField,
    SubmitField,
    EmailField,
)


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[validators.DataRequired(message="Username is required")])
    password = PasswordField(
        "Password",
        validators=[
            validators.DataRequired(message="Password is required"),
            validators.length(min=6, message="Min 6 length of password is required")
        ]
    )
    remember = BooleanField("Remember")
    submit = SubmitField("Log In")


class RegisterForm(LoginForm):
    email = EmailField("Email", validators=[validators.DataRequired(message="Email is required"), validators.Email()])
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[
            validators.DataRequired(message="Confirm password is required"),
            validators.EqualTo("password", message="Passwords should match")
        ]
    )
    first_name = StringField("First name", description='Optional')
    last_name = StringField("Last name", description='Optional')
    linkedin_url = StringField("Linkedin", description='Optional')
    facebook_url = StringField("Facebook", description='Optional')
    submit = SubmitField("Register", description='Optional')


