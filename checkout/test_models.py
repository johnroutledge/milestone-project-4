# Testing code adapted from Code Institute BoutiqueAdo project
from django.test import TestCase

from .models import Order


class TestOrderModels(TestCase):  # pragma: no cover
    """ Test checkout model works """
    def test_order_string_method_returns_order_number(self):
        """
        Test order string method
        """
        order_number = Order.objects.create(order_number='999')
        self.assertEqual(str(order_number), '999')
