from django.db import models

from djangobible.fields import VerseField
from djangobible.models import ScriptureIndexedModel


class TestObject(ScriptureIndexedModel):
    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        """Return the name when the TestObject is referenced as a string."""
        return self.name


class TestSingleVerseObject(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    verse = VerseField()

    def __str__(self):
        """Return the name when the TestObject is referenced as a string."""
        return self.name
