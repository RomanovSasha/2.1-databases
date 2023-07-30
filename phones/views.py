from django.shortcuts import render, redirect, get_object_or_404

from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = str(request.GET.get("sort"))
    template = 'catalog.html'
    phones = Phone.objects.all()
    if sort == 'name':
        phones = sorted(Phone.objects.all(), key=lambda x: x.name)
    if sort == 'min_price':
        phones = sorted(Phone.objects.all(), key=lambda x: x.price)
    if sort == 'max_price':
        phones = sorted(Phone.objects.all(), key=lambda x: x.price, reverse=True)
    return render(request, template, {'phones': phones})


def show_product(request, slug):
    context = get_object_or_404(Phone, slug=slug)
    template = 'product.html'
    return render(request, template, {'phone': context})
