from datetime import datetime

from flask import render_template

from server import create_app, run_app


# Setup Flask app
app = create_app()


@app.route("/")
def index():
    now = datetime.now().strftime("%Y/%-m/%-d %-I:%M:%S %p")
    return render_template("index.html", time=now)


if __name__ == "__main__":
    run_app(app)
