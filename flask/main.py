from flask import Flask, render_template, request
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/empathy', methods=['GET', 'POST'])
def empathy():

    if request.form:
        email = request.form['email']
        password = request.form['password']
        hashed_password_combo = generate_password_hash(password)

        print("Recieved email: ", email)
        print("Hashed Password ", hashed_password_combo)
    return render_template("blog_signup.html")


if __name__ == "__main__":
    app.run()
