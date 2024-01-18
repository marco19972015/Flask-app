from flask import Flask, render_template, request

# __name__ referes to the current file (turn this file into a Flask application)
app = Flask(__name__)

# This code decides based on the browsers request what file or files we will send from the server to the browser
@app.route("/")
def index():
    if "name" in request.args:
        name = request.args["name"]
    else: 
        name = "World"
    
    # Remember for render_template to run I need a tempalte folder (DUH)
    return render_template("index.html")