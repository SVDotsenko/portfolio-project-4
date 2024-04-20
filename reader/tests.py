import os

from django.conf import settings
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from reader.models import ProfileImage


class TestProfileDetail(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )

    def test_render_profile_page_authorised_user(self):
        self.client.login(username='myUsername', password='myPassword')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Information", response.content)
        self.assertIn(b"Profile Image", response.content)

    def test_render_profile_page_unauthorised_user(self):
        self.assertEqual(self.client.get(reverse('profile')).status_code, 302)

    def test_successful_profile_update(self):
        self.client.login(username='myUsername', password='myPassword')
        image_path = os.path.join(settings.BASE_DIR, 'static', 'img',
                                  'profile-image.png')
        with open(image_path, 'rb') as img_file:
            img_data = img_file.read()

        updated_data = {
            'first-name': 'UpdatedFirstName',
            'last-name': 'UpdatedLastName',
            'email': 'updated@test.com',
            'fileInput': SimpleUploadedFile("test_image.png", img_data,
                                            content_type="image/png")
        }

        self.client.post(reverse('profile'), data=updated_data)
        updated_user = User.objects.get(username='myUsername')
        self.assertEqual(updated_user.first_name, 'UpdatedFirstName')
        self.assertEqual(updated_user.last_name, 'UpdatedLastName')
        self.assertEqual(updated_user.email, 'updated@test.com')
        updated_image = ProfileImage.objects.get(user=updated_user)
        self.assertIsNotNone(updated_image.image.public_id)
