from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return"<p>Hello, World!dit is de 2e commit<p>"


@app.route("/tweede")
def hello_world2():
    return"<p>Hello, World! tweede<p>"
