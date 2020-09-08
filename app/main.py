from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Sum(Resource):
	def get(self, a, b):
		data = None
		if not a.isnumeric():
			data = 'a'
		elif not b.isnumeric():
			data = 'b'
		else:
			data = int(a) + int(b)
		return {'data': data}
api.add_resource(Sum, '/<a>/<b>')

if __name__ == '__main__':
	app.run()