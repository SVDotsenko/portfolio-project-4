from django.contrib import messages
from django.contrib.auth import get_user
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from author.models import Author
from .forms import BookForm
from .models import Book


class BookList(View):
    def get(self, request):
        return render(request, "book/books.html",
                      {'books': Book.objects.all().order_by('id')})

    def post(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        book.delete()
        messages.add_message(request, messages.SUCCESS,
                f'The book "{book.title}" by {book.author.name} was removed')
        return redirect('books')


class BookDetail(View):
    def get(self, request, book_id=-1):
        context = {'object_list': Author.objects.all()}
        if book_id >= 0:
            queryset = Book.objects.filter(id=book_id)
            context['book'] = get_object_or_404(queryset, id=book_id)
        return render(request, "book/book.html", context)

    def post(self, request, book_id=-1):
        if book_id < 0:
            book_form = BookForm(data=request.POST)
            action_message = 'added'
        else:
            book = get_object_or_404(Book, id=book_id)
            book_form = BookForm(data=request.POST, instance=book)
            action_message = 'updated'

        if book_form.is_valid():
            book = book_form.save(commit=False)
            book.title = request.POST["title"]
            book.author = Author.objects.filter(id=request.POST["author"])[0]
            book.save()
            messages.add_message(request, messages.SUCCESS,
            f'The book "{book.title}" by {book.author.name} was {action_message}')
        return redirect('books')


def toggle_reader(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if book.reader:
        book.reader = None
        message = 'You returned this book'
    else:
        book.reader = get_user(request)
        message = 'You took this book'
    book.save()
    messages.add_message(request, messages.SUCCESS, message)
    return redirect('books')
