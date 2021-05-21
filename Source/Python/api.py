from flask import Flask, make_response


def register_endpoints(flask_app: Flask) -> None:
    @flask_app.route("/api/hello", methods=["GET"])
    def api_hello__get():
        return make_response("Hello, Flask API!", 200)
