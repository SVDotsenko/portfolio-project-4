from django.urls import reverse
from django.contrib.auth.models import User
from django.test import TestCase
from author.models import Author
from book.models import Book


class TestBookView(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.author = Author(name="Test Author")
        self.book = Book(title='Book title', author=self.author)
        self.author.save()
        self.book.save()

    def test_render_books_page_authorised_user(self):
        self.client.login(username='myUsername', password='myPassword')
        response = self.client.get(reverse('books'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Books", response.content)
        self.assertIn(b"Add Book", response.content)

    def test_successful_book_creation(self):
        self.client.login(username='myUsername', password='myPassword')
        post_data = {'title': 'Book title2', 'author': self.author.id}
        self.assertEqual(Book.objects.count(), 1)
        self.client.post(reverse('add_book'), post_data)
        self.assertEqual(Book.objects.count(), 2)

    def test_successful_book_update(self):
        self.client.login(username='myUsername', password='myPassword')
        new_title = 'Book title2'
        self.client.post(
            reverse('update_book', kwargs={'book_id': self.book.id}),
            {'title': new_title, 'author': self.author.id})
        updated_title = Book.objects.get(id=1).title
        self.assertEqual(updated_title, new_title)

    def test_successful_book_delete(self):
        self.client.login(username='myUsername', password='myPassword')
        self.assertEqual(Book.objects.count(), 1)
        self.client.post(
            reverse('delete_book', kwargs={'book_id': self.book.id}))
        self.assertEqual(Book.objects.count(), 0)

    def test_toggle_reader(self):
        self.user = User.objects.create_user(
            username="reader",
            password="readerPassword",
            email="reader@test.com"
        )
        self.client.login(username='reader', password='readerPassword')
        self.assertIsNone(self.book.reader)
        self.client.post(
            reverse('toggle_reader', kwargs={'book_id': self.book.id}))
        self.book.refresh_from_db()
        self.assertEqual(self.book.reader, self.user)
        self.client.post(
            reverse('toggle_reader', kwargs={'book_id': self.book.id}))
        self.book.refresh_from_db()
        self.assertIsNone(self.book.reader)
