import os

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from playwright.sync_api import sync_playwright


class TagsFunctionalTestcase(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
        super().setUpClass()
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.chromium.launch(headless=True)

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.browser.close()
        cls.playwright.stop()

    def test_verse_tags(self):
        page = self.browser.new_page()
        page.goto(f"{self.live_server_url}/verse_tags/")

        self.assertEqual(page.title(), "Verse Tags Test")
        self.assertEqual(
            page.locator("id=verse-reference").text_content(), "Genesis 1:1"
        )
        self.assertEqual(
            page.locator("id=verse-text").text_content(),
            "In the beginning God created the heaven and the earth.",
        )
        self.assertEqual(
            page.locator("id=full-verse-reference").text_content(),
            "The First Book of Moses, Commonly Called Genesis 1:1",
        )
        self.assertEqual(
            page.locator("id=asv-verse-text").text_content(),
            "In the beginning God created the heavens and the earth.",
        )

        page.close()
