from typing import Callable

import pytest
from selenium import webdriver

import djangobible as bible
from test_django_app.models import TestObject, TestSingleVerseObject


@pytest.fixture
def test_object_factory() -> Callable:
    def create_test_object(name: str) -> TestObject:
        test_object = TestObject(name=name)
        test_object.save()
        return test_object

    return create_test_object


@pytest.fixture
def test_objects(test_object_factory):
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

    for i in range(10):
        test_object = test_object_factory(f"test object {i + 1}")
        test_object.set_verses(
            bible.convert_references_to_verse_ids(bible.get_references(references[i]))
        )
        test_objects.append(test_object)

    return test_objects


@pytest.fixture
def test_object(test_object_factory):
    return test_object_factory("test object")


@pytest.fixture
def test_single_verse_object_factory() -> Callable:
    def create_test_single_verse_object(name: str) -> TestSingleVerseObject:
        test_single_verse_object = TestSingleVerseObject(name=name, verse="Exodus 2:2")
        test_single_verse_object.save()
        return test_single_verse_object

    return create_test_single_verse_object


@pytest.fixture
def test_single_verse_objects(test_single_verse_object_factory):
    test_single_verse_objects = []
    references = [
        "Genesis 1:10",
        "Psalm 130:1",
        "Matthew 18:1",
        "Luke 15:1",
        "Exodus 20:1",
        "Jeremiah 29:11",
        "Psalm 51:1",
        "Genesis 1:1",
        "luke 2:2",
        "Genesis 1:4",
    ]

    for i in range(10):
        test_single_verse_object = test_single_verse_object_factory(
            f"test object {i + 1}"
        )
        test_single_verse_object.verse = references[i]
        test_single_verse_object.save()
        test_single_verse_objects.append(test_single_verse_object)

    return test_single_verse_objects


@pytest.fixture
def test_single_verse_object(test_single_verse_object_factory):
    return test_single_verse_object_factory("test single verse object")


@pytest.fixture
def valid_verse_id():
    return 1001001


@pytest.fixture
def invalid_verse_id():
    return 1100100


@pytest.fixture
def text_with_scripture_references():
    return "You should read Psalm 130:4,8, Jeremiah 29:32-30:10,31:12, Matthew 1:18 - 2:18, and Luke 3: 5-7."


@pytest.fixture
def expected_verse_ids():
    return [
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


@pytest.fixture
def version_asv():
    return bible.Version.AMERICAN_STANDARD


@pytest.fixture
def reference():
    return "Genesis 1:1"


@pytest.fixture
def full_asv_reference():
    return "The First Book of Moses, Commonly Called Genesis 1:1"


@pytest.fixture
def kjv_verse_text():
    return "In the beginning God created the heaven and the earth."


@pytest.fixture
def asv_verse_text():
    return "In the beginning God created the heavens and the earth."


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
