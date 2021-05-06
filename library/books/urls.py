from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='books-home'),
    path('about/', views.about, name='books-about'),
    # path('books/new/', views.create, name='books/book-create'),
    # path('books/<int:book_id>/', views.show, name='books/book-show')
]