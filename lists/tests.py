from django.http import HttpRequest
from django.test import TestCase

from .views import home_page


# Create your tests here.
class HomePageTest(TestCase):
    def test_home_page_that_returns_correct_http(self):
        request = HttpRequest()
        response = home_page(request)

        html = response.content.decode("utf8")
        self.assertIn("<title>To-do lists</title>", html)
        self.assertTrue(html.startswith("<html>"))
        self.assertTrue(html.endswith("</html>"))



