from flask import Flask, render_template, request
from werkzeug.security import check_password_hash, generate_password_hash
from models import User, db


app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
# removes warnings from terminal
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/empathy', methods=['GET', 'POST'])
def empathy():

    if request.method == "POST":
        password = request.form['password']
        hashed_password = generate_password_hash(password)

        user = User(
            email=request.form['email'],
            password=hashed_password,
            display_name=request.form['display_name']
        )
        db.session.add(user)
        db.session.commit()
        print("Sucessful post")

    return render_template("blog_signup.html")


if __name__ == "__main__":
    app.run()
