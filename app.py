from flask import Flask, render_template, request

# __name__ referes to the current file (turn this file into a Flask application)
app = Flask(__name__)

# This code decides based on the browsers request what file or files we will send from the server to the browser
# method now says we can handle both GET and POST request
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET": 
        return render_template("index.html")
    elif request.method == "POST":
        return render_template("greet.html", name=request.form.get("name", "world"))
    
    # Instead of using if else block, I can use 'get' method
    # First argument is what value we want to get
    # Second value is what value we want the default as
    # name = request.args.get("name", "World")

    # Remember for render_template to run I need a tempalte folder (DUH)
        # place holder referes to the literal placehold in the template
        # name refers to the variable above (but can be any value)
    # return render_template("index.html") 

# To support POST request we need to include the method as an argument and pass in an array and string POST
# expect the data via POST
# @app.route("/greet", methods=["POST"])
# def greet():
#     return render_template("greet.html", name=request.args.get("name", "world"))
    



# SIDE NOTES 
    # request.args is only used when using GET (It's a dictionary that contains all of our key valued pairs)
    # When using POST with Flask we need to use request.form

    # GET is always the default in the browsers, only when we click on a button that has been confifured to use POST 
    # are we actually addings things to ie. a cart