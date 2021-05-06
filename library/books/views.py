from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# def create(request):
#     return render(request, 'new.html')

# def show(request, book_id):
#     return render(request, 'show.html')