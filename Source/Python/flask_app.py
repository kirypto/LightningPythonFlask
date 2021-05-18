from typing import NoReturn

from flask import Flask


def _construct_flask_app() -> Flask:
    flask_app = Flask(__name__)

    @flask_app.route("/")
    def hello():
        return "Hello, World!"

    return flask_app


def _main() -> NoReturn:
    flask_app = _construct_flask_app()

    flask_app.run(host="0.0.0.0", port=9001)
    exit()


if __name__ == '__main__':
    _main()
else:
    app = _construct_flask_app()
