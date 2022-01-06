from django.contrib.auth.decorators import login_required
from django.http.response import Http404
from django.shortcuts import redirect, render, get_object_or_404

from apps.products.forms import ProductForm, ProducerForm, ProductPurchaseOptionForm, ProducerPostalAddressForm
from apps.products.models import Product, Producer, ProductPurchaseOption
from services.postal_address.localization import localize_form
from services.postal_address.services import is_country_code_valid, safe_country_code


@login_required
def list_all(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product/list.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        option_form = ProductPurchaseOptionForm(request.POST, exclude_product_field=True)

        if form.is_valid():
            product = form.save(commit=False)
            option_form.instance.product = product

            if option_form.is_valid():
                form.save()
                option_form.save()
                return redirect('product-list')
    else:
        form = ProductForm()
        option_form = ProductPurchaseOptionForm(exclude_product_field=True)

    context = {'product_form': form, 'option_form': option_form}
    return render(request, 'product/create.html', context)


@login_required
def update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    options = ProductPurchaseOption.objects.filter(product_id__exact=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)

        if form.is_valid():
            form.save()
            return redirect('product-list')
    else:
        form = ProductForm(instance=product)

    context = {'pk': pk, 'options': options, 'product_form': form}
    return render(request, 'product/update.html', context)


@login_required
def delete(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product.delete()
        return redirect('product-list')

    context = {'product': product}
    return render(request, 'product/delete.html', context)


@login_required
def producer_list_all(request):
    producers = Producer.objects.all()
    context = {'producers': producers}
    return render(request, 'product-producer/list.html', context)


@login_required
def producer_create(request, country=None):
    if not is_country_code_valid(country):
        country = safe_country_code(country)
        return redirect('product-producer-create', country=country)

    if request.method == 'POST':
        form = ProducerForm(request.POST)
        address_form = localize_form(country, ProducerPostalAddressForm(request.POST))

        if form.is_valid():
            producer = form.save(commit=False)
            address_form.instance.producer = producer

            if address_form.is_valid():
                form.save()
                address_form.save()
                return redirect('product-producer-list')
    else:
        form = ProducerForm()
        address_form = localize_form(country, ProducerPostalAddressForm())

    context = {'producer_form': form, 'address_form': address_form}
    return render(request, 'product-producer/create.html', context)


@login_required
def producer_update(request, pk, country=None):
    if not is_country_code_valid(country):
        producer = get_object_or_404(Producer, pk=pk)
        country = producer.producerpostaladdress.country.country_code
        return redirect('product-producer-update', pk=pk, country=country)

    producer = get_object_or_404(Producer, pk=pk)
    address = producer.producerpostaladdress

    if request.method == 'POST':
        form = ProducerForm(request.POST, instance=producer)
        address_form = localize_form(country, ProducerPostalAddressForm(request.POST, instance=address))

        if form.is_valid() and address_form.is_valid():
            form.save()
            address_form.save()
            return redirect('product-producer-list')
    else:
        form = ProducerForm(instance=producer)
        address_form = localize_form(country, ProducerPostalAddressForm(instance=address))

    context = {'pk': pk, 'producer_form': form, 'address_form': address_form}
    return render(request, 'product-producer/update.html', context)


@login_required
def producer_delete(request, pk):
    producer = get_object_or_404(Producer, pk=pk)

    if request.method == 'POST':
        producer.delete()
        return redirect('product-producer-list')

    context = {'producer': producer}
    return render(request, 'product-producer/delete.html', context)


@login_required
def purchase_option_create(request, product_id):
    if not Product.objects.filter(pk=product_id).exists():
        raise Http404

    if request.method == 'POST':
        form = ProductPurchaseOptionForm(request.POST, product_id=product_id)

        if form.is_valid():
            form.save()
            return redirect('product-update', pk=product_id)
    else:
        form = ProductPurchaseOptionForm(product_id=product_id)

    context = {'option_form': form}
    return render(request, 'product-purchase-option/create.html', context)


@login_required
def purchase_option_update(request, pk, product_id=None):
    option = get_object_or_404(ProductPurchaseOption, pk=pk)

    if not product_id:
        product_id = option.product.id
        return redirect('product-purchase-option-update', pk=pk, product_id=product_id)

    if request.method == 'POST':
        form = ProductPurchaseOptionForm(request.POST, instance=option, product_id=product_id)

        if form.is_valid():
            form.save()
            return redirect('product-update', pk=product_id)
    else:
        form = ProductPurchaseOptionForm(instance=option, product_id=product_id)

    context = {'option_form': form}
    return render(request, 'product-purchase-option/update.html', context)


@login_required
def purchase_option_delete(request, pk, product_id=None):
    option = get_object_or_404(ProductPurchaseOption, pk=pk)

    if not product_id:
        product_id = option.product.id
        return redirect('product-purchase-option-delete', pk=pk, product_id=product_id)

    if request.method == 'POST':
        option.delete()
        return redirect('product-update', pk=product_id)

    context = {'option': option}
    return render(request, 'product-purchase-option/delete.html', context)
