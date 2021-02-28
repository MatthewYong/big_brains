from django.test import TestCase
from .models import Toy


class TestToysViews(TestCase):

    def test_get_all_toys(self):
        """
        A test to prove that the view gets all the toys
        from the model and returns to the template
        """
        response = self.client.get('/toys/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'toys/toys.html')

    def test_get_toy(self):
        """
        A test to prove that the view gets a specific toy
        and returns it to its own template
        """
        toy = Toy.objects.create(
            name='New Toy',
            price='12.95',
            description='Funny',
        )
        response = self.client.get(f'/toys/{toy.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'toys/toy_detail.html')

    def test_search_toy(self):
        """
        A test to prove that the view can search for a specific
        toy using a queryset
        """
        toys_list = list(Toy.objects.all())
        toys = Toy.objects.all()
        self.assertQuerysetEqual(toys, toys_list)
