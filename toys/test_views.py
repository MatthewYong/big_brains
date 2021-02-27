from django.test import TestCase


class TestToysViews(TestCase):

    def test_get_all_toys(self):
        """
        A test case to prove that the view gets
        all the toys from the model
        """
        response = self.client.get('/toys/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'toys/toys.html')
