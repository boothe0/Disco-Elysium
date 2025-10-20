from flask import Flask, render_template, request
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from models import User, db
import os

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = os.environ.get("SECRET_KEY", "dev_key_for_local_use")

db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "home"

with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    # Flask-Login calls this when loading the user from a session
    return User.query.get(int(user_id))


@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return render_template("index.html")
        else:
            return render_template("index.html")
    else:
        return render_template("index.html")


@app.route('/about')
def about():

    return render_template("about.html")


@app.route('/empathy', methods=['GET', 'POST'])
def empathy():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        hashed_password_combo = generate_password_hash(password)

        # Store it in the User model
        user = User(email=email, password=hashed_password_combo)
        db.session.add(user)
        db.session.commit()
    return render_template("blog_signup.html")


if __name__ == "__main__":
    app.run()
