from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, RadioField, SelectField, EmailField
from wtforms.validators import DataRequired, Email, Length, URL, InputRequired


class AddCafeForm(FlaskForm):
    name = StringField("Cafe Name", validators=[DataRequired()])
    map_url = StringField("Google Maps URL", validators=[DataRequired(), URL()])
    img_url = StringField("Image URL", validators=[DataRequired(), URL()])
    location = StringField("Location", validators=[DataRequired()])
    has_sockets = RadioField(
        "Has sockets?",
        choices=[("yes","Yes"),("no", "No")],
        validators=[InputRequired()]
    )
    has_toilet = RadioField(
        "Has toilet?",
        choices=[("yes","Yes"),("no", "No")],
        validators=[InputRequired()]
    )
    has_wifi = RadioField(
        "Has Wifi?",
        choices=[("yes","Yes"),("no", "No")],
        validators=[InputRequired()]
    )
    can_take_calls = RadioField(
        "Can calls be taken?",
        choices=[("yes","Yes"),("no", "No")],
        validators=[InputRequired()]
    )
    seats = StringField("Number of Seats", validators=[DataRequired()])
    coffee_price = StringField("Coffee Price", validators=[DataRequired()])
    submit = SubmitField("Submit Cafe")

class RegisterUser(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")