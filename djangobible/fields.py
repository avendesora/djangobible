"""Custom Django model fields for djangobible."""

from __future__ import annotations

from typing import Any, Callable

import pythonbible as bible
from django import forms
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.functional import cached_property

from djangobible.validators import validate_verse


class VerseField(models.Field):
    """Custom Django model field to represent a Verse."""

    def get_prep_value(self: VerseField, value: int | str | None) -> int:
        """Validate and convert the value to a verse id int."""
        if isinstance(value, str):
            validate_verse(value)
            value = bible.convert_references_to_verse_ids(
                bible.get_references(value),
            )[0]
        elif isinstance(value, int) and not bible.is_valid_verse_id(value):
            raise ValidationError(f"{value} is not a valid verse id.")

        return super().get_prep_value(value)

    @cached_property
    def validators(self: VerseField) -> list[Callable]:
        """Return the list of validators for this field."""
        return [validate_verse]

    def to_python(
        self: VerseField,
        value: int | str | None,
    ) -> str | None:
        """Convert the value into a text scripture reference."""
        if value is None or isinstance(value, str):
            return value

        return bible.format_scripture_references(
            bible.convert_verse_ids_to_references([value]),
        )

    def from_db_value(
        self: VerseField,
        value: int | str | None,
        expression: Any,
        connection: Any,
    ) -> str | None:
        """Convert the value from the DB."""
        return self.to_python(value)

    def formfield(self: VerseField, **kwargs: Any) -> forms.Field:
        """Make sure the form field is a CharField."""
        return super().formfield(
            **{
                "form_class": forms.CharField,
                **kwargs,
            },
        )

    def get_db_prep_save(
        self: VerseField,
        value: Any,
        **kwargs: Any,
    ) -> int | None:
        """Validate and convert the value to a verse id int before saving to the DB."""
        if not value:
            return None

        if isinstance(value, str):
            references = bible.get_references(value)
            verse_ids = bible.convert_references_to_verse_ids(references)

            if not verse_ids:
                raise ValidationError(
                    f"{value} does not contain a valid Scripture reference.",
                )

            value = verse_ids[0]

        if not bible.is_valid_verse_id(value):
            raise ValidationError(f"{value} is not a valid verse id.")

        return int(value)

    def get_internal_type(self: VerseField) -> str:
        """Return the internal type (IntegerField) for the VerseField field."""
        return "IntegerField"
