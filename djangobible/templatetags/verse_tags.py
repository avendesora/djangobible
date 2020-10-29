import djangobible as bible

from django import template

register = template.Library()


@register.simple_tag
def verse_reference(verse_id):
    """For a given verse id return the formatted scripture reference string

    :param verse_id:
    :return:
    """
    book, chapter, verse = bible.get_book_chapter_verse(verse_id)
    return f"{book.title} {chapter}:{verse}"


@register.simple_tag
def verse_text(verse_id, version=None):
    """For a given verse id and version, return the verse text string

    :param verse_id:
    :param version:
    :return:
    """
    try:
        version = bible.Version[version]
    except KeyError:
        try:
            version = bible.Version(version)
        except ValueError:
            pass

    if version is not None:
        parser = bible.get_parser(version=version)
    else:
        parser = bible.get_parser()

    return parser.get_verse_text(verse_id)
