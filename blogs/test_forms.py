from django.test import TestCase
from .forms import BlogForm


class TestBlogForm(TestCase):

    def test_field_title_is_required(self):
        """
        A test case to prove that title field in the form
        is required
        """
        form = BlogForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_field_image_url_is_not_required(self):
        """
        A test case to prove that imageurl field in the form
        is not required
        """
        form = BlogForm({'image_url': 'test'})
        self.assertTrue(form.is_valid())
