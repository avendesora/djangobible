"""The Django admin config for models in the djangobible library."""

from __future__ import annotations

from django.contrib import admin

from test_django_app.models import TestObject
from test_django_app.models import TestSingleVerseObject

admin.site.register(TestObject)
admin.site.register(TestSingleVerseObject)
