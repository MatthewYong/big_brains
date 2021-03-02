from django.test import TestCase


class TestProfileView(TestCase):

    def test_view_profiles(self):
        """
        A test to prove that the view gets to the profiles template
        """
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
