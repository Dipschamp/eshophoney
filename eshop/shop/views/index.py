from django.views import View
from django.shortcuts import render
from shop.models import Category, Customer, Product, Cart

def index(request):
    current_user = request.user
    products = Product.objects.all()
    mobiles = Product.objects.filter(category_id=1)
    laptops = Product.objects.filter(category_id=2)
    tvs = Product.objects.filter(category_id=3)
    headphones = Product.objects.filter(category_id=6)
    homeapps = Product.objects.filter(category_id=9)
    kitapps = Product.objects.filter(category_id=8)
    categories = Category.objects.all()


    pro=[Product.objects.filter(category_id=i.id)[:4] for i in categories]
    print(pro)
    for i in pro:
        print(i)



    carts = Cart.objects.filter(user_id=current_user.id)

    customer = []
    try:
        customer = Customer.objects.get(user_id=current_user.id)
    except:
        pass
    
    qty = 0
    total = 0
    for cart in carts:
        total = total + cart.amount
        qty = qty + cart.qty
    
    params = {
        'customer':customer,
        'products': products,
        'mobiles': mobiles,
        'laptops': laptops,
        'tvs': tvs,
        'headphones': headphones,
        'homeapps': homeapps,
        'kitapps': kitapps,
        'categories':categories,
        'qty':qty,
        'total':total,
        'carts':carts,
        'pro':pro


    }

    return render(request, 'index.html', params)