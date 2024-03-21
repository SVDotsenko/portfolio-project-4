from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Book, Author


class BookList(generic.ListView):
    queryset = Book.objects.all()
    template_name = "blog/index.html"


def book_edit(request, id):
    authors = Author.objects.all()
    queryset = Book.objects.filter(id=id)
    book = get_object_or_404(queryset, id=id)
    return render(
        request,
        "blog/create-update.html",
        {
            "book": book,
            "authors": authors
        },
    )
