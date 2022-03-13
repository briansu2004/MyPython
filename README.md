# MyPython

My Python

## My Python project (Data Science, Machine Learning, AI)

- Created a Python data science POC for a large supermarket chain client

  - Scraped neighborhood data from Wiki, acquired latitudes and longitudes data from the Geocoder, and retrieved location & venues data with Foursquare Places API.
  - Used k-means clustering to categorize and provided the recommendations.

- Built a Python AI POC for a government client to predict how much percent the issued parking tickets can be paid
  - Collected the data from various sources
  - Filtered out the outliers
  - Split for training and testing
  - Used a few algorithms and chose the best model which has the best Area Under the ROC Curve.

## pep8 style guide

https://peps.python.org/pep-0008/

How to follow pep8?

- Use inline comments sparingly.
- Write inline comments on the same line as the statement they refer to.
- Separate inline comments by two or more spaces from the statement.
- Start inline comments with a # and a single space, like block comments.
- Don't use them to explain the obvious.

### How to enforce PEP8 in VScode?

Install autopep8.py

Then activate the same env as interpreter in your VScode.

Select your code with ctrl+a and then do right click mouse you will get the formatting option.

Also make sure that you have python and intelisense extension installed from the extension market place of VScode.

```
pip install pep8
```

## Pylint

```
pip install pylint
```

Scan all files in the folder myfolder

```
pylint ./myfolder
```

Pylin a single file

```
(venv) C:\Code\MyPython\Django-Flask-FastAPI\fastapi-app>pylint database.py
************* Module database
database.py:10:0: C0304: Final newline missing (missing-final-newline)
database.py:1:0: C0114: Missing module docstring (missing-module-docstring)

-----------------------------------
Your code has been rated at 7.14/10
```

### Hint

```
#pylint: disable=<pylint_error_code_to_be_disabled>
```

### pylint_runner

```
pip install pylint_runner
```

```
pylint_runner
```

## Python Framework : Django vs Flask vs FastAPI

Keywords

```
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

## Python unit test for CI/CD pipeline

### unittest - Unit testing framework

The unittest unit testing framework was originally inspired by JUnit and has a similar flavor as major unit testing frameworks in other languages. It supports test automation, sharing of setup and shutdown code for tests, aggregation of tests into collections, and independence of the tests from the reporting framework.

To achieve this, unittest supports some important concepts in an object-oriented way:

test fixture

A test fixture represents the preparation needed to perform one or more tests, and any associated cleanup actions. This may involve, for example, creating temporary or proxy databases, directories, or starting a server process.

test case

A test case is the individual unit of testing. It checks for a specific response to a particular set of inputs. unittest provides a base class, TestCase, which may be used to create new test cases.

test suite

A test suite is a collection of test cases, test suites, or both. It is used to aggregate tests that should be executed together.

test runner

A test runner is a component which orchestrates the execution of tests and provides the outcome to the user. The runner may use a graphical interface, a textual interface, or return a special value to indicate the results of executing the tests.

```
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
```

### pytest

The pytest framework makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries.

```
def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 5
```

## Tricks

`mylist = ['a'] * 6`

set's symmetric_difference, symmetric_difference_update

frozenset

`from timeit import default_timer as timer`

`from collections import Counter`

`from collections import namedtuple`

`from collections import OrderedDict`

`from collections import defaultdict`

`from collections import deque`

`from itertools import product`

`from itertools import permutations`

`from itertools import combinations, combinations_with_replacement`

`from itertools import accumulate`

`from itertools import groupby`

`from itertools import count, cycle, repeat`

`import operator`

`from functools import reduce`

## VSCode extensions for Python

Python (Microsoft)

Python Preview

Tabnine

Python Docstring Generator

Python Indent

Python Snippets

Better Comments

Bracket Pair Colorizer 2

Python Test Explorer for Visual Studio Code

Python Type Hint

Jupyter

## Tips

- Use Modules and Packages
- One Class = One File
- Group Related Functionality Together
- Separate Utility & Helper Functions
- Organize Imports
