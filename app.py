import flask
from flask import jsonify, request

app = flask.Flask(__name__)


@app.route("/", methods=["GET"])
def main():
    """Very basic entry to the API"""
    return "HelloWorld", 200


@app.route("/item/<item>", methods=["GET"])
def echo_items(item):
    """Returns the same item as requested,
    as well as a any possible query string
    """
    result = {"item": item, "query": {}}
    for key in request.args.keys():
        result["query"][key] = request.args.get(key)
    return jsonify(result)


@app.route("/square", methods=["POST"])
def squaring():
    """Square a number received through the 'number'
    parameter of the post data
    """
    if request.is_json:
        number = request.json.get("number")
    else:
        number = request.form.get("number")

    if number is None:
        # There wasn't a 'number' supplied
        return "Missing 'number' parameter", 400

    try:
        # Cast to floating point to handle as many types of input as possible
        fnumber = float(number)
    except ValueError:
        return f"Provided 'number' parameter is not a number: {number}", 400

    result = fnumber * fnumber
    if request.is_json:
        return jsonify({"square": result})
    else:
        return f"square={result}"


if __name__ == "__main__":
    app.run()
