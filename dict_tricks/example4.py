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


ninja_map = {
    'genin': {
        'base_class': Genin,
        'unique_action': Genin.only_genin_can_do
    },
    'chunin': {
        'base_class': Chunin,
        'unique_action': Chunin.only_chunin_can_do
    },
    'jounin': {
        'base_class': Jounin,
        'unique_action': Jounin.only_jounin_can_do
    }
}


@app.route('/<ninja_type>')
def genin(ninja_type):
    params = request.args
    ninja_class = ninja_map[ninja_type]['base_class']()

    if not ninja_class.validate(params):
        return make_response('Failed {}'.format(ninja_type), 500)

    return ninja_map[ninja_type]['unique_action']()


if __name__ == '__main__':
    app.run(debug = True)
