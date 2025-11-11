"""Custom tags for djangobible."""

from __future__ import annotations

from contextlib import suppress

import pythonbible as bible
from django import template

register = template.Library()


@register.simple_tag
def verse_reference(verse_id: int, **kwargs: dict) -> str:
    """For a given verse id return the formatted scripture reference string.

    :param verse_id:
    :return: the scripture reference string for the given verse id
    """
    book: bible.Book
    chapter: int
    verse: int
    book, chapter, verse = bible.get_book_chapter_verse(verse_id)

    if version_id := kwargs.get("version"):
        kwargs["version"] = _get_version(version_id)  # type: ignore[arg-type,assignment]

    reference = bible.NormalizedReference(book, chapter, verse, chapter, verse)

    return bible.format_single_reference(reference, **kwargs)


@register.simple_tag
def verse_text(verse_id: int, **kwargs: dict) -> str:
    """For a given verse id and version, return the verse text string.

    :param verse_id:
    :return: the verse text for the given verse id and version
    """
    version_id: str | None = kwargs.get("version")  # type: ignore[assignment]
    text: str = (
        bible.get_verse_text(verse_id, _get_version(version_id))
        if version_id
        else bible.get_verse_text(verse_id)
    )
    include_verse_numbers: bool = kwargs.get("include_verse_numbers", False)  # type: ignore[assignment]

    return (
        f"{bible.get_verse_number(verse_id)}. {text}" if include_verse_numbers else text
    )


def _get_version(version_id: str) -> bible.Version | None:
    try:
        return bible.Version[version_id]
    except KeyError:
        with suppress(ValueError):
            return bible.Version(version_id)

    return bible.versions.DEFAULT_VERSION
