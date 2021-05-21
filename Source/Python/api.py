from json import dumps

from flask import Flask, make_response, request

_GREETINGS_BY_LANGUAGE = {
    "english": "Hello",
    "spanish": "Hola",
    "german": "Hallo",
    "latin": "Salve",
}


def register_endpoints(flask_app: Flask) -> None:
    @flask_app.route("/api/hello/<name>", methods=["GET"])
    def api_hello_name__get(name: str):
        language = request.args.get("language", type=str) if "language" in request.args else "english"
        greeting = _get_greeting_in(language)
        return make_response(f"{greeting}, {name}!", 200)

    @flask_app.route("/api/greetings", methods=["GET"])
    def api_greetings__get():
        response = make_response(dumps(_GREETINGS_BY_LANGUAGE), 200)
        response.content_type = "application/json"
        return response

    @flask_app.route("/api/greeting/<language>", methods=["GET"])
    def api_greeting_language__get(language: str):
        try:
            greeting = _get_greeting_in(language)
            response = make_response(greeting, 200)
        except ValueError as e:
            response = make_response(dumps({"error": str(e)}), 404)
        response.content_type = "application/json"
        return response


def _get_greeting_in(language: str) -> str:
    if language not in _GREETINGS_BY_LANGUAGE:
        raise ValueError(f"No greeting is registered for desired language '{language}'")
    return _GREETINGS_BY_LANGUAGE[language]
