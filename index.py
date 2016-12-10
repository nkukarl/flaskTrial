from flask import Flask, render_template
from user.user import User

app = Flask(__name__)


@app.route('/')
@app.route('/<username>')
def index(username=None):
    if username:
        user = User(username, 25, ['eating', 'working', 'dancing'])
        return render_template('user.html', user=user)
    return render_template('user.html', user=None)

if __name__ == '__main__':
    app.run(debug=True)