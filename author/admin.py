from django.contrib import admin
from author.models import Author
"""
This module registers the Author model with the Django admin site.
"""
admin.site.register(Author)
