from django.core.exceptions import ValidationError
from django.test import TestCase

import djangobible as bible
from test_django_app.models import TestSingleVerseObject
from test_django_app.tests.factories import (
    TestObjectFactory,
    TestSingleVerseObjectFactory,
)

EXPECTED_VERSE_IDS = [
    19130004,
    19130008,
    24029032,
    24030001,
    24030002,
    24030003,
    24030004,
    24030005,
    24030006,
    24030007,
    24030008,
    24030009,
    24030010,
    24031012,
    40001018,
    40001019,
    40001020,
    40001021,
    40001022,
    40001023,
    40001024,
    40001025,
    40002001,
    40002002,
    40002003,
    40002004,
    40002005,
    40002006,
    40002007,
    40002008,
    40002009,
    40002010,
    40002011,
    40002012,
    40002013,
    40002014,
    40002015,
    40002016,
    40002017,
    40002018,
    42003005,
    42003006,
    42003007,
]


class ModelTestCase(TestCase):
    def test_add_verse(self):
        # Given an object that can be indexed by scripture references
        test_object = TestObjectFactory()

        # When a verse is added to that test_object
        test_object.add_verse(1001001)

        # Then that verse id appears in the list of verse ids
        self.assertEqual(test_object.verse_ids, [1001001])

    def test_add_verse_invalid(self):
        # Given an object that can be indexed by scripture references
        test_object = TestObjectFactory()

        # When we attempt to add an invalid verse to that object
        # Then an error is raised
        with self.assertRaises(bible.InvalidVerseError):
            test_object.add_verse(1100100)

    def test_add_verses_from_text_with_scripture_references(self):
        # Given a test_object and a text with scripture references
        test_object = TestObjectFactory()
        text = "You should read Psalm 130:4,8, Jeremiah 29:32-30:10,31:12, Matthew 1:18 - 2:18, and Luke 3: 5-7."

        # Get the references from the text and convert them to verse ids
        references = bible.get_references(text)
        verse_ids = bible.convert_references_to_verse_ids(references)

        # When we add all of the verse ids to the test object
        for verse_id in verse_ids:
            test_object.add_verse(verse_id)

        # Then the list of verse ids list matches
        actual_verse_ids = test_object.verse_ids

        self.assertEqual(actual_verse_ids, verse_ids)
        self.assertEqual(actual_verse_ids, EXPECTED_VERSE_IDS)

    def test_set_verses(self):
        # Given a test object and a list of verse ids
        test_object = TestObjectFactory()

        # When we set the test object's verses to be the verse ids
        test_object.set_verses(EXPECTED_VERSE_IDS)

        # Then the verse ids list matches
        self.assertEqual(test_object.verse_ids, EXPECTED_VERSE_IDS)

    def test_set_verses_deletes_existing(self):
        # Given a test object and a valid verse id and a list of verse ids
        test_object = TestObjectFactory()

        # When we add a verse to the test object
        test_object.add_verse(1001001)

        # And when we set the test object's verses to be the verse ids
        test_object.set_verses(EXPECTED_VERSE_IDS)

        # Then the original verse id is not in the test object's verse ids list
        actual_verse_ids = test_object.verse_ids
        self.assertNotIn(1001001, actual_verse_ids)

        # And then the actual verse ids is equal to expected verse ids
        self.assertEqual(actual_verse_ids, EXPECTED_VERSE_IDS)

    def test_object_str(self):
        # Given a test object with a name
        test_object = TestObjectFactory()

        # When calling the __str__ method on the test object
        test_object_string = str(test_object)

        # Then the string representation of the test object equals the name.
        self.assertEqual(test_object_string, test_object.name)

    def test_single_verse_object_str(self):
        # Given a test object with a name
        test_single_verse_object = TestSingleVerseObjectFactory()

        # When calling the __str__ method on the test object
        test_object_string = str(test_single_verse_object)

        # Then the string representation of the test object equals the name.
        self.assertEqual(test_object_string, test_single_verse_object.name)

    def test_single_verse_object_filter_by_verse(self):
        # Given a valid_verse_id and a matching reference string
        valid_verse_id = 1001001
        reference_string = bible.format_scripture_references(
            bible.convert_verse_ids_to_references([valid_verse_id])
        )

        # Given a single verse object that references that verse id
        test_single_verse_object = TestSingleVerseObjectFactory(verse=valid_verse_id)

        # When we get the test objects by the int verse id and the test objects by the reference string
        test_objects_by_id = TestSingleVerseObject.objects.filter(verse=valid_verse_id)
        test_objects_by_reference = TestSingleVerseObject.objects.filter(
            verse=reference_string
        )

        # Then both collections of objects should be the same
        self.assertEqual(test_objects_by_id.count(), test_objects_by_reference.count())

        for i, test_object_a in enumerate(test_objects_by_id):
            test_object_b = test_objects_by_reference[i]
            self.assertEqual(test_object_a, test_object_b)
            self.assertEqual(test_object_a, test_single_verse_object)
            self.assertEqual(test_object_b, test_single_verse_object)

    def test_single_verse_object_filter_by_verse_invalid(self):
        # Given an invalid reference and verse id
        invalid_verse_id = 1100100

        # When attempting to filter the objects by the invalid reference
        # Then a validation error is raised.
        with self.assertRaises(ValidationError):
            TestSingleVerseObject.objects.filter(verse="invalid reference")

        # When attempting to filter the objects by the invalid verse id
        # Then a validation error is raised.
        with self.assertRaises(ValidationError):
            TestSingleVerseObject.objects.filter(verse=invalid_verse_id)

    def test_single_verse_object_set_verse_by_id(self):
        # Given a test single verse object and a valid verse id
        valid_verse_id = 1001001
        test_single_verse_object = TestSingleVerseObjectFactory(verse=2002002)

        # Given the reference string associated with that verse id
        reference_string: str = bible.format_scripture_references(
            bible.convert_verse_ids_to_references([valid_verse_id])
        )

        # Given that the current verse associated with the object is not the same as the given verse id
        self.assertNotEqual(test_single_verse_object.verse, valid_verse_id)
        self.assertNotEqual(test_single_verse_object.verse, reference_string)

        # When we set the verse on the test object to be the verse id
        test_single_verse_object.verse = valid_verse_id
        test_single_verse_object.save()

        # Then the verse associated with the object matches the verse id
        self.assertEqual(test_single_verse_object.verse, valid_verse_id)

        # And the verse associated with the object after retrieving it from the DB again matches the reference string
        updated_test_single_verse_object: TestSingleVerseObject = (
            TestSingleVerseObject.objects.get(id=test_single_verse_object.id)
        )
        self.assertEqual(updated_test_single_verse_object.verse, reference_string)

    def test_single_verse_object_set_verse_by_reference(self):
        # Given a test single verse object and a verse reference
        reference = "Genesis 1:1"

        # Given the verse id associated with that reference
        test_single_verse_object = TestSingleVerseObject(verse=2002002)
        verse_id = bible.convert_references_to_verse_ids(
            bible.get_references(reference)
        )[0]

        # Given that the current verse associated with the object is not the same as the given reference
        self.assertNotEqual(test_single_verse_object.verse, reference)
        self.assertNotEqual(test_single_verse_object.verse, verse_id)

        # When we set the verse on the test object to be the reference
        test_single_verse_object.verse = reference
        test_single_verse_object.save()

        # Then the verse associated with the object matches the reference
        self.assertEqual(test_single_verse_object.verse, reference)

        # And the verse associated with the object after retrieving it from the DB again still matches the reference
        updated_test_single_verse_object: TestSingleVerseObject = (
            TestSingleVerseObject.objects.get(id=test_single_verse_object.id)
        )
        self.assertEqual(updated_test_single_verse_object.verse, reference)

    def test_single_verse_object_set_verse_by_reference_invalid(self):
        # Given a test single verse object and an invalid verse id and reference
        test_single_verse_object = TestSingleVerseObject(verse=2002002)

        # When we set the verse on the test object to be the invalid reference
        # Then a validation error is raised.
        with self.assertRaises(ValidationError):
            test_single_verse_object.verse = "invalid reference"
            test_single_verse_object.save()

        # When we set the verse on the test object to be the invalid verse id
        # Then a validation error is raised
        with self.assertRaises(ValidationError):
            test_single_verse_object.verse = 1100100
            test_single_verse_object.save()
