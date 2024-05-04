from django import forms
from author.models import Author


class AuthorForm(forms.ModelForm):
    """
    A form for creating or updating an Author instance.
    """
    class Meta:
        """
        The Meta class provides metadata for the Author form.
        It specifies the model to be used and the fields to be included in the form.
        """
        model = Author
        fields = ('name',)


class AuthorFormInput(forms.Form):
    """
    A form for inputting author information.

    Attributes:
        name (CharField): The name of the author.
    """
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
