from django.test import TestCase

from author.models import Author
from book.forms import BookForm
from book.models import Book


class BookFormTest(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = BookForm({'title': 'Book Title',
                         'author': Author.objects.create(name='Author Name')})
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    def test_name_is_required(self):
        """Test for the 'title' field"""
        form = BookForm({'title': '',
                         'author': Author.objects.create(name='Author Name')})
        self.assertFalse(form.is_valid(), msg="Title was not provided")

    def test_form_meta_model(self):
        """Test the Meta model attribute"""
        form = BookForm()
        self.assertEqual(form.Meta.model, Book,
                         msg="Incorrect Meta model attribute")

    def test_form_meta_fields(self):
        """Test the Meta fields attribute"""
        form = BookForm()
        self.assertEqual(form.Meta.fields, ('title', 'author',),
                         msg="Incorrect Meta fields attribute")
