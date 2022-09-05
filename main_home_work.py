import flask
import utills

app = flask.Flask(__name__)
"""
Приложение, считывает файл с перечнем кандидатов, их фото и данными в формате JSON.
создает WEB сайт с полным перечнем кандидатов в головной каталоге и отдельно по номерам и профессиям 
"""


@app.route('/')
def index():
    return utills.get_all()


@app.route('/candidates/<int:pk>')
def get_candidate(pk):
    return utills.get_by_pk(pk)


@app.route('/skills/<skill>')
def get_candidate_skill(skill):
    return utills.get_by_skill(skill)


app.run(debug=True)
