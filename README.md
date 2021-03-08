# Flask API intro

A tiny Flask API to experiment with.

Install `flask`, and the run it, for example as:

```shell
FLASK_ENV=development flask run -h localhost -p 8000
```

this will run `app.py` in development mode, and restart
the server whenever the file changes.

Try the various endpoints as listed below.

## Top level

Simple `GET` query:

```shell
$ curl localhost:8000/
HelloWorld
```

## Items

Playing with `GET` and query strings. A simple `GET` on `/items` to get all
items back:

```shell
$ curl "localhost:8000/items"
[
  "couch",
  "fork",
  "tooth"
]
```

To query a single item, issue a simple `GET` on `/item/<item>`

```shell
$ curl "localhost:8000/item/tooth"
{
  "item": "tooth",
  "kind": "wooden"
}
```

or modify the request with a query string parameter `format=full`:

```shell
curl "localhost:8000/item/tooth?format=full"
{
  "item": "tooth",
  "kind": "wooden",
  "verbose": "This is our wooden tooth!"
}
```

To add new items, use `POST` request on the `/item` endpoint,
including `item` and `kind` as a form data or JSON. As form data:

```shell
$ curl -XPOST -d 'item=spoon&kind=coffee' localhost:8000/item
Created spoon of coffee kind

$ curl "localhost:8000/item/spoon"
{
  "item": "spoon",
  "kind": "coffee"
}
```

As JSON:

```shell
$ curl -XPOST -H 'Content-type: application/json' -d '{"item": "castle", "kind": "bouncy"}' localhost:8000/item
Created castle of bouncy kind%

$ curl "localhost:8000/item/castle?verbose"
{
  "item": "castle",
  "kind": "bouncy",
  "verbose": "This is our bouncy castle!"
}
```

Items cannot be overwritten after they are set:

```shell
$ curl -XPOST -d 'item=chocolate&kind=hot' localhost:8000/item
Created chocolate of hot kind

$ curl -XPOST -d 'item=chocolate&kind=hot' localhost:8000/item
Can't create item, as chocolate already exists
```

Also getting a 404 status with a message if the item is not known:
```shell
$ curl "localhost:8000/item/mirage"
{
  "message": "No record of this item: mirage"
}
```

The server stores the items in memory, so it will always be going back to the
same basic items that we have set by default when the server restarts.
