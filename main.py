from secrets import token_hex

from flask import Flask, request, render_template, url_for, redirect, flash
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from sqlalchemy import String, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, MappedColumn
from werkzeug.security import generate_password_hash, check_password_hash

from forms import LoginForm, AddCafeForm, RegisterUser

# FLASK + CONFIG
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
app.secret_key = token_hex(32)
bootstrap = Bootstrap5(app)
csrf  = CSRFProtect(app)
login_manager = LoginManager()
login_manager.init_app(app)
#END

# SQLALCHEMY SETUP
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)
#END


#Models
class Cafe(db.Model):
    __tablename__ = 'cafe'
    id: Mapped[int] = MappedColumn(primary_key=True)
    name : Mapped[str] = MappedColumn(String(50), unique=True, nullable=False)
    map_url : Mapped[str] = MappedColumn(String(250), nullable=False)
    img_url : Mapped[str] = MappedColumn(String(250), nullable=False)
    location : Mapped[str] = MappedColumn(String(250), nullable=False)
    has_sockets : Mapped[bool] = MappedColumn(Boolean, nullable=False)
    has_toilet : Mapped[bool] = MappedColumn(Boolean, nullable=False)
    has_wifi : Mapped[bool] = MappedColumn(Boolean, nullable=False)
    can_take_calls : Mapped[bool] = MappedColumn(Boolean, nullable=False)
    seats : Mapped[str] = MappedColumn(String(250), nullable=False)
    coffee_price : Mapped[str] = MappedColumn(String(250), nullable=False)

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id: Mapped[int] = MappedColumn(primary_key=True)
    name: Mapped[str] = MappedColumn(String(50), nullable=False)
    email: Mapped[str] = MappedColumn(String(50), unique=True, nullable=False)
    password: Mapped[str] = MappedColumn(String(250), nullable=False)
#END

with app.app_context():
    db.create_all()


#User loader
@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, user_id)

# Routes and Functions
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=["GET","POST"])
def register():
    form = RegisterUser()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()

        if user:
            flash("This email has already been registered, please log-in to continue!")
            return redirect(url_for('login'))

        new_user = User(
            name=name,
            email=email,
            password=generate_password_hash(password=password, method="pbkdf2:sha256", salt_length=8)
        )
        db.session.add(new_user)
        db.session.commit()
        flash("Registered Successfully!")
        return redirect(url_for('login'))


    return render_template("register.html", form=form)


@app.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    email = form.email.data
    password = form.password.data

    if form.validate_on_submit():
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar_one_or_none()

        if user and check_password_hash(user.password, password):
            login_user(user)
            flash("Logged in Successfully!")
            return redirect(url_for('home'))
        else:
            flash("Invalid credentials, Please try again")
            return redirect(url_for('login'))

    return render_template("login.html", form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("logged out successfully!")
    return redirect(url_for('home'))


@app.route("/cafes")
def cafes():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    return render_template("cafes.html", cafes=all_cafes)

@app.route("/suggest-cafe", methods=["GET","POST"])
def suggest_cafe():
    form = AddCafeForm()
    if form.validate_on_submit():
        new_cafe = Cafe(
            name = form.name.data,
            location = form.location.data,
            map_url = form.map_url.data,
            img_url = form.img_url.data,
            has_sockets = True if form.has_sockets.data == "yes" else False,
            has_toilet = True if form.has_toilet.data == "yes" else False,
            has_wifi = True if form.has_wifi.data == "yes" else False,
            can_take_calls = True if form.can_take_calls.data == "yes" else False,
            seats = form.seats.data,
            coffee_price = form.coffee_price.data
        )
        db.session.add(new_cafe)
        db.session.commit()
        flash("Cafe added successfully!", "success")
        return redirect(url_for('cafes'))

    print(form.errors)
    print(request.method)

    return render_template("add-cafe.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
