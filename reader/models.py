from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db import models


class ProfileImage(models.Model):
    """
    Represents a user's profile image.

    Attributes:
        user (User): The user associated with the profile image.
        image (CloudinaryField): The image field for storing the profile image.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField('image', default='placeholder')
