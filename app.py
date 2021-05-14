from typing import NoReturn

from flask import Flask


def _main() -> NoReturn:
    flask_app = Flask(__name__)

    @flask_app.route("/")
    def hello():
        return "Hello, World!"

    flask_app.run()
    exit()


if __name__ == '__main__':
    _main()
