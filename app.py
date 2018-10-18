from flask import Flask
from app.view.user.index import user
app = Flask(__name__)
app.register_blueprint(user)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5006, debug=True)
