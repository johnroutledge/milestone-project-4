from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from django.contrib.auth.decorators import login_required

from profiles.models import UserProfile


def basket_contents(request):

    # if request.user.is_authenticated:
    #     profile = get_object_or_404(UserProfile, user=request.user)
    #     orders = profile.orders.all()

    basket_items = []
    total = 0
    discount = 0
    discounted_total = 0
    product_count = 0
    basket = request.session.get('basket', {})

    for item_id, item_data in basket.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            basket_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                basket_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })

    # Calculate delivery charges
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    # Caulculate grand total
    # if request.user.is_authenticated:
    #     profile = get_object_or_404(UserProfile, user=request.user)
    #     orders = profile.orders.all()

    #     if not orders:
    #         discount = total * Decimal(settings.FIRST_ORDER_DISCOUNT / 100)
    #         discounted_total = total - discount
    #         grand_total = delivery + discounted_total
    #     else:
    #         grand_total = delivery + total
    # else:
    #     grand_total = delivery + total

    grand_total = delivery + total

    context = {
        'basket_items': basket_items,
        'total': total,
        'discount': discount,
        'discounted_total': discounted_total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'first_order_discount': settings.FIRST_ORDER_DISCOUNT,
        'grand_total': grand_total,
    }

    return context
