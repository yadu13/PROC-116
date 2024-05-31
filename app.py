# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/father")


# define the route to father webpage
@app.route("/father")
def home1():

    name = "Mark" # write your name
    age = "30" # write your age

    return render_template('father.html' , name = name , age = age)
# define the route to mother webpage
@app.route("/mother")
def home2():

    name = "Erica" # write your name
    age = "25" # write your age

    return render_template('mother.html' , name = name , age = age)
# define the route to friends webpage
@app.route("/friend")
def home3():

    name = "Victor" # write your name
    age = "8" # write your age

    return render_template('friend.html' , name = name , age = age)
# define route for yourself
@app.route("/me")

def home4():

    name ="Alex" # write your name
    age = "6" # write your age

    return render_template('index.html' , name = name , age = age)

# run the file
app.run(debug=True)
