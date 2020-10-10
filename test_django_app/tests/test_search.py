import pytest

import djangobible as bible
from test_django_app.models import TestObject


@pytest.mark.django_db
def test_search_by_text_with_scripture_references(
    test_objects, text_with_scripture_references
):
    # Given test_objects with scripture references and a search text
    # When searching for test objects associated with the verses in the search text
    references = bible.get_references(text_with_scripture_references)
    verse_ids = bible.convert_references_to_verse_ids(references)
    actual_test_objects = TestObject.objects.filter_by_verse_ids(verse_ids)

    # Then the result is a queryset containing test object 1 and test object 5
    assert len(actual_test_objects) == 2
    assert test_objects[1] in actual_test_objects
    assert test_objects[5] in actual_test_objects
