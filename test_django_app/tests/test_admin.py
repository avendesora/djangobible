import os

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from playwright.sync_api import sync_playwright

from test_django_app.tests.factories import TEST_PASSWORD, SuperUserFactory


class AdminTestcase(StaticLiveServerTestCase):
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

    def _login_to_admin_site(self):
        user = SuperUserFactory()

        page = self.browser.new_page()
        page.goto(f"{self.live_server_url}/admin/")
        page.wait_for_selector("text=Django administration")
        page.fill("[name=username]", user.username)
        page.fill("[name=password]", TEST_PASSWORD)
        page.click("text=Log in")
        self.assertIn(user.username, page.locator("id=user-tools").text_content())

        return user, page

    def test_object(self):
        user, page = self._login_to_admin_site()

        page.click("text=Test objects")
        page.wait_for_selector("text=Select test object to change")

        page.click("text=Add test object")

        # TODO

        page.close()

    def test_single_verse_object(self):
        user, page = self._login_to_admin_site()

        page.click("text=Test single verse objects")
        page.wait_for_selector("text=Select test single verse object to change")

        page.goto(
            f"{self.live_server_url}/admin/test_django_app/testsingleverseobject/add/"
        )

        page.fill("[name=name]", "my new test single verse object")
        page.fill("[name=verse]", "Genesis 1:1")
        page.click("text=Save")

        page.wait_for_selector("text=my new test single verse object")

        page.goto(
            f"{self.live_server_url}/admin/test_django_app/testsingleverseobject/add/"
        )

        page.fill("[name=name]", "my other new test single verse object")
        page.click("text=Save")

        page.click("text=my other new test single verse object")
        page.fill("[name=verse]", "Genesis 1:1")
        page.click("text=Save")

        page.close()
