import flask, flask.views

class Main(flask.views.MethodView):
	def get(self, page="login"):
		page += ".html"
		if os.path.isfile('templates/' + page):
			return flask.render_template(page)
		flask.abort(404)

