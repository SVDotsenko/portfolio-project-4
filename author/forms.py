from django import forms

from author.models import Author


class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name',)
