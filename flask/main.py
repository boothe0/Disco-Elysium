from flask import Flask, render_template
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


@app.route('/empathy')
def empathy():
    return render_template("blog.html")


if __name__ == "__main__":
    app.run()
