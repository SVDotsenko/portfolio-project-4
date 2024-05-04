from django.db import models


class Author(models.Model):
    """
    Represents an author in the system.
    """
    name = models.CharField(max_length=200)
