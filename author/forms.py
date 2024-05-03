from django import forms
from author.models import Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name',)


class AuthorFormInput(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'id': 'name',
            'oninput': 'validateInput()',
            'class': 'form-control',
            'placeholder': 'Author name',
            'type': 'text',
            'pattern': '^[A-Z][a-zA-Z]*( [A-Z][a-zA-Z]*)*$',
            'title': 'Server validation: Each word must start with a capital '
                     'letter separated by a space',
        })
    )
