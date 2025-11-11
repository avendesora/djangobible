from __future__ import annotations

from django.test import TestCase
from pythonbible import InvalidVerseError
from pythonbible import Version

from djangobible.templatetags.verse_tags import verse_reference
from djangobible.templatetags.verse_tags import verse_text


class TagTestCase(TestCase):
    def test_tag_verse_reference(self: TagTestCase) -> None:
        # Given a valid verse id
        valid_verse_id = 1001001

        # When getting the reference for that verse_id
        actual_reference = verse_reference(valid_verse_id)

        # Then the reference is as expected
        self.assertEqual(actual_reference, "Genesis 1:1")

    def test_tag_verse_reference_null(self: TagTestCase) -> None:
        # Given a null verse id
        # When getting the reference for that verse_id
        # Then an invalid verse error is raised.
        with self.assertRaises(InvalidVerseError):
            verse_reference(None)

    def test_tag_verse_reference_invalid(self: TagTestCase) -> None:
        # Given an invalid verse id
        invalid_verse_id = 1100100

        # When getting the reference for that verse_id
        # Then an invalid verse error is raised.
        with self.assertRaises(InvalidVerseError):
            verse_reference(invalid_verse_id)

    def test_tag_verse_reference_version_full_title(self: TagTestCase) -> None:
        # Given a verse id and a version
        valid_verse_id = 1001001
        version_asv = Version.AMERICAN_STANDARD

        # When getting the reference
        reference = verse_reference(
            valid_verse_id,
            version=version_asv.value,
            full_title=True,
        )

        # Then the full title reference is as expected.
        self.assertEqual(
            reference,
            "The First Book of Moses, Commonly Called Genesis 1:1",
        )

    def test_tag_verse_text(self: TagTestCase) -> None:
        # Given a verse id
        valid_verse_id = 1001001

        # When getting the verse text for that verse id
        actual_verse_text = verse_text(valid_verse_id)

        # Then the verse text is as expected.
        self.assertEqual(
            actual_verse_text,
            "In the beginning God created the heavens and the earth.",
        )

    def test_tag_verse_text_null(self: TagTestCase) -> None:
        # Given a null verse id
        # When getting the verse text for that verse id
        # Then an invalid verse error is raised.
        with self.assertRaises(InvalidVerseError):
            verse_text(None)

    def test_tag_verse_text_invalid(self: TagTestCase) -> None:
        # Given an invalid verse id
        invalid_verse_id = 1100100

        # When getting the verse text for that verse id
        # Then an invalid verse error is raised.
        with self.assertRaises(InvalidVerseError):
            verse_text(invalid_verse_id)

    def test_tag_verse_text_version(self: TagTestCase) -> None:
        # Given a valid verse id and a version that is not the default
        valid_verse_id = 1001001
        version_asv = Version.KING_JAMES

        # When getting the verse text for that verse_id and version
        actual_verse_text = verse_text(valid_verse_id, version=version_asv)

        # Then the verse text is as expected.
        self.assertEqual(
            actual_verse_text,
            "In the beginning God created the heaven and the earth.",
        )

    def test_tag_verse_bad_version(self: TagTestCase) -> None:
        # Given a valid verse id and a version that is not a valid version
        valid_verse_id = 1001001
        bad_version = "bad version"

        # When getting the verse text for that verse_id and version
        actual_verse_text = verse_text(valid_verse_id, version=bad_version)

        # Then the verse text defaults to kjv
        self.assertEqual(
            actual_verse_text,
            "In the beginning God created the heavens and the earth.",
        )

    def test_tag_verse_text_verse_numbers(self: TagTestCase) -> None:
        # Given a valid verse id
        valid_verse_id = 1001001

        # When getting the verse text while setting the include_verse_numbers keyword
        # argument to True
        actual_verse_text = verse_text(valid_verse_id, include_verse_numbers=True)

        # Then the verse text is as expected.
        self.assertEqual(
            actual_verse_text,
            "1. In the beginning God created the heavens and the earth.",
        )
