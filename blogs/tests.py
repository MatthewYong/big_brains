from django.test import TestCase
from .forms import BlogForm


class TestBlogForm(TestCase):

    def test_field_is_required(self):
        """
        A test case to prove that the form is working
        """
        form = BlogForm({'title': ''})
        self.assertTrue(form.is_valid)
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')
