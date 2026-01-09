from django.http import HttpRequest
from django.shortcuts import redirect, render

from .models import Item


# Create your views here.
def home_page(request: HttpRequest):
    if request.method == 'POST':
        todo_item = Item(text=request.POST['todo_item'])
        todo_item.save()
        return redirect('/')
    return render(request, "lists/home_page.html", {"todo_items": Item.objects.all()})

