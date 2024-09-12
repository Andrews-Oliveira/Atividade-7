
from playwright.sync_api import Playwright, sync_playwright
import unittest


class Todotest(unittest.TestCase):
    def setUp(self) ->None :
        self.browser = sync_playwright().start().chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.page.goto("https://vanilton.net/web-test/todos/")


    def test_cadastrar_todos(self):
        page=self.page
        page.locator("html").click()
        page.get_by_placeholder("What needs to be done?").click()
        page.get_by_placeholder("What needs to be done?").click()
        page.get_by_placeholder("What needs to be done?").click()
        page.get_by_placeholder("What needs to be done?").fill("teste")
        page.get_by_placeholder("What needs to be done?").click()
        (page.get_by_placeholder("What needs to be done?").press("Enter"))
        self.assertTrue(page.get_by_placeholder("What needs to be done?").is_visible())



    def tearDown(self)->None:
        self.context.close()
        self.browser.close()



