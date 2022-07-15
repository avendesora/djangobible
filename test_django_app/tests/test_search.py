from __future__ import annotations

from django.test import TestCase
from pythonbible import convert_references_to_verse_ids, get_references

from test_django_app.models import TestObject
from test_django_app.tests.factories import TestObjectFactory


def get_test_objects() -> list[TestObject]:
    test_objects = []
    references = [
        "Genesis 1:1-10",
        "Psalm 130",
        "Matthew 18",
        "Luke 15",
        "Exodus 20",
        "Jeremiah 29",
        "Psalm 51",
        "Genesis 1:1",
        "luke 2",
        "Genesis 1:1-4",
    ]

    for index in range(10):
        test_object = TestObjectFactory()
        test_object.set_verses(
            convert_references_to_verse_ids(get_references(references[index])),
        )
        test_objects.append(test_object)

    return test_objects


class SearchTestCase(TestCase):
    def test_search_by_text_with_scripture_references(self: SearchTestCase) -> None:
        # Given test_objects with scripture references and a search text
        text = (
            "You should read Psalm 130:4,8, Jeremiah 29:32-30:10,31:12, "
            "Matthew 1:18 - 2:18, and Luke 3: 5-7."
        )
        test_objects = get_test_objects()

        # When searching for test objects associated with the verses in the search text
        references = get_references(text)
        verse_ids = convert_references_to_verse_ids(references)
        actual_test_objects = TestObject.objects.filter_by_verse_ids(verse_ids)

        # Then the result is a queryset containing test object 1 and test object 5
        self.assertEqual(len(actual_test_objects), 2)

        for index, test_object in enumerate(test_objects):
            if index in {1, 5}:
                self.assertIn(test_object, actual_test_objects)
            else:
                self.assertNotIn(test_object, actual_test_objects)
