# This is whre you can start you python file for your week1 web app
# Name: Christopher Van Schyndel

import flask
import settings
from utils import login_required

# Views
from login import Login
from remote import Remote
from music import Music
from triangle import Triangle
from scrabbleappfunc import Scrabbler

app = flask.Flask(__name__)
app.secret_key = settings.secret_key









# Works in progress

class Asteroids(flask.views.MethodView):
	@login_required
	def get(self):
		return flask.render_template('asteroids.html')

class RemoteZsnes(flask.views.MethodView):
	@login_required
	def get(self):
		return flask.render_template('remotezsnes.html')

class CoffeeData(flask.views.MethodView):
	@login_required
	def get(self):
		return flask.render_template('coffeedata.html')



# Routes

app.add_url_rule('/',
				 view_func=Login.as_view('login'),
				 methods=["GET", "POST"])
app.add_url_rule('/remote/',
				 view_func=Remote.as_view('remote'),
				 methods=["GET", "POST"])
app.add_url_rule('/triangle/', 
				 view_func=Triangle.as_view('triangle'),
				 methods=["GET", "POST"])
app.add_url_rule('/music/', 
				 view_func=Music.as_view('music'),
				 methods=["GET"])
app.add_url_rule('/asteroids/',
				 view_func=Asteroids.as_view('asteroids'),
				 methods=["GET"])
app.add_url_rule('/remotezsnes/',
				 view_func=RemoteZsnes.as_view('remotezsnes'),
				 methods=["GET"])
app.add_url_rule('/asteroids/',
				 view_func=CoffeeData.as_view('coffeedata'),
				 methods=["GET"])
app.add_url_rule('/scrabbler/',
				 view_func=Scrabbler.as_view('scrabbler'),
				 methods=["GET", "POST"])

@app.errorhandler(404)
def page_not_found(error):
	return flask.render_template('404.html'), 404


app.debug = True
app.run()