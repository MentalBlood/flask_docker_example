from flask import Flask, request
from flask_restful import Resource, Api
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)
api = Api(app)

@app.route('/add', methods=['POST'])
def json_example():
	args = request.get_json()
	a = args['a']
	b = args['b']
	data = None
	if not type(a) == type(1):
		data = 'a'
	elif not type(b) == type(1):
		data = 'b'
	else:
		data = int(a) + int(b)
	return {'data': data}

if __name__ == '__main__':
	app.run()