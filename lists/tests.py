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
    def test_can_save_POST_request(self):
        todo_text = 'a new todo item'
        response = self.client.post('/', {'todo_item': todo_text})

        new_item=Item.objects.last()
        self.assertEqual(new_item.text, todo_text)
        self.assertContains(response, todo_text)
        self.assertTemplateUsed('lists/home_page.html')

    def test_can_save_multiple_POST_items(self):
        todo_text = 'a new todo item'
        todo_other_text = 'a newer todo item!'
        self.client.post('/', {'todo_item': todo_text})
        response = self.client.post('/', {'todo_item': todo_other_text})

        self.assertContains(response, todo_text)
        self.assertContains(response, todo_other_text)
        self.assertTemplateUsed('lists/home_page.html')

    def test_do_not_save_empty_items(self):
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)
        self.assertTemplateUsed('lists/home_page.html')
