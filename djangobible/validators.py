"""Validators for djangobible custom Fields."""

from __future__ import annotations

from django.core.exceptions import ValidationError
from pythonbible import (
    NormalizedReference,
    convert_references_to_verse_ids,
    get_references,
)


def validate_verse(verse_value: str | None) -> None:
    """Validate that the given value is a valid string representation of a verse."""
    if verse_value is None:
        return

    references: list[NormalizedReference] = get_references(verse_value)

    if not references:
        raise ValidationError("Not a valid reference.")

    if len(references) > 1:
        raise ValidationError("Only single verse references allowed.")

    verse_ids: list[int] = convert_references_to_verse_ids(references)

    if len(verse_ids) > 1:
        raise ValidationError("Only single verse references allowed.")
