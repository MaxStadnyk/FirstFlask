# -*- coding: utf-8 -*-
from flask import Flask, request
from func import s_names

app = Flask(__name__)


@app.route("/likes")
def index():
    if request.args.get('names') is None:
        return dict(error=True, data=None, error_message="Incorrect data")
    else:
        names_get = request.args.get('names').split(',')
        res_str = s_names(names_get)
        if res_str != "Incorrect data":
            return dict(error=False, data=res_str, error_message=None)
        else:
            return dict(error=True, data=None, error_message="Incorrect data")


if __name__ == "__main__":
    app.run(port=8000)
#AttributeError
