from flask import Flask, render_template, request

# __name__ referes to the current file (turn this file into a Flask application)
app = Flask(__name__)

# This code decides based on the browsers request what file or files we will send from the server to the browser
@app.route("/")
def index():
    # Instead of using if else block, I can use 'get' method
    # First argument is what value we want to get
    # Second value is what value we want the default as
    # name = request.args.get("name", "World")

    # Remember for render_template to run I need a tempalte folder (DUH)
        # place holder referes to the literal placehold in the template
        # name refers to the variable above (but can be any value)
    return render_template("index.html") 

@app.route("/greet")
def greet():
    return render_template("greet.html", name=request.args.get("name", "world"))