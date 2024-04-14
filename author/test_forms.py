from django.test import TestCase
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