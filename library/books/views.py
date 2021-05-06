from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'books/home.html')

def about(request):
    return render(request, 'books/about.html')

# def create(request):
#     return render(request, 'new.html')

# def show(request, book_id):
#     return render(request, 'show.html')