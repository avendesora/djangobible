import pytest

import djangobible as bible
from djangobible.templatetags.verse_tags import verse_reference, verse_text


@pytest.mark.functional
def test_verse_tags(
    driver, reference, full_asv_reference, kjv_verse_text, asv_verse_text
):
    driver.get("http://127.0.0.1:8000/verse_tags/")

    assert driver.title == "Verse Tags Test"
    assert driver.find_element_by_id("verse-reference").text == reference
    assert driver.find_element_by_id("verse-text").text == kjv_verse_text
    assert driver.find_element_by_id("full-verse-reference").text == full_asv_reference
    assert driver.find_element_by_id("asv-verse-text").text == asv_verse_text


def test_tag_verse_reference(valid_verse_id, reference):
    # Given a valid verse id
    # When getting the reference for that verse_id
    actual_reference = verse_reference(valid_verse_id)

    # Then the reference is as expected
    assert actual_reference == reference


def test_tag_verse_reference_null():
    # Given a null verse id
    # When getting the reference for that verse_id
    # Then an invalid verse error is raised.
    with pytest.raises(bible.InvalidVerseError):
        verse_reference(None)


def test_tag_verse_reference_invalid(invalid_verse_id):
    # Given an invalid verse id
    # When getting the reference for that verse_id
    # Then an invalid verse error is raised.
    with pytest.raises(bible.InvalidVerseError):
        verse_reference(invalid_verse_id)


def test_tag_verse_reference_version_full_title(
    valid_verse_id, version_asv, full_asv_reference
):
    # Given a verse id and a version
    # When getting the reference
    reference = verse_reference(
        valid_verse_id, version=version_asv.value, full_title=True
    )

    # Then the full title reference is as expected.
    assert reference == full_asv_reference


def test_tag_verse_text(valid_verse_id, kjv_verse_text):
    # Given a verse id
    # When getting the verse text for that verse id
    actual_verse_text = verse_text(valid_verse_id)

    # Then the verse text is as expected.
    assert actual_verse_text == kjv_verse_text


def test_tag_verse_text_null():
    # Given a null verse id
    # When getting the verse text for that verse id
    # Then an invalid verse error is raised.
    with pytest.raises(bible.InvalidVerseError):
        verse_text(None)


def test_tag_verse_text_invalid(invalid_verse_id):
    # Given an invalid verse id
    # When getting the verse text for that verse id
    # Then an invalid verse error is raised.
    with pytest.raises(bible.InvalidVerseError):
        verse_text(invalid_verse_id)


def test_tag_verse_text_version(valid_verse_id, version_asv, asv_verse_text):
    # Given a valid verse id and a version that is not the default
    # When getting the verse text for that verse_id and version
    actual_verse_text = verse_text(valid_verse_id, version=version_asv)

    # Then the verse text is as expected.
    assert actual_verse_text == asv_verse_text


def test_tag_verse_text_verse_numbers(valid_verse_id, kjv_verse_text):
    # Given a valid verse id
    # When getting the verse text while setting the include_verse_numbers keyword argument to True
    actual_verse_text = verse_text(valid_verse_id, include_verse_numbers=True)

    # Then the verse text is as expected.
    assert actual_verse_text == f"1. {kjv_verse_text}"
