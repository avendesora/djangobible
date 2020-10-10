from django.db import models

from djangobible.models import ScriptureIndexedModel


class TestObject(ScriptureIndexedModel):
    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.name
