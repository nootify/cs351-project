import logging
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


@app.route("/bad", methods=["GET", "POST"])
def vulnerable():
    if request.method == "POST":
        data = request.form.get("bad-input")
        return render_template("bad.html", user_input=data)
    else:
        return "Direct access not allowed."


@app.route("/good", methods=["GET", "POST"])
def ok():
    if request.method == "POST":
        data = request.form.get("good-input")
        return render_template("good.html", user_input=data)
    else:
        return "Direct access not allowed."


@app.route("/fixme", methods=["GET", "POST"])
def fixme_form():
    if request.method == "POST":
        data = request.form.get("fixme-input")
        return render_template("fixme.html", user_input=data)
    else:
        return "Please fix me."


if __name__ == "__main__":
    run_app(app)
