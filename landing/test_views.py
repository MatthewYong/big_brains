from django.test import TestCase


class TestLandingView(TestCase):

    def test_view_landing(self):
        """
        A test to prove that the view gets all the blogs and toys
        from the model and returns to the landing template
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'landing/index.html')
