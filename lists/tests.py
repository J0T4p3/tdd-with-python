from django.test import TestCase


class HomePageTest(TestCase):
    def test_home_page_that_returns_correct_html(self):
        # By the context, get the view associated with the url
        response = self.client.get("/")
        html = response.content.decode("utf8").strip()
        self.assertIn("<title>To-do lists</title>", html)
        self.assertTrue(html.startswith("<html>"))
        self.assertTrue(html.endswith("</html>"))
        self.assertTemplateUsed("lists/home_page.html")

