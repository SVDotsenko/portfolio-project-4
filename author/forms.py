from django import forms
from author.models import Author


class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name',)


class AuthorForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'id': 'name',
            'name': 'name',
            'oninput': 'validateInput()',
            'class': 'form-control validate col-xl-9 col-lg-8 col-md-8 '
                     'col-sm-7',
            'placeholder': 'Author name',
            'type': 'text',
            'pattern': '[A-Z][a-z]*(\s[A-Z][a-z]*)*',
            'title': 'Server validation: Each word must start with a capital '
                     'letter separated by a space',
        })
    )
