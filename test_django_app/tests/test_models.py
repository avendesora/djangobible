import pytest
from django.core.exceptions import ValidationError

import djangobible as bible
from test_django_app.models import TestObject, TestSingleVerseObject


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


def test_object_str():
    # Given a test object with a name
    test_object = TestObject()
    test_object.name = "test name"

    # When calling the __str__ method on the test object
    test_object_string = str(test_object)

    # Then the string representation of the test object equals the name.
    assert test_object_string == test_object.name


@pytest.mark.django_db
def test_single_verse_object_filter_by_verse(
    test_single_verse_object, valid_verse_id: int
) -> None:
    # Given a valid_verse_id and a matching reference string
    reference_string: str = bible.format_scripture_references(
        bible.convert_verse_ids_to_references([valid_verse_id])
    )
    # When we get the test objects by the int verse id and the test objects by the reference string
    test_objects_by_id = TestSingleVerseObject.objects.filter(verse=valid_verse_id)
    test_objects_by_reference = TestSingleVerseObject.objects.filter(
        verse=reference_string
    )

    # Then both collections of objects should be the same
    assert test_objects_by_id.count() == test_objects_by_reference.count()

    for i, test_object_a in enumerate(test_objects_by_id):
        test_object_b = test_objects_by_reference[i]
        assert test_object_a == test_object_b
        assert test_object_a == test_single_verse_object
        assert test_object_b == test_single_verse_object


@pytest.mark.django_db
def test_single_verse_object_filter_by_verse_invalid(invalid_verse_id: int) -> None:
    # Given an invalid reference and verse id

    # When attempting to filter the objects by the invalid reference
    # Then a validation error is raised.
    with pytest.raises(ValidationError):
        TestSingleVerseObject.objects.filter(verse="invalid reference")

    # When attempting to filter the objects by the invalid verse id
    # Then a validation error is raised.
    with pytest.raises(ValidationError):
        TestSingleVerseObject.objects.filter(verse=invalid_verse_id)


@pytest.mark.django_db
def test_single_verse_object_set_verse_by_id(
    test_single_verse_object, valid_verse_id: int
) -> None:
    # Given a test single verse object and a valid verse id
    # Given the reference string associated with that verse id
    reference_string: str = bible.format_scripture_references(
        bible.convert_verse_ids_to_references([valid_verse_id])
    )

    # Given that the current verse associated with the object is not the same as the given verse id
    assert test_single_verse_object.verse != valid_verse_id
    assert test_single_verse_object.verse != reference_string

    # When we set the verse on the test object to be the verse id
    test_single_verse_object.verse = valid_verse_id
    test_single_verse_object.save()

    # Then the verse associated with the object matches the verse id
    assert test_single_verse_object.verse == valid_verse_id

    # And the verse associated with the object after retrieving it from the DB again matches the reference string
    updated_test_single_verse_object: TestSingleVerseObject = (
        TestSingleVerseObject.objects.get(id=test_single_verse_object.id)
    )
    assert updated_test_single_verse_object.verse == reference_string


@pytest.mark.django_db
def test_single_verse_object_set_verse_by_reference(
    test_single_verse_object, reference: str
) -> None:
    # Given a test single verse object and a verse reference
    # Given the verse id associated with that reference
    verse_id = bible.convert_references_to_verse_ids(bible.get_references(reference))[0]

    # Given that the current verse associated with the object is not the same as the given reference
    assert test_single_verse_object.verse != reference
    assert test_single_verse_object.verse != verse_id

    # When we set the verse on the test object to be the reference
    test_single_verse_object.verse = reference
    test_single_verse_object.save()

    # Then the verse associated with the object matches the reference
    assert test_single_verse_object.verse == reference

    # And the verse associated with the object after retrieving it from the DB again still matches the reference
    updated_test_single_verse_object: TestSingleVerseObject = (
        TestSingleVerseObject.objects.get(id=test_single_verse_object.id)
    )
    assert updated_test_single_verse_object.verse == reference


@pytest.mark.django_db
def test_single_verse_object_set_verse_by_reference_invalid(
    test_single_verse_object, invalid_verse_id: int
) -> None:
    # Given a test single verse object and an invalid verse id and reference

    # When we set the verse on the test object to be the invalid reference
    # Then a validation error is raised.
    with pytest.raises(ValidationError):
        test_single_verse_object.verse = "invalid reference"
        test_single_verse_object.save()

    # When we set the verse on the test object to be the invalid verse id
    # Then a validation error is raised
    with pytest.raises(ValidationError):
        test_single_verse_object.verse = invalid_verse_id
        test_single_verse_object.save()
