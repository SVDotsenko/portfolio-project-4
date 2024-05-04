from django.contrib import messages
from django.contrib.auth import get_user
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from author.models import Author
from .forms import BookForm
from .models import Book


class BookList(View):
    def get(self, request):
        """
        Handle GET requests for the view.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
       HttpResponse: The HTTP response object containing the rendered template.
        """
        return render(request, "book/books.html",
                      {'books': Book.objects.all().order_by('id')})

    def post(self, request, book_id):
        """
        Handle the HTTP POST request to delete a book.

        Args:
            request (HttpRequest): The HTTP request object.
            book_id (int): The ID of the book to be deleted.

        Returns:
            HttpResponseRedirect: A redirect response to the 'books' URL.

        Raises:
            Http404: If the book with the specified ID does not exist.
        """
        book = get_object_or_404(Book, id=book_id)
        book.delete()
        messages.add_message(request, messages.SUCCESS,
                             f'The book "{book.title}" by {book.author.name} '
                             f'was removed')
        return redirect('books')


class BookDetail(View):
    def get(self, request, book_id=-1):
        """
        Handles the GET request for the book view.

        Args:
            request (HttpRequest): The HTTP request object.
            book_id (int, optional): The ID of the book. Defaults to -1.

        Returns:
            HttpResponse: The rendered book template with the context.
        """
        context = {'object_list': Author.objects.all()}
        if book_id >= 0:
            queryset = Book.objects.filter(id=book_id)
            context['book'] = get_object_or_404(queryset, id=book_id)
        return render(request, "book/book.html", context)

    def post(self, request, book_id=-1):
        """
        Handle the HTTP POST request for creating or updating a book.

        Args:
            request (HttpRequest): The HTTP request object.
            book_id (int, optional): The ID of the book to be updated.
            Defaults to -1.

        Returns:
            HttpResponseRedirect: A redirect response to the 'books' URL.

        """
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
                                 f'The book "{book.title}" by '
                                 f'{book.author.name} was '
                                 f'{action_message}')
        return redirect('books')


def toggle_reader(request, book_id):
    """
    Add or remove the reader to a book.

    Parameters:
    - request: The HTTP request object.
    - book_id: The ID of the book to toggle the reader.

    Returns:
    - A redirect response to the 'books' page.

    """
    book = get_object_or_404(Book, id=book_id)
    if book.reader:
        book.reader = None
        message = f'You returned the book "{book.title}" by {book.author.name}'
    else:
        book.reader = get_user(request)
        message = f'You took the book "{book.title}" by {book.author.name}'
    book.save()
    messages.add_message(request, messages.SUCCESS, message)
    return redirect('books')
