from django.http import HttpRequest
from django.test import TestCase

from .views import home_page


# Create your tests here.
class HomePageTest(TestCase):
    def test_home_page_that_returns_correct_html(self):
        response = self.client.get("/")
        html = response.content.decode("utf8")
        self.assertIn("<title>To-do lists</title>", html)
        self.assertTrue(html.startswith("<html>"))
        self.assertTrue(html.endswith("</html>"))





