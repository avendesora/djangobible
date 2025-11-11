"""Validators for djangobible custom Fields."""

from __future__ import annotations

from django.core.exceptions import ValidationError
from pythonbible import NormalizedReference
from pythonbible import convert_references_to_verse_ids
from pythonbible import get_references


def validate_verse(verse_value: str | None) -> None:
    """Validate that the given value is a valid string representation of a verse."""
    if verse_value is None:
        return

    references: list[NormalizedReference] = get_references(verse_value)

    if not references:
        error_message = "Not a valid reference."
        raise ValidationError(error_message)

    if len(references) > 1:
        error_message = "Only single verse references allowed."
        raise ValidationError(error_message)

    verse_ids: list[int] = convert_references_to_verse_ids(references)

    if len(verse_ids) > 1:
        error_message = "Only single verse references allowed."
        raise ValidationError(error_message)
