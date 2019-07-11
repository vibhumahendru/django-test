from django.shortcuts import render
from .models import Product
from .forms import ProductForm
from django.core import serializers
from django.http import HttpResponse

# Create your views here.


def product_create_view(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = ProductForm()
        print("YO YO YO")
    context = {
        "form":form
    }

    return render(request, 'products/product_create.html',context)




def product_detail_view(request):
    obj = Product.objects.get(id=1)
    products = Product.objects.all()
    data = serializers.serialize('json', products)
    print(products)
    context = {
        "object":obj
    }


    # return HttpResponse(data, content_type='application/json')
    return render(request, 'products/product_detail.html',context)











    ##
