"""The Django admin config for models in the djangobible library."""

from __future__ import annotations

from django.contrib import admin

from djangobible.forms import ScriptureIndexedModelAdminForm
from test_django_app.models import TestObject, TestSingleVerseObject

admin.site.register(TestSingleVerseObject)


class TestObjectAdmin(admin.ModelAdmin):
    """Admin config for TestObject model."""

    form = ScriptureIndexedModelAdminForm


admin.site.register(TestObject, TestObjectAdmin)
