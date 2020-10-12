import pytest

import djangobible as bible


@pytest.mark.django_db
def test_add_verse(test_object, valid_verse_id):
    # Given an object that can be indexed by scripture references
    # When a verse is added to that test_object
    test_object.add_verse(valid_verse_id)

    # Then that verse id appears in the list of verse ids
    assert test_object.verse_ids == [valid_verse_id]


@pytest.mark.django_db
def test_add_verse_invalid(test_object, invalid_verse_id):
    # Given an object that can be indexed by scripture references
    # When we attempt to add an invalid verse to that object
    # Then an error is raised
    with pytest.raises(bible.InvalidVerseError):
        test_object.add_verse(invalid_verse_id)


@pytest.mark.django_db
def test_add_verses_from_text_with_scripture_references(
    test_object, text_with_scripture_references, expected_verse_ids
):
    # Given a test_object and a text with scripture references
    # Get the references from the text and convert them to verse ids
    references = bible.get_references(text_with_scripture_references)
    verse_ids = bible.convert_references_to_verse_ids(references)

    # When we add all of the verse ids to the test object
    for verse_id in verse_ids:
        test_object.add_verse(verse_id)

    # Then the list of verse ids list matches
    actual_verse_ids = test_object.verse_ids
    assert actual_verse_ids == verse_ids
    assert actual_verse_ids == expected_verse_ids


@pytest.mark.django_db
def test_set_verses(test_object, expected_verse_ids):
    # Given a test object and a list of verse ids
    # When we set the test object's verses to be the verse ids
    test_object.set_verses(expected_verse_ids)

    # Then the verse ids list matches
    assert test_object.verse_ids == expected_verse_ids


@pytest.mark.django_db
def test_set_verses_deletes_existing(test_object, valid_verse_id, expected_verse_ids):
    # Given a test object and a valid verse id and a list of verse ids
    # When we add a verse to the test object
    test_object.add_verse(valid_verse_id)

    # And when we set the test object's verses to be the verse ids
    test_object.set_verses(expected_verse_ids)

    # Then the original verse id is not in the test object's verse ids list
    actual_verse_ids = test_object.verse_ids
    assert valid_verse_id not in actual_verse_ids

    # And then the actual verse ids is equal to expected verse ids
    assert actual_verse_ids == expected_verse_ids
