# djangobible

The djangobible library is a Django app that wraps the [pythonbible](https://github.com/avendesora/pythonbible) library and provides models, managers, and other tools to easily index an object by a scripture reference.

[![PyPI version](https://img.shields.io/pypi/v/djangobible?color=blue&logo=pypi&logoColor=lightgray)](https://pypi.org/project/djangobible/)
[![license MIT](https://img.shields.io/badge/license-MIT-orange.svg)](https://opensource.org/licenses/MIT)

![Django CI](https://github.com/avendesora/djangobible/workflows/Django%20CI/badge.svg)
![CodeQL](https://github.com/avendesora/djangobible/workflows/CodeQL/badge.svg)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/ca34603bdaf8446ba288430b69092093)](https://app.codacy.com/gh/avendesora/djangobible?utm_source=github.com&utm_medium=referral&utm_content=avendesora/djangobible&utm_campaign=Badge_Grade_Settings)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/83a28131bf6642ed9e439344122686fc)](https://www.codacy.com/gh/avendesora/djangobible/dashboard?utm_source=github.com&utm_medium=referral&utm_content=avendesora/djangobible&utm_campaign=Badge_Coverage)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![Python 3.9](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9-blue?logo=python&logoColor=lightgray)](https://www.python.org/downloads/release/python-390/)
[![Django 3.0+](https://img.shields.io/badge/Django-3.0%20%7C%203.1%20%7C%203.2-blue)](https://www.djangoproject.com/download/)

## Installation

Pip install the djangobible library.

```shell script
pip install djangobible
```

Add djangobible to your Django project's ``INSTALLED_APPS`` setting:

```python
INSTALLED_APPS = [
    ...,  # other apps
    "djangobible",
]
```

Run the django migrations for djangobible

```
./manage.py migrate djangobible
```

### Settings

There currently are no settings (other than INSTALLED_APPS) related to the djangobible project. In the future, it would be nice to have settings that determine things like the available versions of the Bible and the default version.

Also, once support is implemented for multiple locales and languages, there could be related settings for that functionality.

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

### Django versions

The djangobible library is actively tested on Django 3.0 and 3.1, and support for Django 3.2 is planned. It may work on previous versions, but it has not been tested on other versions. 

## Features

The djangobible library is a complete wrapper for the [pythonbible](https://github.com/avendesora/pythonbible) library, so importing the djangobible library as:

```python
import djangobible as bible
```

will provide all the same functionality as importing the pythonbible library as:

```python
import pythonbible as bible
```

This includes features such as:
- Searching text for Scripture references
- Converting a normalized scripture reference into a list of integer verse ids
- Converting a list of verse id integers into a list of normalized scripture references
- Converting a list of normalized scripture references into a formatted string scripture reference 
- Retrieving the Biblical text (in one or more open-source or public domain versions) for a given verse ID integer

For more information, see the [pythonbible documentation](https://github.com/avendesora/pythonbible).

In addition, the djangobible library includes the following features:

### Template Tags

There are currently two template tags provided by the djangobible library: ``verse_reference`` and ``verse_text``.

#### verse_reference

The ``verse_reference`` template tag, given a verse ID and a Bible version, returns the appropriate Scripture reference string.

For example, given ``verse_id = 1001001`` and ``version = djangobible.Version.KING_JAMES``, the following snippet from a Django template:

```html
{% load verse_tags %}
...
{% verse_reference verse_id version=version %}
```

would display:

```
Genesis 1:1
```

The version parameter is optional, and the current default is King James, though that will ideally be configurable in the future.

There is another optional parameter, ``full_title``, which is a boolean flag to determine whether to display the long version or the short version of the book of the Bible title. It defaults to ``False``, which displays the short version. For example, given ``verse_id = 1001001`` and ``version = djangobible.Version.KING_JAMES`` and ``full_title = True``, the following snippet from a Django template:

```html
{% load verse_tags %}
...
{% verse_reference verse_id version=version full_title=full_title %}
```

would display:

```
The First Book of Moses, called Genesis 1:1
```

#### verse_text

The ``verse_text`` template tag, given a verse ID and a Bible version, returns the appropriate text of that Bible verse.

For example, given ``verse_id = 1001001`` and ``version = djangobible.Version.KING_JAMES``, the following snippet from a Django template:

```html
{% load verse_tags %}
...
{% verse_text verse_id %}
```

would display:

```
In the beginning God created the heaven and the earth.
```

The version parameter is optional, and the current default is King James, though that will ideally be configurable in the future.

### One-to-many style relationships between verses and Django models

For situations where an instance of a Django model needs to be associated with a single verse, that Django model can have a field of type ``VerseField``.

For example:

```python
from django.db import models

import djangobible as bible


class MyModel(models.Model):
    ...  # other fields
    
    verse = bible.VerseField()
```

The underlying implementation of ``VerseField`` is an ``IntegerField`` which stores the verse ID of the associated verse.

Having this custom field type provides several benefits:
- The Django admin (and Wagtail) form contains a text field for the verse rather than an integer field and allows the user to enter the Scripture reference text rather than the verse id, which they may not know. It then validates that text to ensure it references one, and only one, verse.
- As just mentioned, this allows for validation, not only that the value is one, and only one, verse id, but that it is also a valid verse id (i.e. that it represents a book, chapter, and verse of the Bible that actually exists).
- More readable query filters (e.g. ``MyModel.objects.filter(verse=1001001)`` is valid, but so is ``MyModel.objects.filter(verse="Genesis 1:1")``).

You can set the verse field with either the int verse ID or the string reference:

```python
my_object = MyModel.objects.create(name="my object")
my_object.verse = 1001001
my_object.save()
```

or

```python
my_object = MyModel.objects.create(name="my object")
my_object.verse = "Genesis 1:1"
my_object.save()
```

You can filter the objects in the query set by either the int verse ID or the string reference:

```python
MyModel.objects.filter(verse=1001001)
```

or

```python
MyModel.objects.filter(verse="Genesis 1:1")
```

In any of the above examples, if the verse is not a valid verse ID integer or string reference for a single verse, then a ``ValidationError`` will be raised.

### Many-to-many style relationships between verses and Django models

> **WARNING**: This is still a work in progress, and this functionality does not yet exist in a stable form.

There are situations where an instance of a Django model needs to be associated with multiple verses. The current intended solution, inspired by the [django-taggit](https://github.com/jazzband/django-taggit) library, is to implement this feature in such a way that you would add this relationship to your model like:

```python
from django.db import models

import djangobible as bible


class MyModel(models.Model):
    ...  # other fields

    verses = bible.VerseManager()
```

Then you could add, remove, and reference those verses with something like:

```
>>> my_object = MyModel.objects.create(name="My Object")
>>> my_object.verses.add("Genesis 1:1-3")
>>> my_object.verses.all()
[<Verse: Genesis 1:1>, <Verse: Genesis 1:2>, <Verse: Genesis 1:3>]
>>> my_object.verses.remove("Genesis 1:2")
>>> my_object.verses.all()
[<Verse: Genesis 1:1>, <Verse: Genesis 1:3>]
>>> MyModel.objects.filter(verses__in=[1001001])
[<MyModel: My Object>]
```

Ideally, the form field would be a text field where the user could enter a list of Scripture references (e.g. "Genesis 1:1,3-10;Psalm 119;Luke 2:1-18;John 3:16")