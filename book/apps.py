from django.apps import AppConfig


class BookConfig(AppConfig):
    """
    AppConfig for the 'book' app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'book'
