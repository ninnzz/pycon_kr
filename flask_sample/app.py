from flask import Flask, abort, make_response
app = Flask(__name__)

@app.route('/one')
def one():
	return 'This is a success.'

@app.route('/two')
def two():
	print('This will return a 404 error')
	abort(404)

@app.route('/three')
def three():
	print('This will return a 500 error')
	return make_response('Error', 500)

if __name__ == '__main__':
	app.run(debug = True)