from django.test import TestCase


class HomePageTest(TestCase):
    def test_correct_template_rendering(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "lists/home_page.html")

    # A little smoke test in the unittest
    def test_exists_todo_form(self):
        response = self.client.get("/")
        self.assertContains(response, '<form method="POST">')
        self.assertContains(response, '<input name="todo_item"')

    def test_post_todo_addition_request(self):
        response = self.client.post("/", data={"todo_item": "a new todo"})
        self.assertContains(response, "a new todo")
