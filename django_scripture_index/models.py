from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class ScriptureReference(models.Model):
    verse = models.PositiveIntegerField(null=False, blank=False)

    # Below the mandatory fields for generic relation
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    class Meta:
        db_table = u'scripture_reference'

    # TODO - make sure the verse is valid (in constants.VERSE_IDS) before saving
