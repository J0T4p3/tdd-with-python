import os
import re

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

import pytest
from playwright.sync_api import Page, expect, sync_playwright


@pytest.mark.django_db
def test_can_start_a_todo_list(live_server, page:Page):
    page.goto(live_server.url)
    expect(page).to_have_title(re.compile("To-do"))
    expect(page.get_by_role('h1', name="To-do"))

    # She are prompted to write a todo right away
    input_box = page.get_by_placeholder("Enter a to-do item")

    # After she presses the button, a list appear bellow the input box with 1 - make a pasta as it's title
    input_box.fill("make a pasta")
    page.get_by_placeholder("Enter a to-do item").press('Enter')
    expect(page.get_by_text("1: make a pasta", exact=True)).to_be_visible()

    # She writes again, now with the words "Serve the pasta to friends".
    # Again, after pressing 'enter', the words written are now in the second list item,
    # 2 - Serve the pasta to friends, with the first step appearing before the second.
    input_box.fill("serve it to friends")
    page.get_by_placeholder("Enter a to-do item").press('Enter')
    expect(page.get_by_text("1: make a pasta", exact=True)).to_be_visible()
    expect(page.get_by_text("2: serve it to friends", exact=True)).to_be_visible()
