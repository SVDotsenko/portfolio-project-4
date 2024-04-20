from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from author.forms import AuthorForm, AuthorFormInput
from author.models import Author
from book.models import Book


class AuthorList(View):
    def get(self, request):
        books = Book.objects.all()
        authors = Author.objects.all().order_by('id')
        for author in authors:
            author.read = any(book.author == author and book.reader
                              for book in books)
        return render(request, "author/authors.html", {'authors': authors})

    def post(self, request, author_id):
        get_object_or_404(Author, id=author_id).delete()
        return redirect('authors')


class AuthorDetail(View):
    def get(self, request, author_id=-1):
        form_input = AuthorFormInput()
        if author_id >= 0:
            name = get_object_or_404(Author, id=author_id).name
            form_input.fields['name'].initial = name
        return render(request, "author/author.html", {'form_input': form_input,
                                                      'author_id': author_id})

    def post(self, request, author_id=-1):
        if author_id < 0:
            author_form = AuthorForm(data=request.POST)
        else:
            author = get_object_or_404(Author, id=author_id)
            author_form = AuthorForm(data=request.POST, instance=author)

        if author_form.is_valid():
            author = author_form.save(commit=False)
            author.name = request.POST["name"]
            author.save()

        return redirect('authors')
