def make_receipt(orders):
    receipt = 'Product, Quantity, Price, Customer'

    for order in orders:
        receipt = receipt + "\n%s, %s, %s, %s" % (
            str(order.purchaseOption.product), order.purchaseOption.quantity, str(order.purchaseOption.price_cents),
            str(order.customer))

    return receipt
