from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from author.models import Author


class TestAuthorView(TestCase):

    def setUp(self):
        """
        Set up the test environment by creating a superuser,
        an author, and saving the author.
        """
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.author = Author(name="Test Author")
        self.author.save()

    def test_render_authors_page_authorised_user_admin(self):
        """
        Test case to verify that the authors page is rendered correctly for
        an authorised user with admin privileges.
        """
        self.client.login(username='myUsername', password='myPassword')
        response = self.client.get(reverse('authors'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Authors", response.content)
        self.assertIn(b"Add Author", response.content)

    def test_render_authors_page_authorised_user_not_admin(self):
        """
        Test case to verify that an authorized user who is not an admin
        receives a 403 Forbidden response when accessing the authors page.
        """
        self.user = User.objects.create_user(
            username='reader',
            password='readerPassword',
            email='test@test.com'
        )
        self.client.login(username='reader', password='readerPassword')
        response = self.client.get(reverse('authors'))
        self.assertIn('403', response.url)

    def test_render_authors_page_unauthorised_user(self):
        """
        Test case to verify that an unauthorised user is redirected to
        the login page when trying to access the authors page.
        """
        response = self.client.get(reverse('authors'))
        self.assertEqual(response.status_code, 302)

    def test_successful_author_creation(self):
        """Test case to verify successful creation of an author."""
        self.client.login(username='myUsername', password='myPassword')
        post_data = {'name': 'Test Author2'}
        self.assertEqual(Author.objects.count(), 1)
        self.client.post(reverse('add_author'), post_data)
        self.assertEqual(Author.objects.count(), 2)

    def test_add_author_non_admin(self):
        """
        Test case to verify that a non-admin user cannot add an author.
        """
        self.user = User.objects.create_user(
            username='reader',
            password='readerPassword',
            email='test@test.com'
        )
        self.client.login(username='reader', password='readerPassword')
        post_data = {'name': 'Test Author2'}
        original_count = Author.objects.count()
        self.client.post(reverse('add_author'), post_data)
        self.assertEqual(Author.objects.count(), original_count)
        response = self.client.get(reverse('add_author'))
        self.assertEqual(response.status_code, 302)

    def test_successful_author_update(self):
        """Test case to verify successful author update."""
        self.client.login(username='myUsername', password='myPassword')
        new_name = 'William Shakespeare'
        response = self.client.get(reverse('update_author', kwargs={
            'author_id': self.author.id}))

        self.assertEqual(response.context['form_input'].fields['name'].initial,
                         self.author.name)

        self.client.post(reverse('update_author', kwargs={
            'author_id': self.author.id}), {'name': new_name})
        updated_name = Author.objects.get(id=self.author.id).name
        self.assertEqual(updated_name, new_name)

    def test_update_author_non_admin(self):
        """
        Test case to verify that a non-admin user cannot update an author.
        """
        self.user = User.objects.create_user(
            username='reader',
            password='readerPassword',
            email='test@test.com'
        )
        self.client.login(username='reader', password='readerPassword')
        post_data = {'name': 'Updated Author'}

        original_name = self.author.name
        self.client.post(
            reverse('update_author', kwargs={'author_id': self.author.id}),
            post_data)

        self.author.refresh_from_db()

        self.assertEqual(self.author.name, original_name)
        response = self.client.get(
            reverse('update_author', kwargs={'author_id': self.author.id}))
        self.assertEqual(response.status_code, 302)

    def test_successful_author_delete(self):
        """Test case to verify successful deletion of an author."""
        self.client.login(username='myUsername', password='myPassword')
        self.assertEqual(Author.objects.count(), 1)
        self.client.post(
            reverse('delete_author', kwargs={'author_id': self.author.id}))
        self.assertEqual(Author.objects.count(), 0)

    def test_delete_author_non_admin(self):
        """
        Test case to verify that a non-admin user cannot delete an author.
        """
        self.user = User.objects.create_user(
            username='reader',
            password='readerPassword',
            email='test@test.com'
        )
        self.client.login(username='reader', password='readerPassword')
        original_count = Author.objects.count()
        self.client.post(
            reverse('delete_author', kwargs={'author_id': self.author.id}))
        self.assertEqual(Author.objects.count(), original_count)
