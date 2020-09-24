from django_scripture_index.constants import BookOfTheBible, VERSE_IDS
from django_scripture_index.errors import InvalidVerseError


def get_verse_id(book_of_the_bible, chapter_number, verse_number):
    verse_id = int(book_of_the_bible) * 1000000 + chapter_number * 1000 + verse_number

    if verse_id not in VERSE_IDS:
        raise InvalidVerseError(
            f'{book_of_the_bible.name()} {chapter_number}:{verse_number} is not a valid Bible verse.'
        )

    return verse_id


def get_book_chapter_verse(verse_id):
    if verse_id not in VERSE_IDS:
        raise InvalidVerseError(f'{verse_id} is not a valid Bible verse ID.')

    book_of_the_bible = int(verse_id / 1000000)
    chapter_number = int(verse_id % 1000000 / 1000)
    verse_number = int(verse_id % 1000)

    return BookOfTheBible(book_of_the_bible), chapter_number, verse_number


def get_scripture_reference_string(verse_id):
    if verse_id not in VERSE_IDS:
        raise InvalidVerseError(f'{verse_id} is not a valid Bible verse ID.')

    book, chapter, verse = get_book_chapter_verse(verse_id)
    return f'{book.name()} {chapter}:{verse}'
