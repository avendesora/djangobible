from typing import List, Optional

import pythonbible as bible
from django.core.exceptions import ValidationError


def validate_verse(value: Optional[str]) -> None:
    if value is None:
        return

    references: List[bible.NormalizedReference] = bible.get_references(value)

    if not references:
        raise ValidationError("Not a valid reference.")

    if len(references) > 1:
        raise ValidationError("Only single verse references allowed.")

    verse_ids: List[int] = bible.convert_references_to_verse_ids(references)

    if not verse_ids:
        raise ValidationError("Not a valid reference.")

    if len(verse_ids) > 1:
        raise ValidationError("Only single verse references allowed.")
