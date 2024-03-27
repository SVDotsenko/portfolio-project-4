from django.db import models
from django.contrib.auth.models import User
from author.models import Author


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    reader = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
