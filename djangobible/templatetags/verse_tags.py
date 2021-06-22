from typing import Optional

import pythonbible as bible
from django import template

register = template.Library()


@register.simple_tag
def verse_reference(verse_id: int, **kwargs) -> str:
    """For a given verse id return the formatted scripture reference string

    :param verse_id:
    :return: the scripture reference string for the given verse id
    """
    book: bible.Book
    chapter: int
    verse: int
    book, chapter, verse = bible.get_book_chapter_verse(verse_id)

    version_id: Optional[str] = kwargs.get("version")

    if version_id:
        kwargs["version"] = _get_version(version_id)

    reference = bible.NormalizedReference(
        book,
        chapter,
        verse,
        chapter,
        verse
    )

    return bible.format_single_reference(reference, **kwargs)


@register.simple_tag
def verse_text(verse_id: int, **kwargs) -> str:
    """For a given verse id and version, return the verse text string

    :param verse_id:
    :return: the verse text for the given verse id and version
    """
    version_id: Optional[str] = kwargs.get("version")
    text: str = ""

    if version_id is not None:
        text = bible.get_verse_text(verse_id, _get_version(version_id))
    else:
        text = bible.get_verse_text(verse_id)

    include_verse_numbers: bool = kwargs.get("include_verse_numbers", False)

    if include_verse_numbers:
        text = f"{bible.get_verse_number(verse_id)}. {text}"

    return text


def _get_version(version_id: str) -> Optional[bible.Version]:
    try:
        return bible.Version[version_id]
    except KeyError:
        try:
            return bible.Version(version_id)
        except ValueError:
            pass

    return None
