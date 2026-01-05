
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template("anisha.html")

@app.route("/login")
def anisha():
    username=request.args.get("usr")
    password=request.args.get("pass")
    description=request.args.get("desc")
    print(username, password, description)
    return "login is successful!"


if(__name__ == "__main__"):
    app.run(debug=True)