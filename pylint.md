# Pylint

```dos
pip install pylint
```

Scan all files in the folder myfolder

```dos
pylint ./myfolder
```

Pylint a single file

```dos
(venv) C:\Code\MyPython\Django-Flask-FastAPI\fastapi-app>pylint database.py
************* Module database
database.py:10:0: C0304: Final newline missing (missing-final-newline)
database.py:1:0: C0114: Missing module docstring (missing-module-docstring)

-----------------------------------
Your code has been rated at 7.14/10
```

## Hint

```dos
#pylint: disable=<pylint_error_code_to_be_disabled>
```

## pylint_runner

```dos
pip install pylint_runner
```

```dos
pylint_runner
```
