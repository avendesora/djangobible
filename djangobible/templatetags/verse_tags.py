from typing import Optional

import pythonbible as bible
from django import template

register = template.Library()


@register.simple_tag
def verse_reference(
    verse_id: int, version_id: str = None, full_title: bool = False
) -> str:
    """For a given verse id return the formatted scripture reference string

    :param verse_id:
    :param version_id: optional Bible version
    :param full_title: optional, defaults to False, if True use the long book title
    :return: the scripture reference string for the given verse id
    """
    book, chapter, verse = bible.get_book_chapter_verse(verse_id)
    kwargs = {"full_title": full_title}

    if version_id:
        kwargs["version"] = _get_version(version_id)

    return bible.format_single_reference(book, chapter, verse, chapter, verse, **kwargs)


@register.simple_tag
def verse_text(verse_id: int, version_id: str = None) -> str:
    """For a given verse id and version, return the verse text string

    :param verse_id:
    :param version_id:
    :return: the verse text for the given verse id and version
    """
    version: bible.Version = _get_version(version_id)

    if version is not None:
        return bible.get_verse_text(verse_id, version=version)

    return bible.get_verse_text(verse_id)


def _get_version(version_id: str) -> Optional[bible.Version]:
    try:
        return bible.Version[version_id]
    except KeyError:
        try:
            return bible.Version(version_id)
        except ValueError:
            pass

    return None
