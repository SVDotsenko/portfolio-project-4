from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from .forms import AddBookForm
from .models import Book, Author


class BookList(generic.ListView):
    queryset = Book.objects.all()
    template_name = "blog/index.html"


class AddBookView(generic.ListView):
    model = Book
    queryset = Author.objects.all()
    template_name = "blog/create-book.html"


def update_book(request, book_id):
    if request.method == "POST":
        book = get_object_or_404(Book, id=book_id)
        book_form = AddBookForm(data=request.POST, instance=book)
        if book_form.is_valid():
            book = book_form.save(commit=False)
            book.title = request.POST["title"]
            book.author = Author.objects.filter(id=request.POST["author"])[0]
            book.reader = request.user
            book.save()

        return HttpResponseRedirect(reverse('home'))

    authors = Author.objects.all()
    queryset = Book.objects.filter(id=book_id)
    book = get_object_or_404(queryset, id=book_id)
    return render(
        request,
        "blog/update-book.html",
        {
            "book": book,
            "authors": authors
        },
    )


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
