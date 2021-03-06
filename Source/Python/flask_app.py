from pathlib import Path
from typing import NoReturn

from flask import Flask

from Source.Python.api import register_endpoints


def _construct_flask_app() -> Flask:
    static_file_folder = Path(__file__).parents[1].joinpath("Resource/StaticFiles").as_posix()
    flask_app = Flask(__name__, static_url_path="/static", static_folder=static_file_folder)

    @flask_app.route("/")
    def hello():
        return "Hello, World!"

    register_endpoints(flask_app)

    return flask_app


def _main() -> NoReturn:
    flask_app = _construct_flask_app()

    flask_app.run(host="0.0.0.0", port=9001)
    exit()


if __name__ == '__main__':
    _main()
else:
    app = _construct_flask_app()
