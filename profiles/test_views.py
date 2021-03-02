from django.test import TestCase
from django.contrib.auth.models import User


class TestProfileView(TestCase):

    def test_view_profiles(self):
        """
        A test to prove that the view gets to the profiles template
        """
        test_view_user = User.objects.create_user(
            username='test_name',
            email='test_email@email.com',
            password=None)

        self.client.force_login(test_view_user)
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
