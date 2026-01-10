import time

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By

MAX_WAIT = 5

class NewVisitorsTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def assert_row_in_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element(By.ID, "id_todo_table")
                rows = table.find_elements(By.TAG_NAME, "tr")
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException):
                if time.time() - start_time > MAX_WAIT:
                    raise
                time.sleep(0.1)



    def test_can_start_a_todo_list(self):
        # Edith get to know a new website for writing todo lists
        # She goes to its homepage
        self.browser.get(self.live_server_url)

        # She notices something related with To-do on the title
        self.assertIn("To-do", self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn("To-do", header_text)

        # She are prompted to write a todo right away
        input_box = self.browser.find_element(By.ID, "id_input_todo")
        self.assertEqual(input_box.get_attribute("placeholder"), "Enter a to-do item")

        # After she presses the button, a list appear bellow the input box with 1 - make a pasta as it's title
        input_box.send_keys("make a pasta")
        input_box.send_keys(webdriver.Keys.ENTER)

        self.assert_row_in_table("1: make a pasta" )

        # She writes again, now with the words "Serve the pasta to friends".
        # Again, after pressing 'enter', the words written are now in the second list item,
        # 2 - Serve the pasta to friends, with the first step appearing before the second.
        input_box = self.browser.find_element(By.ID, "id_input_todo")
        self.assertEqual(input_box.get_attribute("placeholder"), "Enter a to-do item")
        input_box.send_keys("serve it to friends")
        input_box.send_keys(webdriver.Keys.ENTER)

        # After she presses the button, a list appear bellow the input box with 2 - serve it to friends as it's title
        self.assert_row_in_table("2: serve it to friends" )

        # The box is now empty again, ready to receive new inputs
        self.fail('Finish the test')
