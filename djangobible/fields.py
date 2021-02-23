from typing import Callable, List, Optional, Union

import pythonbible as bible
from django import forms
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.functional import cached_property

from .validators import validate_verse


class VerseField(models.IntegerField):
    def get_prep_value(self, value):
        if value is None:
            return None

        if isinstance(value, str):
            validate_verse(value)
            value = bible.convert_references_to_verse_ids(bible.get_references(value))[
                0
            ]
        elif isinstance(value, int):
            if not bible.is_valid_verse_id(value):
                raise ValidationError(f"{value} is not a valid verse id.")

        return super().get_prep_value(value)

    @cached_property
    def validators(self) -> List[Callable]:
        return [validate_verse]

    def to_python(self, value: Optional[Union[int, str]]) -> Optional[str]:
        if value is None or isinstance(value, str):
            return value

        return bible.format_scripture_references(
            bible.convert_verse_ids_to_references([value])
        )

    def from_db_value(
        self, value: Optional[Union[int, str]], expression, connection
    ) -> Optional[str]:
        return self.to_python(value)

    def formfield(self, **kwargs) -> forms.Field:
        return super().formfield(
            **{
                "form_class": forms.CharField,
                **kwargs,
            }
        )

    def get_db_prep_value(
        self, value: Optional[Union[int, str]], *args, **kwargs
    ) -> Optional[int]:
        if value is None:
            return None

        if isinstance(value, str):
            references = bible.get_references(value)
            verse_ids = bible.convert_references_to_verse_ids(references)

            if verse_ids is None or len(verse_ids) == 0:
                raise ValidationError(
                    f"{value} does not contain a valid Scripture reference."
                )

            value = verse_ids[0]

        if not bible.is_valid_verse_id(value):
            raise ValidationError(f"{value} is not a valid verse id.")

        return value
