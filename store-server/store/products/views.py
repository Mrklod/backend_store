from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from products.models import ProductCategory,Product,Basket
# Create your views here.
# контролеры = views = функции

def index(request):
    context = {
        'title':'Geekshop'
    }
    return render(request, "products/index.html",context)

def products(request):
    context = {
        'title':'Catalog',
        'categories': ProductCategory.objects.all(),
        'products':Product.objects.all()
    }
    return render(request, "products/products.html",context)
@login_required
def basket_add(request,product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user,product=product)

    if not baskets.exists():
        basket = Basket(user=request.user,product=product,quantity=1)
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        bakset = baskets.first()
        bakset.quantity += 1
        bakset.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
@login_required
def basket_delete(request,id):
    basket = Basket.objects.get(id=id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

