import random

import factory
from django.contrib.auth import get_user_model

import djangobible
from test_django_app.models import TestObject, TestSingleVerseObject

TEST_USERNAME = "admin"
TEST_EMAIL = "admin@python.bible"
TEST_PASSWORD = "Test1234"


class SuperUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        return manager.create_superuser(
            username=TEST_USERNAME, email=TEST_EMAIL, password=TEST_PASSWORD
        )


class TestObjectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TestObject

    name = factory.Faker("name")


class TestSingleVerseObjectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TestSingleVerseObject

    name = factory.Faker("name")
    verse = random.choice(djangobible.verses.VERSE_IDS)
