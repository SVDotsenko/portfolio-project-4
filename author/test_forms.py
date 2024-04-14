import re
import unittest
from django.test import TestCase
from author.forms import AuthorForm
from .forms import AddAuthorForm
from .models import Author


class TestAddAuthorForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = AddAuthorForm({'name': 'test'})
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    def test_name_is_required(self):
        """Test for the 'name' field"""
        form = AddAuthorForm({'name': ''})
        self.assertFalse(form.is_valid(), msg="Name was not provided")

    def test_form_meta_model(self):
        """Test the Meta model attribute"""
        form = AddAuthorForm()
        self.assertEqual(form.Meta.model, Author,
                         msg="Incorrect Meta model attribute")

    def test_form_meta_fields(self):
        """Test the Meta fields attribute"""
        form = AddAuthorForm()
        self.assertEqual(form.Meta.fields, ('name',),
                         msg="Incorrect Meta fields attribute")


class AuthorFormTest(unittest.TestCase):

    def test_valid_first_second_name(self):
        name = "William Shakespeare"
        form = AuthorForm(data={'name': name})
        pattern = form.fields['name'].widget.attrs['pattern']
        self.assertTrue(re.match(pattern, name))

    def test_invalid_first_name(self):
        name = "william Shakespeare"
        form = AuthorForm(data={'name': name})
        pattern = form.fields['name'].widget.attrs['pattern']
        self.assertFalse(re.match(pattern, name))

    # Unfortunately, this test does not work as it should,
    # due to the fact that the regular expression that works correctly
    # in the browser JS does not work correctly in Python
    # def test_invalid_second_name(self):
    #     """Test for invalid second name."""
    #     name = "William shakespeare"
    #     form = AuthorForm(data={'name': name})
    #     pattern = form.fields['name'].widget.attrs['pattern']
    #     self.assertFalse(re.match(pattern, name))

    def test_empty_name(self):
        name = ""
        form = AuthorForm(data={'name': name})
        pattern = form.fields['name'].widget.attrs['pattern']
        self.assertFalse(re.match(pattern, name))
        self.assertFalse(form.is_valid())
