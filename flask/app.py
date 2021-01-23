from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return '<p>You\'ve reached the <b>Flask</b> Container</p>'


if __name__ == "__main__":
	app.run()