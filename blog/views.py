from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect

from .forms import AddBookForm
from .models import Book, Author


class BookList(generic.ListView):
    queryset = Book.objects.all()
    template_name = "blog/index.html"


def book_edit(request, book_id):
    authors = Author.objects.all()
    queryset = Book.objects.filter(id=book_id)
    book = get_object_or_404(queryset, id=book_id)
    return render(
        request,
        "blog/create-update.html",
        {
            "book": book,
            "authors": authors
        },
    )


class AddBookView(generic.ListView):
    model = Book
    queryset = Author.objects.all()
    template_name = "blog/create-book.html"


def create_book(request):
    if request.method == "POST":
        book_form = AddBookForm(data=request.POST)
        if book_form.is_valid():
            book = book_form.save(commit=False)
            book.title = request.POST["title"]
            book.author = Author.objects.filter(id=request.POST["author"])[0]
            book.reader = request.user
            book.save()

    return HttpResponseRedirect(reverse('home'))
