from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
def home_page(request: HttpRequest):
    return render(request, "lists/home_page.html", {"todo_item": request.POST.get("todo_item")})

