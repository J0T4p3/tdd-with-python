from django.test import TestCase


class HomePageTest(TestCase):
    def test_correct_template_rendering(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "lists/home_page.html")

    # A little smoke test in the unittest
    def test_exists_todo_form(self):
        response = self.client.get("/")
        self.assertContains(response, '<form method="POST">')
        self.assertContains(response, '<input id="id_input_todo" name="todo-item" placeholder="Enter a to-do item" />')
