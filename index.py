from flask import Flask, render_template, jsonify, request
from user.user import User
from logic.calculate import func

app = Flask(__name__)


@app.route('/')
@app.route('/<username>')
def index(username=None):
    if username:
        user = User(username, 25, ['eating', 'working', 'dancing'])
        return render_template('user.html', user=user)
    return render_template('user.html', user=None)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/_calc')
def _calc():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    result = func(a, b)
    return jsonify(ans=result)

@app.route('/calc')
def calc():
    return render_template('calc.html')


if __name__ == '__main__':
    app.run(debug=True)