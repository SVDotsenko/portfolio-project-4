from django.contrib import admin
from book.models import Book
"""
Registers the Book model with the Django admin site.
"""
admin.site.register(Book)
