from django.views import generic
from .models import Book


class BookList(generic.ListView):
    queryset = Book.objects.all()
    template_name = "blog/index.html"
