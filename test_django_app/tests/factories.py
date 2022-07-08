import random

import factory

import djangobible
from test_django_app.models import TestObject, TestSingleVerseObject


class TestObjectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TestObject

    name = factory.Faker("name")


class TestSingleVerseObjectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TestSingleVerseObject

    name = factory.Faker("name")
    verse = random.choice(djangobible.verses.VERSE_IDS)
