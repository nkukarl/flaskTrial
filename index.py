from flask import Flask
import time

app = Flask(__name__)


@app.route('/')
def index():
    return 'This is the home page!'

@app.route('/profile/<username>')
def profile(username):
    return username

@app.route('/post/<int:id>')
def show(id):
    return str(id)


if __name__ == '__main__':
    app.run(debug=True)