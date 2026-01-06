from django.test import TestCase


class HomePageTest(TestCase):
    def test_correct_template_rendering(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "lists/home_page.html")

    # A little smoke test in the unittest
    def test_correct_content_displayed(self):
        response = self.client.get("/")
        self.assertContains(response, "To-do")
