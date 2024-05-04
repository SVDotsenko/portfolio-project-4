from django.db import models
from django.contrib.auth.models import User
from author.models import Author


class Book(models.Model):
    """
    Represents a book in the library.

    Attributes:
        title (str): The title of the book.
        author (Author): The author of the book.
        reader (User): The user who is currently reading the book.
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    reader = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
