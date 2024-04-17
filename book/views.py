from django.contrib.auth import get_user
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from author.models import Author
from .forms import AddBookForm
from .models import Book


class BookList(View):
    def get(self, request):
        return render(request, "book/books.html",
                      {'books': Book.objects.all().order_by('id')})

    def post(self, request, book_id):
        get_object_or_404(Book, id=book_id).delete()
        return redirect('home')


def toggle_reader(request, book_id):
    books = Book.objects.all()
    book = get_object_or_404(books, id=book_id)
    book.reader = None if book.reader else get_user(request)
    book.save()
    return redirect('home')


class BookDetail(View):
    def get(self, request, book_id=-1):
        context = {'object_list': Author.objects.all()}
        if book_id >= 0:
            queryset = Book.objects.filter(id=book_id)
            context['book'] = get_object_or_404(queryset, id=book_id)
        return render(request, "book/book.html", context)

    def post(self, request, book_id=-1):
        if book_id < 0:
            book_form = AddBookForm(data=request.POST)
        else:
            book = get_object_or_404(Book, id=book_id)
            book_form = AddBookForm(data=request.POST, instance=book)

        if book_form.is_valid():
            book = book_form.save(commit=False)
            book.title = request.POST["title"]
            book.author = Author.objects.filter(id=request.POST["author"])[0]
            book.save()

        return redirect('home')
