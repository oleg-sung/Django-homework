
from django.shortcuts import render

from books.models import Book


def books_view(request):
    books = Book.objects.all()
    template = 'books/books_list.html'
    context = {'books': books}
    return render(request, template, context)


def book_date(request, pub_date):
    template = 'books/books_date.html'
    books_objects = Book.objects.filter(pub_date=pub_date)
    books_next = (Book.objects.filter(pub_date__gt=pub_date).order_by('pub_date').first())
    if books_next:
        books_next = str(books_next.pub_date)
    else:
        books_next = None
    books_previous = Book.objects.filter(pub_date__lt=pub_date).order_by('pub_date').first()
    if books_previous:
        books_previous = str(books_previous.pub_date)
    else:
        books_previous = None
    context = {
        'books': books_objects,
        'next_book': books_next,
        'previous_book': books_previous,
    }
    return render(request, template, context)
