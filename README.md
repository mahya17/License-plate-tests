# License Plate Tests 🚘

A Python testing project that checks whether license plates meet the required validation rules.

## About the Project

The project reimplements the **Vanity Plates** problem from an earlier CS50 problem set and focuses on testing the `is_valid()` function.

The `is_valid()` function receives a string and returns either `True` or `False` depending on whether the license plate meets the required rules.

The project also includes automated tests in `test_plates.py` to check different valid and invalid license plate cases.

## How It Works

The `is_valid()` function checks whether a given license plate is valid.

The tests are designed to cover different cases and make sure the function correctly handles both valid and invalid inputs.

For example:

```text id="d8b8e3"
is_valid("CS50") → True
is_valid("HELLO") → True
```

The tests are written in a separate `test_plates.py` file and can be run using `pytest`.

## What I Practiced

* Writing functions
* Boolean values
* `return`
* Conditional statements
* String validation
* Importing functions between files
* Writing automated tests
* Using `pytest`
* Testing valid and invalid inputs
* Designing tests to catch incorrect implementations

## Technologies

* Python
* pytest

## Testing

Run the following command to execute the tests:

```bash id="3w2b9x"
pytest test_plates.py
```

## Course

This project was completed as part of **CS50's Introduction to Programming with Python** by Harvard University.
