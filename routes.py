#This is the server end of our application responsible for fetching data
#if and when it is needed and talking to the database
#this forms the center of the server side technology at the request response cycle
from flask import Flask, render_template
#Create the object app which is an instance of the Flask microservice
app = Flask(__name__)
#The decorator must be an class implementation of Flask object 
#This means that everytime that the home page is run, the it gets routed to our index.html page
@app.route("/")
def index():
	return render_template("index.html")

@app.route("/about")
def about():
	return render_template("about.html")

if __name__ == "__main__":
	#Run the app on a local server
	app.run(debug=True)