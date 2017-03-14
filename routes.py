#This is the server end of our application responsible for fetching data
#if and when it is needed and talking to the database
#this forms the center of the server side technology at the request response cycle
from flask import Flask, render_template, request
from models import db, User
from forms import SignupForm

app = Flask(__name__)
#Check out Flask-sqlAlchemy #Connects to database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/learningflask'
db.init_app(app)

app.secret_key = "development-key"

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
  form = SignupForm()

  if request.method == "POST":
    if form.validate() == False:
      return render_template('signup.html', form=form)
    else:
      newuser = User(form.first_name.data, form.last_name.data, form.email.data, form.password.data)
      db.session.add(newuser)
      db.session.commit()
      return 'Success!'

  elif request.method == "GET":
    return render_template('signup.html', form=form)

if __name__ == "__main__":
	#Run the app on a local server
  app.run(debug=True)