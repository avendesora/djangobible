# djangobible

The djangobible library is a Django app that wraps the [pythonbible](https://github.com/avendesora/python-bible) library and provides models, managers, and other tools to easily index an object by a scripture reference.

[![PyPI version](https://img.shields.io/pypi/v/djangobible?color=blue&logo=pypi&logoColor=lightgray)](https://pypi.org/project/djangobible/)
[![license MIT](https://img.shields.io/badge/license-MIT-orange.svg)](https://opensource.org/licenses/MIT)

![Django CI](https://github.com/avendesora/django-bible/workflows/Django%20CI/badge.svg)
![CodeQL](https://github.com/avendesora/django-bible/workflows/CodeQL/badge.svg)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/ca34603bdaf8446ba288430b69092093)](https://app.codacy.com/gh/avendesora/django-bible?utm_source=github.com&utm_medium=referral&utm_content=avendesora/django-bible&utm_campaign=Badge_Grade_Settings)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/83a28131bf6642ed9e439344122686fc)](https://www.codacy.com/gh/avendesora/django-bible/dashboard?utm_source=github.com&utm_medium=referral&utm_content=avendesora/django-bible&utm_campaign=Badge_Coverage)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![Python 3.9](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9-blue?logo=python&logoColor=lightgray)](https://www.python.org/downloads/release/python-390/)

## Installation

```shell script
pip install djangobible
```

### Optional Dependencies

If the [defusedxml](https://github.com/tiran/defusedxml) library is installed, djangobible/pythonbible will use it to parse XML files rather than the builtin xml.etree library.

To install djangobible with all optional dependencies, use the following command.

```shell script
pip install djangobible[all]
```

### Python 3.6

Python 3.6 is not officially supported (djangobible is only tested on Python 3.7+). However, djangobible should work on Python 3.6 if you have the dataclasses library installed:

```shell script
pip install dataclasses
```

If you are using Python 3.7+, the dataclasses library is included in the Python standard library, and you do not need to explicitly install the dataclasses library.

## Features

coming soon...
