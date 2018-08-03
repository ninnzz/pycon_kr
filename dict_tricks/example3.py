from flask import Flask, abort, make_response, request
app = Flask(__name__)


class Genin():

    @staticmethod
    def only_genin_can_do():
        return 'Graduiate from ninja academy'

    def validate(self, data):
        if 'team_leader' not in data:
            return False
        return True

class Chunin():

    @staticmethod
    def only_chunin_can_do():
        return 'Take chunin exam'

    def validate(self, data):
        if 'examiner' not in data or data['examiner'] != 'kakashi':
            return False
        return True

class Jounin():

    @staticmethod
    def only_jounin_can_do():
        return 'Be a team leader'

    def validate(self, data):
        if 'mission' not in data or data['mission'] != 'kill_akatsuki':
            return False
        return True


@app.route('/genin')
def genin():
    params = request.args
    genin_class = Genin()

    if not genin_class.validate(params):
        return make_response('Failed genin', 500)

    return genin_class.only_genin_can_do()

@app.route('/jounin')
def jounin():
    params = request.args
    jounin_class = Jounin()

    if not jounin_class.validate(params):
        return make_response('Failed jounin', 500)

    return jounin_class.only_jounin_can_do()


@app.route('/chunin')
def chunin():
    params = request.args
    chunin_class = Chunin()

    if not chunin_class.validate(params):
        return make_response('Failed chunin', 500)

    return chunin_class.only_chunin_can_do()


if __name__ == '__main__':
    app.run(debug = True)
