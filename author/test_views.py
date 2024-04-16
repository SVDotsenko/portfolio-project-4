from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from author.models import Author


class TestAuthorView(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.author = Author(name="Test Author")
        self.author.save()

    def test_render_authors_page_authorised_user(self):
        self.client.login(username='myUsername', password='myPassword')
        response = self.client.get(reverse('authors'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Authors", response.content)
        self.assertIn(b"Add Author", response.content)

    def test_render_authors_page_unauthorised_user(self):
        response = self.client.get(reverse('authors'))
        self.assertEqual(response.status_code, 302)

    def test_successful_author_creation(self):
        self.client.login(username='myUsername', password='myPassword')
        post_data = {'name': 'Test Author2'}
        response = self.client.post(reverse('add_author'), post_data)
        self.assertEqual(response.status_code, 302)
