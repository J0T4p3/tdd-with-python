import unittest

from selenium import webdriver


class NewVisitorsTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_todo_list(self):
        # Edith get to know a new website for writing todo lists
        # She goes to its homepage
        self.browser.get('http://localhost:8000')

        # She notices something related with To-do on the title
        self.assertIn("To-do", self.browser.title)

        # She are prompted to write a todo right away
        self.fail('Finish the test')

        # She types "make a pasta" on the box and press 'enter'

        # After she presses the button, a list appear bellow the input box with 1 - make a pasta as it's title
        # The box is now empty again, ready to receive new inputs

        # She writes again, now with the words "Serve the pasta to friends".
        # Again, after pressing 'enter', the words written are now in the second list item,
        # 2 - Serve the pasta to friends, with the first step appearing before the second.

if __name__ == "__main__":
    unittest.main()
