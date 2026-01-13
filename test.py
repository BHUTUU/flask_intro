
from flask import Flask, render_template, request
from models.TodoModel import TodoModel
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("todo.html")

@app.route("/fetch_all_todos"):
def fetch_all_todos():
# to work on!


if(__name__ == "__main__"):
    app.run(debug=True)