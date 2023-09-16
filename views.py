from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import BookCategory, Book
from .forms import BookCategoryForm, BookForm

def book_category_list(request):
    categories = BookCategory.objects.all()
    return render(request, 'book_distribution_app/book_category_list.html', {'categories': categories})

def book_category_create(request):
    # Add logic to create a new book category here
    pass

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_distribution_app/book_list.html', {'books': books})

def book_create(request):
    # Add logic to create a new book here
    pass

def report_view(request):
    # Add logic to generate a report here
    pass


# Create your views here.
