from django.contrib.auth.decorators import login_required
from django.contrib import messages
from shop.models import Cart
from django.http.response import HttpResponseRedirect

@login_required(login_url='/login')
def addtocart(request, prid):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    if request.method=='POST':
        pid=request.POST['product']
        uid=request.POST['user']
        qty=request.POST['qty']
        size=request.POST['size']


        # c=Cart(user_id=uid, product_id=pid,qty=qty,size=size)
                # c.save()

        if Cart.objects.filter(user_id=current_user.id, product_id=prid):
            qty = request.POST['qty']
            # size=request.POST['size']
            # data = Cart.objects.filter(user_id=current_user.id, product_id=prid,size=size)
            # data.qty=qty
            # # data.size=size
            # data.save()
            # print('ddd',data)

            data = Cart.objects.filter(user_id=current_user.id, product_id=prid).update(qty=qty,size=size)
            print(True)
        # elif Cart.objects.filter(user_id=current_user.id, product_id=prid):
        #     qty = request.POST['qty']
        #     data = Cart.objects.filter(user_id=current_user.id, product_id=prid).update(qty=qty,size=size)
        #     print(True)

        else:
            data = Cart(user_id=uid, product_id=pid, qty=qty, size=size)
            data.save()
            messages.success(request, data.product.product_name + " added to the Cart.")




    elif Cart.objects.filter(user_id=current_user.id, product_id=prid):
        print('ppppp', True)
        # d1= Cart.objects.get(user_id=current_user.id, product_id=prid)
        # for i in d1:
        #
        #     print(i.size)

        data = Cart.objects.get(user_id=current_user.id, product_id=prid)
        print(data)
        data.qty = data.qty + 1
        print(data.qty)
        data.save()
    else:
        data = Cart(user_id=current_user.id, product_id=prid, qty=1, size='s')
        data.save()
        #
        # if check_product:
        #     control = 1
        # else:
        #     control = 0
        #
        # if control == 1:
    return HttpResponseRedirect(url)

# @login_required(login_url='/login')
# def addtocart(request, prid):
#     url = request.META.get('HTTP_REFERER')
#     current_user = request.user
#     check_product = Cart.objects.filter(user_id=current_user.id, product_id=prid)
#
#     if check_product:
#         control = 1
#     else:
#         control = 0
#
#     if control == 1:
#         data = Cart.objects.get(user_id=current_user.id, product_id=prid)
#         data.qty = data.qty + 1
#         data.save()
#     else:
#         data = Cart()
#         data.user_id = current_user.id
#         data.product_id = prid
#         data.qty = 1
#         data.save()
#     messages.success(request, data.product.product_name + " added to the Cart.")
#     return HttpResponseRedirect(url)

def deletefromcart(request, prid):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    product = Cart.objects.get(user_id=current_user.id, product_id=prid)
        
    if product.qty == 1:
        product.delete()
    else:
        product.qty = product.qty - 1
        product.save()
    
    messages.success(request, product.product.product_name + " deleted from the Cart.")
    return HttpResponseRedirect(url)

def deleteallfromcart(request, prid):
    current_user = request.user
    Cart.objects.get(product_id=prid, user_id=current_user.id).delete()
    return HttpResponseRedirect('/cart')
    
def clearcart(request):
    current_user = request.user
    Cart.objects.filter(user_id=current_user.id).delete()
    return HttpResponseRedirect('/cart')
