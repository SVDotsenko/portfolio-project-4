from django import forms

from reader.models import ProfileImage


class AddProfileImageForm(forms.ModelForm):
    class Meta:
        model = ProfileImage
        fields = ('image',)
