from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
def home_page(request: HttpRequest):
    if request.method == 'POST':
        return HttpResponse(request.POST['todo_item'])

    return render(request, "lists/home_page.html")

