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


class ScriptureIndexedModelManager(models.Manager):
    def filter_by_verse_ids(self, verse_ids):
        content_type = ContentType.objects.get_for_model(self.model)
        verse_relations = VerseRelation.objects.filter(
            content_type=content_type, verse__in=verse_ids
        )
        object_ids = verse_relations.values_list("object_id", flat=True)
        return self.get_queryset().filter(pk__in=object_ids)


class ScriptureIndexedModel(models.Model):
    verses = GenericRelation(VerseRelation)
    objects = ScriptureIndexedModelManager()

    class Meta:
        """ScriptureIndexed Model is an abstract model."""

        abstract = True

    def add_verse(self, verse_id):
        # will raise an error if object.id is null
        VerseRelation(content_object=self, verse=verse_id).save()

    def set_verses(self, verse_ids):
        # Delete any existing verse relations
        self.verses.all().delete()

        # Create new verse relation objects
        verse_relations = [
            VerseRelation(content_object=self, verse=verse_id)
            for verse_id in verse_ids
        ]


        VerseRelation.objects.bulk_create(verse_relations)

    @property
    def verse_ids(self):
        return [verse_relation.verse for verse_relation in self.verses.all()]
