# import json

"""
herokuで動作するフロントページ
"""

import flask
from flask import request
import pgtest

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """
    動作確認用
    :return: hello worldのページ
    """
    return "hello world!"


@app.route('/abc', methods=['POST'])
def abc():
    """
    json送受信サンプル
    curl -H 'Content-Type:application/json' -d '{"text":"bbb"}' http://localhost:5000/abc
    :return: jsonサンプル
    """

    req = request.json

    print(req)
    print(req['text'])

    ret = pgtest.get_param()

    print(ret)

    result = {"hoge": "fuga"}
    # result = ret
    return flask.jsonify(result)


if __name__ == '__main__':
    # app.run(port=3000, debug=True)
    app.run()
