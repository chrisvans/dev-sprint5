import flask, flask.views
import os
from utils import login_required




def is_triangle(a, b, c):
	if a > b + c or b > a + c or c > a + b:
		return 'no, a triangle is not possible.'
	else:
		return 'yes, a triangle is possible.'

def stickinput(a, b, c):
	if a.isdigit() == False or b.isdigit() == False or c.isdigit() == False:
		return 'None'
	else:
		a = int(a)
		b = int(b)
		c = int(c)
		return is_triangle(a, b, c)

class Triangle(flask.views.MethodView):
	@login_required
	def get(self):
		return flask.render_template('triangle.html')
	
	@login_required
	def post(self):
		result = 'With the sides given: '
		result += str((flask.request.form['expressionA'])) + ', ' + str((flask.request.form['expressionB'])) + ', and ' + str((flask.request.form['expressionC'])) + '. '
		a = str((flask.request.form['expressionA']))
		b = str((flask.request.form['expressionB']))
		c = str((flask.request.form['expressionC']))
		trianglechecked = stickinput(a, b, c)
		result += 'Then ' + trianglechecked
		if a.isdigit() == True and b.isdigit() == True and c.isdigit() == True:
			flask.flash(result)
		return flask.redirect(flask.url_for('triangle'))