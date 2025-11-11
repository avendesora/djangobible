"""Custom Django managers and models for djangobible."""

from __future__ import annotations

import pythonbible as bible
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models


class VerseRelation(models.Model):
    """Custom Django model for a verse relation."""

    verse = models.PositiveIntegerField(null=False, blank=False)

    # Below the mandatory fields for generic relation
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    class Meta:
        """Set the DB table name."""

        db_table = "verse_relation"

    def save(
        self: VerseRelation,
        force_insert: bool = False,
        force_update: bool = False,
        using: str | None = None,
        update_fields: list[str] | None = None,
    ) -> None:
        """Save the instance to the DB."""
        if not bible.is_valid_verse_id(self.verse):
            raise bible.InvalidVerseError(verse_id=self.verse)

        super().save(force_insert, force_update, using, update_fields)


class ScriptureIndexedModelManager(models.Manager):
    """Custom Django model manager for ScriptureIndexedModel."""

    def filter_by_verse_ids(
        self: ScriptureIndexedModelManager,
        verse_ids: list[int] | None,
    ) -> models.QuerySet:
        """Return the Query Set for the objects related to the given verse ids."""
        content_type = ContentType.objects.get_for_model(self.model)
        verse_relations = VerseRelation.objects.filter(
            content_type=content_type,
            verse__in=verse_ids,
        )
        object_ids = verse_relations.values_list("object_id", flat=True)
        return self.get_queryset().filter(pk__in=object_ids)


class ScriptureIndexedModel(models.Model):
    """An abstract Django model with a many-to-many relationship for verses."""

    verses = GenericRelation(VerseRelation)
    objects = ScriptureIndexedModelManager()

    class Meta:
        """ScriptureIndexed Model is an abstract model."""

        abstract = True

    def add_verse(self: ScriptureIndexedModel, verse_id: int | None) -> None:
        """Add a verse to the related verses."""
        VerseRelation(content_object=self, verse=verse_id).save()

    def set_verses(self: ScriptureIndexedModel, verse_ids: list[int] | None) -> None:
        """Overwrite the related verses with the given list of verse ids."""
        self.verses.all().delete()

        if not verse_ids:
            return

        verse_relations = [
            VerseRelation(content_object=self, verse=verse_id) for verse_id in verse_ids
        ]

        VerseRelation.objects.bulk_create(verse_relations)

    @property
    def verse_ids(self: ScriptureIndexedModel) -> list[int]:
        """Return the list of related verse id integers."""
        return [verse_relation.verse for verse_relation in self.verses.all()]
