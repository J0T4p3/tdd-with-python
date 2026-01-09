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
        self.client.post("/", data={"todo_item": "a new todo"})
        last_inserted_todo = Item.objects.last()
        self.assertEqual(last_inserted_todo.text, "a new todo")

    def test_post_multiple_todo_addition_request(self):
        self.client.post("/", data={"todo_item": "a new todo"})
        self.client.post("/", data={"todo_item": "other todo"})

        todos = Item.objects.all()
        self.assertEqual(todos.count(), 2)
        self.assertEqual(todos[0].text, "a new todo")
        self.assertEqual(todos[1].text, "other todo")

class ItemModelTest(TestCase):
    def test_can_save_POST_request(self):
        todo_text = 'a new todo item'
        response = self.client.post('/', {'todo_item': todo_text})

        new_item=Item.objects.last()
        self.assertEqual(new_item.text, todo_text)
        self.assertRedirects(response, '/')

    def test_can_save_multiple_POST_items(self):
        todo_text = 'a new todo item'
        todo_other_text = 'a newer todo item!'
        self.client.post('/', {'todo_item': todo_text})
        response = self.client.post('/', {'todo_item': todo_other_text})

        self.assertRedirects(response, '/')

    def test_do_not_save_empty_items(self):
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)
        self.assertTemplateUsed('lists/home_page.html')
