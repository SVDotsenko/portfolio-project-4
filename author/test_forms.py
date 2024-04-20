import re
from django.test import TestCase
from author.forms import AuthorFormInput
from .forms import AuthorForm
from .models import Author


class TestAddAuthorForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = AuthorForm({'name': 'test'})
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    def test_name_is_required(self):
        """Test for the 'name' field"""
        form = AuthorForm({'name': ''})
        self.assertFalse(form.is_valid(), msg="Name was not provided")

    def test_form_meta_model(self):
        """Test the Meta model attribute"""
        form = AuthorForm()
        self.assertEqual(form.Meta.model, Author,
                         msg="Incorrect Meta model attribute")

    def test_form_meta_fields(self):
        """Test the Meta fields attribute"""
        form = AuthorForm()
        self.assertEqual(form.Meta.fields, ('name',),
                         msg="Incorrect Meta fields attribute")


class TestAuthorFormInput(TestCase):

    def test_valid_first_second_name(self):
        name = "William Shakespeare"
        form = AuthorFormInput(data={'name': name})
        pattern = form.fields['name'].widget.attrs['pattern']
        self.assertTrue(re.match(pattern, name))

    def test_invalid_first_name(self):
        name = "william Shakespeare"
        form = AuthorFormInput(data={'name': name})
        pattern = form.fields['name'].widget.attrs['pattern']
        self.assertFalse(re.match(pattern, name))

    def test_invalid_second_name(self):
        """Test for invalid second name."""
        name = "William shakespeare"
        form = AuthorFormInput(data={'name': name})
        pattern = form.fields['name'].widget.attrs['pattern']
        self.assertFalse(re.match(pattern, name))

    def test_empty_name(self):
        name = ""
        form = AuthorFormInput(data={'name': name})
        pattern = form.fields['name'].widget.attrs['pattern']
        self.assertFalse(re.match(pattern, name))
        self.assertFalse(form.is_valid())
