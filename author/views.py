from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from author.forms import AddAuthorForm
from author.models import Author
from blog.models import Book


class AuthorList(View):
    def get_authors(self):
        books = Book.objects.all()
        authors = Author.objects.all().order_by('id')
        for author in authors:
            author.read = any(book.author == author and book.reader
                              for book in books)
        return authors

    def get(self, request, author_id=-1):
        authors = self.get_authors()
        if author_id < 0:
            context = {'object_list': authors}
            return render(request, "author/index.html", context)
        get_object_or_404(authors, id=author_id).delete()
        return redirect('authors')


class AuthorDetail(View):
    def get(self, request, author_id=-1):
        if author_id >= 0:
            queryset = Author.objects.filter(id=author_id)
            context = {'author': get_object_or_404(queryset, id=author_id)}
            return render(request, "author/author.html", context)
        return render(request, "author/author.html")

    def post(self, request, author_id=-1):
        if author_id < 0:
            author_form = AddAuthorForm(data=request.POST)
        else:
            author = get_object_or_404(Author, id=author_id)
            author_form = AddAuthorForm(data=request.POST, instance=author)

        if author_form.is_valid():
            author = author_form.save(commit=False)
            author.name = request.POST["name"]
            author.save()

        return redirect('authors')
