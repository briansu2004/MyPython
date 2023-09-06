# Python Frameworks for APIs: Django vs Flask vs FastAPI

Keywords

```text
Flask
Flask-SQLAlchemy
SQLite
autopep8

FastAPI
ASGI web server
uvicorn
Jinjia2
starlette

Django
```

Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions.

SQLAlchemy is an open-source SQL toolkit and object-relational mapper for the Python programming language released under the MIT License.

Flask-SQLAlchemy is an extension for Flask that adds support for SQLAlchemy to your application.

SQLite is a database engine, written in the C language. It is not a standalone app; rather, it is a library that software developers embed in their apps. As such, it belongs to the family of embedded databases.

autopep8 automatically formats Python code to conform to the PEP 8 style guide.

FastAPI is a Web framework for developing RESTful APIs in Python. FastAPI is based on Pydantic and type hints to validate, serialize, and deserialize data, and automatically auto-generate OpenAPI documents. It fully supports asynchronous programming and can run with Uvicorn and Gunicorn.

The Asynchronous Server Gateway Interface (ASGI) is a calling convention for web servers to forward requests to asynchronous-capable Python programming language frameworks, and applications. It is built as a successor to the Web Server Gateway Interface (WSGI).

Uvicorn is an ASGI web server implementation for Python. Until recently Python has lacked a minimal low-level server/application interface for async frameworks. The ASGI specification fills this gap, and means we're now able to start building a common set of tooling usable across all async frameworks.

FastAPI does async!

Starlette is a lightweight ASGI framework/toolkit, which is ideal for building async web services in Python. It is production-ready, and gives you the following: A lightweight, low-complexity HTTP web framework. WebSocket support.

Jinja is a web template engine for the Python programming language. It was created by Armin Ronacher and is licensed under a BSD License. Jinja is similar to the Django template engine but provides Python-like expressions while ensuring that the templates are evaluated in a sandbox.

Jinja2 is a full-featured template engine for Python. It has full unicode support, an optional integrated sandboxed execution environment, widely used and BSD licensed.

FastAPI provides OOTB swagger, i.e. http://127.0.0.1:8000/docs

Django is a Python-based free and open-source web framework that follows the model–template–views architectural pattern. It is maintained by the Django Software Foundation, an independent organization established in the US as a 501 non-profit.

Django has an OOTB admin module.