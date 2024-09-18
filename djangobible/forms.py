"""Custom Django forms for djangobible models."""

from __future__ import annotations

from typing import Any

import pythonbible as bible
from django import forms
from django.core.exceptions import ValidationError

from djangobible.models import ScriptureIndexedModel


class ScriptureIndexedModelAdminForm(forms.ModelForm):
    """Custom Django form for ScriptureIndexedModel."""

    reference = forms.CharField(max_length=255)

    def __init__(
        self: ScriptureIndexedModelAdminForm,
        *args: dict,
        **kwargs: dict,
    ) -> None:
        """Initialize the form with the initial reference."""
        verse_ids = kwargs["instance"].verses.values_list("verse", flat=True)  # type: ignore[attr-defined]

        kwargs.update(
            initial={
                "reference": bible.format_scripture_references(
                    bible.convert_verse_ids_to_references(list(verse_ids)),
                ),
            },
        )

        super().__init__(*args, **kwargs)

    def clean(self: ScriptureIndexedModelAdminForm) -> dict:
        """Validate the reference field."""
        cleaned_data = super().clean()
        reference = cleaned_data.get("reference")
        references = bible.get_references(reference)

        if not bible.convert_references_to_verse_ids(references):
            error_message = f"{reference} does not contain a valid Scripture reference."
            raise ValidationError(error_message)

        return cleaned_data

    def save(
        self: ScriptureIndexedModel,
        commit: bool = True,
    ) -> Any:
        """Save the form and set the verses."""
        reference = self.cleaned_data["reference"]
        references = bible.get_references(reference)
        verse_ids = bible.convert_references_to_verse_ids(references)

        updated_object = super().save(commit=commit)  # type: ignore[misc]
        updated_object.set_verses(verse_ids)

        return updated_object

    class Meta:
        """Set the model and fields for the form."""

        model = ScriptureIndexedModel
        fields = "__all__"
