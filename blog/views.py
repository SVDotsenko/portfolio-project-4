from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views import View
from .forms import AddBookForm
from .models import Book, Author


class BookList(View):
    def get(self, request, book_id=-1):
        books = Book.objects.all()
        if book_id < 0:
            context = {'object_list': books}
            return render(request, "blog/book/index.html", context)
        get_object_or_404(books, id=book_id).delete()
        return redirect('home')


class BookDetail(View):
    def get(self, request, book_id=-1):
        context = {'object_list': Author.objects.all()}
        if book_id >= 0:
            queryset = Book.objects.filter(id=book_id)
            context['book'] = get_object_or_404(queryset, id=book_id)
        return render(request, "blog/book/book.html", context)

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
            book.reader = request.user
            book.save()

        return redirect('home')


class AuthorList(generic.ListView):
    queryset = Author.objects.all()
    template_name = "blog/author/index.html"
