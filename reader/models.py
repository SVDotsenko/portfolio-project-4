from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db import models


class ProfileImage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField('image', default='placeholder')
