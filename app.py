import flask
from flask import jsonify, request

app = flask.Flask(__name__)

items = {
    "fork": "silver",
    "tooth": "wooden",
    "couch": "comfy",
}


@app.route("/", methods=["GET"])
def main():
    """Very basic entry to the API"""
    return "HelloWorld", 200


@app.route("/items", methods=["GET"])
def all_items():
    """Querying all the items we have in store."""
    return jsonify(sorted(list(items.keys())))


@app.route("/item/<item>", methods=["GET"])
def query_item(item):
    """Query a single item"""
    if item in items:
        result = {"item": item, "kind": items[item]}
        if "verbose" in request.args.keys():
            result["verbose"] = f"This is our {items[item]} {item}!"
        return jsonify(result)
    else:
        result = {"message": f"No record of this item: {item}"}
        return jsonify(result), 404


@app.route("/item", methods=["POST"])
def create_item():
    """Creating a new item"""
    params = request.json if request.is_json else request.form
    item_name = params.get("item")
    kind_value = params.get("kind")
    if item_name is not None and kind_value is not None:
        if item_name not in items:
            items[item_name] = kind_value
            return f"Created {item_name} of {kind_value} kind", 201
        else:
            return f"Can't create item, as {item_name} already exists", 409
    else:
        return "Please submit both 'item' and 'kind' parameters!", 400


if __name__ == "__main__":
    app.run()
