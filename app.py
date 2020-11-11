from datetime import datetime

from flask import render_template

from server import create_app, run_app


# Setup Flask app
STATIC_FOLDER = "../static"
TEMPLATE_FOLDER = "../templates"
app = create_app(static_folder=STATIC_FOLDER, template_folder=TEMPLATE_FOLDER)


@app.route("/")
def index():
    now = datetime.now().strftime("%Y/%-m/%-d %-I:%M:%S %p")
    return render_template("index.html", time=now)


if __name__ == "__main__":
    run_app(app)
