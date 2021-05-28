from json import dumps
from typing import Callable, Union

from flask import Flask, make_response, request
from werkzeug.exceptions import BadRequest

_GREETINGS_BY_LANGUAGE = {
    "english": "Hello",
    "spanish": "Hola",
    "german": "Hallo",
    "latin": "Salve",
}


def register_endpoints(flask_app: Flask) -> None:
    @flask_app.route("/api/hello/<name>", methods=["GET"])
    @with_error_response_on_raised_exceptions
    def api_hello_name__get(name: str):
        language = (request.args.get("language", type=str)
                    if "language" in request.args else "english")
        greeting = _GREETINGS_BY_LANGUAGE[language]
        return make_response(f"{greeting}, {name}!", 200)

    @flask_app.route("/api/greetings", methods=["GET", "PUT"])
    @with_error_response_on_raised_exceptions
    def api_greetings():
        if request.method == "GET":
            response = make_response(dumps(_GREETINGS_BY_LANGUAGE), 200)
        else:
            greetings: dict = request.json
            if type(greetings) is not dict or any(map(
                    lambda x: type(x) is not str,
                    list(greetings.keys()) + list(greetings.values()))):
                raise ValueError("Body contents must be a dictionary of strings")
            _GREETINGS_BY_LANGUAGE.clear()
            _GREETINGS_BY_LANGUAGE.update(greetings)
            response = make_response(dumps(_GREETINGS_BY_LANGUAGE), 200)
        response.content_type = "application/json"
        return response

    @flask_app.route("/api/greeting/<language>", methods=["GET", "PUT"])
    @with_error_response_on_raised_exceptions
    def api_greeting_language(language: str):
        if request.method == "GET":
            greeting = _GREETINGS_BY_LANGUAGE[language]
            response = make_response(greeting, 200)
        else:
            is_new_greeting = language in _GREETINGS_BY_LANGUAGE
            greeting = request.data.decode("utf8")
            _GREETINGS_BY_LANGUAGE[language] = greeting
            response = make_response(
                f"Set greeting for {language} to be '{greeting}'",
                201 if is_new_greeting else 200)
        response.content_type = "application/json"
        return response


def _error_response(ex: Union[BaseException, str], status_code: int):
    error_message = ex if type(ex) is str else f"{type(ex).__name__}: {ex}"
    response = make_response(dumps({"error": error_message, "status_code": status_code}), status_code)
    response.content_type = "application/json"
    return response


def with_error_response_on_raised_exceptions(handler_function: Callable) -> Callable:
    def inner(*args, **kwargs):
        try:
            return handler_function(*args, **kwargs)
        except (TypeError, ValueError, AttributeError) as e:
            return _error_response(e, 400)
        except BadRequest as e:
            return _error_response(str(e), 400)
        except KeyError as e:
            return _error_response(e, 404)
        except BaseException as e:
            return _error_response(e, 500)

    inner.__name__ = f"__wrapped__{handler_function.__name__}"  # Flask needs method names to be unique
    return inner
