import os

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello world! fukc you, circleci, from github actions && /' 
        + 'no, no, no...fukc github actions too'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
