from django import forms

from reader.models import ProfileImage


class ProfileImageForm(forms.ModelForm):
    class Meta:
        model = ProfileImage
        fields = ('image',)
