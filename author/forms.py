from django import forms

from author.models import Author


class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name',)


class NameForm(forms.Form):
    name = forms.CharField(
        min_length=3,
        widget=forms.TextInput(attrs={
            'id': 'name',
            'name': 'name',
            'oninput': 'validateInput()',
            'class': 'form-control validate col-xl-9 col-lg-8 col-md-8 col-sm-7',
            'placeholder': 'Author name',
            'type': 'text',
        })
    )
