import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


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
        header_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn("To-do", header_text)

        # She are prompted to write a todo right away
        input_box = self.browser.find_element(By.ID, "id_input_todo")
        self.assertEqual(input_box.get_attribute("placeholder"), "Enter a to-do item")

        # She types "make a pasta" on the box and press 'enter'
        input_box.send_keys("make a pasta")
        input_box.send_keys(webdriver.Keys.ENTER)

        # After she presses the button, a list appear bellow the input box with 1 - make a pasta as it's title
        time.sleep(1)
        table = self.browser.find_element(By.ID, "id_todo_table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        self.assertTrue(any(row.text == "1: make a pasta" for row in rows))

        # The box is now empty again, ready to receive new inputs
        self.fail('Finish the test')

        # She writes again, now with the words "Serve the pasta to friends".
        # Again, after pressing 'enter', the words written are now in the second list item,
        # 2 - Serve the pasta to friends, with the first step appearing before the second.

if __name__ == "__main__":
    unittest.main()
