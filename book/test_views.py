from django.urls import reverse
from django.contrib.auth.models import User
from django.test import TestCase
from author.models import Author
from book.models import Book


class TestBookView(TestCase):

    def setUp(self):
        """
        Set up the necessary objects and data for the test case.
        """
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
        """
        Test case to verify that the books page is rendered correctly for an
        authorised user.
        """
        self.client.login(username='myUsername', password='myPassword')
        response = self.client.get(reverse('books'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Books", response.content)
        self.assertIn(b"Add Book", response.content)

    def test_successful_book_creation(self):
        """
        Test case to verify successful book creation.

        This test logs in a user, creates a book using the 'add_book' view,
        and then checks if the book count has increased by 1.

        """
        self.client.login(username='myUsername', password='myPassword')
        post_data = {'title': 'Book title2', 'author': self.author.id}
        self.assertEqual(Book.objects.count(), 1)
        self.client.post(reverse('add_book'), post_data)
        self.assertEqual(Book.objects.count(), 2)

    def test_successful_book_update(self):
        """
        Test case to verify successful book update.

        This test case logs in a user, retrieves a book object, updates its
        title, and verifies that the title has been successfully updated in the
        database.
        """
        self.client.login(username='myUsername', password='myPassword')
        new_title = 'Book title2'
        response = self.client.get(reverse('update_book',
                                           kwargs={'book_id': self.book.id}))
        self.assertEqual(response.context['book'].id, self.book.id)
        self.client.post(
            reverse('update_book', kwargs={'book_id': self.book.id}),
            {'title': new_title, 'author': self.author.id})
        updated_title = Book.objects.get(id=self.book.id).title
        self.assertEqual(updated_title, new_title)

    def test_successful_book_delete(self):
        """
        Test case to verify successful deletion of a book.

        This test logs in a user, creates a book, and then deletes it using the
        `delete_book` view.
        It asserts that the book count before and after the deletion is as
        expected.
        """
        self.client.login(username='myUsername', password='myPassword')
        self.assertEqual(Book.objects.count(), 1)
        self.client.post(
            reverse('delete_book', kwargs={'book_id': self.book.id}))
        self.assertEqual(Book.objects.count(), 0)

    def test_toggle_reader(self):
        """
        Test case for toggling the reader of a book.

        This test checks if the reader of a book can be toggled correctly.
        It creates a user, logs in as the user, and checks if the initial
        reader of the book is None.
        Then it sends a POST request to toggle the reader of the book and
        checks if the reader is updated correctly.
        Finally, it sends another POST request to toggle the reader back to
        None and checks if the reader is set to None again.
        """
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
