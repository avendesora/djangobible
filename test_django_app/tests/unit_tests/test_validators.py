from __future__ import annotations

from django.core.exceptions import ValidationError
from django.test import TestCase

from djangobible.validators import validate_verse


class ValidatorsTestCase(TestCase):
    def test_validate_verse_none(self: ValidatorsTestCase) -> None:
        validate_verse(None)
        self.assertTrue(True)

    def test_validate_verse_not_valid_reference(self: ValidatorsTestCase) -> None:
        invalid_reference = "invalid reference"

        with self.assertRaises(ValidationError):
            validate_verse(invalid_reference)

    def test_validate_verse_only_single_verse(self: ValidatorsTestCase) -> None:
        multi_verse_reference = "Genesis 1:1-2"

        with self.assertRaises(ValidationError):
            validate_verse(multi_verse_reference)

        multi_reference_reference = "Genesis 1:1 and Exodus 2:2"

        with self.assertRaises(ValidationError):
            validate_verse(multi_reference_reference)
