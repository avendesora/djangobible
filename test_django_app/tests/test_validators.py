from django.core.exceptions import ValidationError
from django.test import TestCase

from djangobible.validators import validate_verse


class ValidatorsTestCase(TestCase):
    def test_validate_verse_none(self):
        self.assertIsNone(validate_verse(None))

    def test_validate_verse_not_valid_reference(self):
        invalid_reference = "invalid reference"

        with self.assertRaises(ValidationError):
            validate_verse(invalid_reference)

    def test_validate_verse_only_single_verse(self):
        multi_verse_reference = "Genesis 1:1-2"

        with self.assertRaises(ValidationError):
            validate_verse(multi_verse_reference)

        multi_reference_reference = "Genesis 1:1 and Exodus 2:2"

        with self.assertRaises(ValidationError):
            validate_verse(multi_reference_reference)
