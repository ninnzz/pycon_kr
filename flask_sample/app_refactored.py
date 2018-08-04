from flask import Flask, abort, make_response, jsonify
app = Flask(__name__)

class ErrorResponse(Exception):
    # Set default status
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        return dict(code=self.status_code, message=self.message, data=self.payload)

@app.errorhandler(ErrorResponse)
def exception_encountered(error):
    error = error.to_dict()
    # You can modify this to return any kind of error
    # You can return an error page
    # You can use json return for pure API
    return make_response(jsonify(error), error['code'])

@app.route('/one')
def one():
    return 'This is a success.'

@app.route('/two')
def two():
    raise ErrorResponse('This will be 404', 404)

@app.route('/three')
def three():
    raise ErrorResponse('This will be a 500 error', payload='With additional data', status_code=500)

if __name__ == '__main__':
    app.run(debug = True)