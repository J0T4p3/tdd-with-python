from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Item


# Create your views here.
def home_page(request: HttpRequest):
    todo_item = Item()
    if todo := request.POST.get("todo_item"):
        todo_item.text = todo
        todo_item.save()
    return render(request, "lists/home_page.html", {"todo_items": Item.objects.all()})

