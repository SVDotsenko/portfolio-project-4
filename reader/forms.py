from django import forms

from reader.models import ProfileImage


class ProfileImageForm(forms.ModelForm):
    """
    A form for uploading a profile image.

    This form is used to upload a profile image for a user.

    Attributes:
        image (FileField): The field for uploading the image.

    """
    class Meta:
        """
        The Meta class provides additional information about the ModelForm class.
        It specifies the model to be used and the fields to be included in the form.
        """

        model = ProfileImage
        fields = ('image',)
