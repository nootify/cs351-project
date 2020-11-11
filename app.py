from datetime import datetime

from flask import render_template, request

from server import create_app, run_app


# Setup Flask app
STATIC_FOLDER = "../static"
TEMPLATE_FOLDER = "../templates"
app = create_app(static_folder=STATIC_FOLDER, template_folder=TEMPLATE_FOLDER)


@app.route("/")
def index():
    now = datetime.now().strftime("%Y/%-m/%-d %-I:%M:%S %p")
    return render_template("index.html", time=now)


@app.route("/bad", methods=["POST"])
def vulnerable():
    data = request.form["bad-input"]
    return render_template("bad.html", user_input=data)


@app.route("/good", methods=["POST"])
def ok():
    data = request.form["good-input"]
    return render_template("good.html", user_input=data)


if __name__ == "__main__":
    run_app(app)
