from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_page(request):
    html = """
        <html>
            <title>To-do lists</title>
            <body>
                <h1>To-do</h1>
                <input id="id_input_todo" placeholder="Enter a to-do item"></input>
                <table id="id_todo_table">
                    <tr>1: make a pasta</tr>
                </table>
            </body>
        </html>
    """
    return HttpResponse(content=html)
