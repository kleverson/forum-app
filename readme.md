# Flask example

Using Flask to build a Flask-SQLalchemy extensions.

### Extension:

- SQL ORM: [Flask-SQLalchemy](http://flask-sqlalchemy.pocoo.org/2.1/)

## Installation

Install with pip:

```
$ pip install -r requirements.txt
```

#### cfg example

```

DEBUG = true
SQLALCHEMY_DATABASE_URI = 'Connection string'
SQLALCHEMY_TRACK_MODIFICATIONS = true

TITLE = "analytics api"
SECRET_KEY = "jadkfbsdkjbfbh"
PASSWORD_SCHEMES = ['pbkdf2_sha512', 'md5_crypt']

JWT_SECRET_KEY= "abcd1dfa134"
JWT_BLACKLIST_ENABLED = true
JWT_ACCESS_TOKEN_EXPIRES=60
JWT_BLACKLIST_TOKEN_CHECKS = ['access','refresh']

EXTENSIONS = [
    "forum.blueprints:init_app",
    "forum.ext.database:init_app"
]

....


```

#### Builtin Configuration Values

SERVER_NAME: the name and port number of the server.

JSON_SORT_KEYS : By default Flask will serialize JSON objects in a way that the keys are ordered.

- [reference¶](http://flask.pocoo.org/docs/0.12/config/)

## Run Flask

### Run flask for develop

```
$ flask run
```

In flask, Default port is `5000`

### Run flask for production

## Reference

Offical Website

- [Layout](<https://www.figma.com/file/v2iTCFTkqXkGPRPunhZdfT/Forum-Concept-for-Alem.school-(Community)?type=design&node-id=0%3A1&mode=design&t=2kgwJsoscAh7PYqU-1>)
- [Flask](http://flask.pocoo.org/)
- [Flask-SQLalchemy](http://flask-sqlalchemy.pocoo.org/2.1/)
