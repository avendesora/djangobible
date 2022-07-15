"""Django models for testing djangobible managers, models, and fields."""

from __future__ import annotations

from django.db import models

from djangobible.fields import VerseField
from djangobible.models import ScriptureIndexedModel


class TestObject(ScriptureIndexedModel):
    """Model for testing many-to-many verse relation with ScriptureIndexedModel."""

    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self: TestObject) -> str:
        """Return the name when the TestObject is referenced as a string."""
        return self.name


class TestSingleVerseObject(models.Model):
    """Model for testing single verse relation with VerseField."""

    name = models.CharField(max_length=255, null=False, blank=False)
    verse = VerseField(null=True, blank=True)

    def __str__(self: TestSingleVerseObject) -> str:
        """Return the name when the TestObject is referenced as a string."""
        return self.name
