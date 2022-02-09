from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello Python!"

@app.route('/hello')
def hello1():
    return "You are in Hello!"

if __name__ == '__main__':
    app.run('localhost', 4449)
