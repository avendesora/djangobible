import pythonbible as bible
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models


class VerseRelation(models.Model):
    verse = models.PositiveIntegerField(null=False, blank=False)

    # Below the mandatory fields for generic relation
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    class Meta:
        db_table = u"verse_relation"

    def save(self, *args, **kwargs):
        if not bible.is_valid_verse_id(self.verse):
            raise bible.InvalidVerseError(verse_id=self.verse)

        super(VerseRelation, self).save(*args, **kwargs)


class ScriptureIndexedModel(models.Model):
    verses = GenericRelation(VerseRelation)

    class Meta:
        abstract = True

    def add_verse(self, verse_id):
        # will raise an error if object.id is null
        VerseRelation(content_object=self, verse=verse_id).save()

    @property
    def verse_ids(self):
        return [verse_relation.verse for verse_relation in self.verses.all()]
