from django.test import TestCase


class TestCartView(TestCase):

    def test_view_cart(self):
        """
        A test to prove that the view gets to the cart template
        """
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart.html')
