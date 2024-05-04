from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from author.forms import AuthorForm, AuthorFormInput
from author.models import Author
from book.models import Book


class AuthorList(View):
    def get(self, request):
        """
        Retrieves all books and authors from the database and renders the
        'authors.html' template.

        Returns:
            HttpResponse: The rendered template with the author's data.
        """
        books = Book.objects.all()
        authors = Author.objects.all().order_by('id')
        for author in authors:
            author.read = any(book.author == author and book.reader
                              for book in books)
        return render(request, "author/authors.html", {'authors': authors})

    def post(self, request, author_id):
        """
        Handle HTTP POST request to delete an author.

        Args:
            request (HttpRequest): The HTTP request object.
            author_id (int): The ID of the author to be deleted.

        Returns:
            HttpResponseRedirect: A redirect response to the 'authors' page.

        Raises:
            Http404: If the author with the specified ID does not exist.
        """
        author = get_object_or_404(Author, id=author_id)
        author.delete()
        messages.add_message(request, messages.SUCCESS,
                             f'{author.name} was removed')
        return redirect('authors')


class AuthorDetail(View):
    def get(self, request, author_id=-1):
        """
        Handles the GET request for the author view.

        Args:
            request (HttpRequest): The HTTP request object.
            author_id (int, optional): The ID of the author. Defaults to -1.

        Returns:
            HttpResponse: The HTTP response object.
        """
        form_input = AuthorFormInput()
        if author_id >= 0:
            name = get_object_or_404(Author, id=author_id).name
            form_input.fields['name'].initial = name
        return render(request, "author/author.html", {'form_input': form_input,
                                                      'author_id': author_id})

    def post(self, request, author_id=-1):
        """
        Handle the HTTP POST request for creating or updating an author.

        Args:
            request (HttpRequest): The HTTP request object.
            author_id (int, optional): The ID of the author to be updated.
            Defaults to -1.

        Returns:
            HttpResponseRedirect: A redirect response to the 'authors' page.

        """
        if author_id < 0:
            author_form = AuthorForm(data=request.POST)
            action_message = 'added'
        else:
            author = get_object_or_404(Author, id=author_id)
            author_form = AuthorForm(data=request.POST, instance=author)
            action_message = 'updated'

        if author_form.is_valid():
            author = author_form.save(commit=False)
            author.name = request.POST["name"]
            author.save()
            messages.add_message(request, messages.SUCCESS,
                                 f'{author.name} was {action_message}')
        return redirect('authors')
