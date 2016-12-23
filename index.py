from flask import Flask, render_template, jsonify, request
from user.user import User
from logic.calculate import add2
from logic.information import get_table_info

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
    """
    query format: http://localhost:5000/_calc?a=5&b=5
    """
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    ans = add2(a, b)
    return jsonify(ans)

@app.route('/calc')
def calc():
    return render_template('calc.html')

@app.route('/_info')
def _info():
    table_info = get_table_info()
    return jsonify(table_info)

@app.route('/info')
def info():
    return render_template('info.html')


if __name__ == '__main__':
    app.run(debug=True)