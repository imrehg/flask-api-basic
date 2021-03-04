# Flask API intro

A tiny Flask API to experiment with.

Install `flask`, and the run it, for example as:

```shell
FLASK_ENV=development flask run -h localhost -p 80000
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

Playing with `GET` and query strings. Simple `GET` on `/item/<item>`

```shell
$ curl "localhost:8000/item/spoon"
{
  "item": "spoon",
  "query": {}
}
```

or include some query strings as well:

```shell
$ curl "localhost:8000/item/fork?fancy=yes"
{
  "item": "fork",
  "query": {
    "fancy": "yes"
  }
}
```

## Squaring

Playing with `POST` in either as form data:

```shell
$ curl -XPOST -d 'number=41&test=123' localhost:8000/square
square=1681.0
```

or JSON request:

```shell
$ curl -XPOST -H "Content-Type: application/json" -d '{"number":14}' localhost:8000/square
{
  "square": 196.0
}
```
