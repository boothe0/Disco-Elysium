from flask import Flask, render_template, request
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from models import User, db
from flask_mail import Mail, Message
import os


app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = os.environ.get("SECRET_KEY", "dev_key_for_local_use")

app.config.update(
    MAIL_SERVER=os.environ.get("MAIL_SERVER", "localhost"),
    MAIL_PORT=int(os.environ.get("MAIL_PORT", 1025)),
    MAIL_USERNAME=os.environ.get("MAIL_USERNAME", None),
    MAIL_PASSWORD=os.environ.get("MAIL_PASSWORD", None),
    MAIL_USE_TLS=os.environ.get(
        "MAIL_USE_TLS", "False").lower() in ("true", "1"),
    MAIL_USE_SSL=os.environ.get(
        "MAIL_USE_SSL", "False").lower() in ("true", "1"),
    MAIL_DEFAULT_SENDER=os.environ.get(
        "MAIL_DEFAULT_SENDER", "noreply@example.com")
)
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "home"

with app.app_context():
    db.create_all()
mail = Mail(app)
mail.init_app(app)

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
            return render_template("index.html", user_logged_in=True, user=user)
        else:
            return render_template("index.html", user_logged_in=False)
    else:
        return render_template("index.html", user_logged_in=False)


@app.route('/about')
def about():

    return render_template("about.html")


@app.route('/empathy', methods=['GET', 'POST'])
def empathy():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        display_name = request.form['display_name']
        hashed_password_combo = generate_password_hash(password)

        # Store it in the User model
        user = User(email=email, password=hashed_password_combo,
                    display_name=display_name)

        db.session.add(user)
        db.session.commit()
        send_email()
    return render_template("blog_signup.html")

def send_email():
    try:
        with mail.connect() as conn:
            for user in User.query.all():
                msg = Message(
                    subject=f"Hello, {user.display_name} thank you for joining our mailing list!",
                    body="We are excited to have you with us.",
                    recipients=[user.email],
                )
                conn.send(msg)
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    app.run()
