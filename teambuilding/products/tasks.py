from django.core.mail import send_mail
from django.utils.translation import gettext


def send_order_email_to_producer(order):
    small_orders = order.product_order_set
    email = order.producer.email
    receipt = ""

    for small_order in small_orders:
        receipt = receipt + "- " + "%(order)s" % ({'order': str(small_order)}) + "\n"

    message = gettext("Orders:\n%(receipt)s\nDelivery address:\n%(address)s") % (
        {'receipt': receipt, 'address': str(order.address)}
    )

    send_mail(
        gettext("New order"),
        message,
        None,
        [email],
        fail_silently=True
    )
