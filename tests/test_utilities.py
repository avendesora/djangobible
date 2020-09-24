import pytest

from django_scripture_index.constants import BookOfTheBible
from django_scripture_index.errors import InvalidVerseError
from django_scripture_index.utilities import get_book_chapter_verse
from django_scripture_index.utilities import get_scripture_reference_string
from django_scripture_index.utilities import get_verse_id


@pytest.fixture
def verse_id():
    return 1001001


@pytest.fixture
def invalid_verse_id():
    return 1100100


@pytest.fixture
def book():
    return BookOfTheBible.GENESIS


@pytest.fixture
def chapter():
    return 1


@pytest.fixture
def verse():
    return 1


@pytest.fixture
def invalid_chapter():
    return 100


@pytest.fixture
def invalid_verse():
    return 100


def test_get_verse_id(book, chapter, verse, verse_id):
    # Given a book of the Bible, a chapter number, and a verse number

    # When the get_verse_id() function is called
    actual_verse_id = get_verse_id(book, chapter, verse)

    # Then the verse id is the appropriate integer value
    assert verse_id == actual_verse_id


def test_get_verse_id_invalid(book, invalid_chapter, invalid_verse):
    # Given a book of the Bible, a chapter number, and a verse number that is not valid

    # When the get_verse_id() function is called, Then an exception is raised.
    with pytest.raises(InvalidVerseError):
        get_verse_id(book, invalid_chapter, invalid_verse)


def test_get_book_chapter_verse(book, chapter, verse, verse_id):
    # Given a verse id

    # When the get_book_chapter_verse() function is called
    actual_book, actual_chapter, actual_verse = get_book_chapter_verse(verse_id)

    # Then the book is the appropriate BookOfTheBible ENUM value
    assert book == actual_book

    # And the chapter number is the appropriate int value
    assert chapter == actual_chapter

    # And the verse number is the appropriate int value
    assert verse == actual_verse


def test_get_book_chapter_verse_invalid(invalid_verse_id):
    # Given an invalid verse id

    # When the get_book_chapter_verse() function is called, Then an exception is raised.
    with pytest.raises(InvalidVerseError):
        get_book_chapter_verse(invalid_verse_id)


def test_get_scripture_reference_string(verse_id):
    # Given a verse id

    # When the get_scripture_reference_string() function is called
    scripture_reference = get_scripture_reference_string(verse_id)

    # Then the scripture reference string is the appropriate value.
    assert scripture_reference == 'Genesis 1:1'


def test_get_scripture_reference_string_invalid(invalid_verse_id):
    # Given an invalid verse id

    # When the get_scripture_reference_string() function is called, Then an exception is thrown
    with pytest.raises(InvalidVerseError):
        get_scripture_reference_string(invalid_verse_id)
