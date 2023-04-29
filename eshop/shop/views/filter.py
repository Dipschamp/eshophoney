from django.shortcuts import render

from shop.models import Product


def filter(request):

    if 'min_price' in request.GET:
        filter_price1 = request.GET.get('min_price')
        filter_price2 = request.GET.get('max_price')
        if filter_price1 == '':
            filter_price1 = 0

        products= Product.objects.filter(price__range=(filter_price1, filter_price2))
    else:
        products=Product.objects.all()


    return render(request,'products.html',{'products':products})