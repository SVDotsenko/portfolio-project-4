from django import forms
from .models import Book


class EditBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author',)
