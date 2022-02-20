""" Testing code adapted from Code Institute BoutiqueAdo project """
from django.test import TestCase

from .models import Order
from products.models import Product


class TestOrderModels(TestCase):
    """ Test order model works """
    def test_order_string_method_returns_order_number(self):
        """
        Test order model string method
        """
        order_number = Order.objects.create(order_number='999')
        self.assertEqual(str(order_number), '999')


class TestOrderLineItemModel(TestCase):
    """ Test order line item model works """
    def test_order_line_item_string_method_returns_sku_and_order_number(self):
        """
        Test order line item model string method
        """
        product = Product.objects.create(sku="j999", price=9.99)
        order = Order.objects.create(order_number="999")
        correct = "SKU j999 on order 999"
        self.assertEqual(str(
            f'SKU {product.sku} on order {order.order_number}'), correct)
