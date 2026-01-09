from django.test import TestCase

from .models import Item


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
        self.assertTemplateUsed(response, "lists/home_page.html")

    def test_post_multiple_todo_addition_request(self):
        response = self.client.post("/", data={"todo_item": "a new todo"})
        response = self.client.post("/", data={"todo_item": "other todo"})
        self.assertContains(response, "a new todo")
        self.assertContains(response, "other todo")
        self.assertTemplateUsed(response, "lists/home_page.html")

class ItemModelTest(TestCase):
    def test_saved_item(self):
        item = Item()
        item.text = "The first Item"
        item.save()

        item = Item()
        item.text = "The second Item"
        item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)
        self.assertEqual(saved_items[0].text, "The first Item")
        self.assertEqual(saved_items[1].text, "The second Item")

