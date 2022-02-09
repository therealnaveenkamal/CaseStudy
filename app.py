from flask import Flask
import flask

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def hello():
    return flask.render_template("index.html")

@app.route('/hello')
def hello1():
    return "You are in Hello!"

if __name__ == '__main__':
    app.run('localhost', 4449, debug = True)
