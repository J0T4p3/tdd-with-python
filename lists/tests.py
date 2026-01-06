from django.test import TestCase


class HomePageTest(TestCase):
    def test_home_page_that_returns_correct_html(self):
        # By the context, get the view associated with the url
        response = self.client.get("/")
        self.assertTemplateUsed(response, "lists/home_page.html")

