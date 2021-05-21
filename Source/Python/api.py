from flask import Flask, make_response, request


def register_endpoints(flask_app: Flask) -> None:
    @flask_app.route("/api/hello/<name>", methods=["GET"])
    def api_hello_name__get(name: str):
        language = request.args.get("language", type=str) if "language" in request.args else "english"
        greeting = _get_greeting_in(language)
        return make_response(f"{greeting}, {name}!", 200)


def _get_greeting_in(language: str) -> str:
    greetings_by_language = {
        "english": "Hello",
        "spanish": "Hola",
        "german": "Hallo",
        "latin": "Salve",
    }
    if language not in greetings_by_language:
        raise ValueError(f"No greeting is registered for desired language '{language}'")
    return greetings_by_language[language]
