# WildCard Matching - LeetCode

### Installing project dependencies
```shell
pip install -r requirements_dev.txt
```

### Running the app
```shell
python wildcard_matching.py
```

### Installing pre-commit
```shell
pre-commit install
```

### Running pre-commit over staged files
```shell
pre-commit run --all-files
```

### Running tests
```shell
pytest
```

### Running coverage
```shell
coverage run -m pytest
```

### Reporting coverage
```shell
coverage report -m
```

### Reporting coverage to html
```shell
coverage html
```

To view the html page, run:

```shell
cd htmlcov
python -m http.server 8080
```
and go to http://localhost:8080.
