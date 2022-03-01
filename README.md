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
