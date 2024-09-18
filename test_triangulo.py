from playwright.sync_api import sync_playwright
import unittest


class Triangulotest(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = sync_playwright().start().chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.page.goto("https://vanilton.net/web-test/triangulo_v2/")
        self.context.set_default_timeout(5_000)

    def test_triangulo_equilatero(self):
        page = self.page
        page.get_by_label("Lado A:").click()
        page.get_by_label("Lado A:").fill("1")
        page.get_by_label("Lado B:").click()
        page.get_by_label("Lado B:").fill("1")
        page.get_by_label("Lado C:").click()
        page.get_by_label("Lado C:").fill("1")
        page.get_by_role("button", name="Validar").click()

    def test_triangulo_isosceles(self):
        page = self.page
        page.get_by_label("Lado A:").click()
        page.get_by_label("Lado A:").fill("3")
        page.get_by_label("Lado B:").click()
        page.get_by_label("Lado B:").fill("3")
        page.get_by_label("Lado C:").click()
        page.get_by_label("Lado C:").fill("2")
        page.get_by_role("button", name="Validar").click()
        self.assertTrue(page.get_by_text("Triângulo Isósceles",exact=True).is_visible())


    def test_triangulo_escaleno(self):
        page = self.page
        page.get_by_label("Lado A:").click()
        page.get_by_label("Lado A:").fill("4")
        page.get_by_label("Lado B:").click()
        page.get_by_label("Lado B:").fill("3")
        page.get_by_text("Lado A: Lado B: Lado C:").click()
        page.get_by_label("Lado C:").click()
        page.get_by_label("Lado C:").fill("2")
        page.get_by_role("button", name="Validar").click()



    def tearDown(self) -> None:
        self.context.close()
        self.browser.close()


