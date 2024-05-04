from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    """
    A form for creating or updating a book.

    Inherits from forms.ModelForm and uses the Book model.
    The form includes fields for the book's title and author.
    """

    class Meta:
        """
        The Meta class provides additional information about the form.
        It specifies the model to be used and the fields to be included in the
        form.
        """
        model = Book
        fields = ('title', 'author',)
