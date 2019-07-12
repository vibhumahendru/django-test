from django.shortcuts import render
from .models import Product
from .forms import ProductForm, RawProductForm
from django.core import serializers
from django.http import HttpResponse

# Create your views here.


# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#
#     if form.is_valid():
#         form.save()
#         form = ProductForm()
#         print("YO YO YO")
#     context = {
#         "form":form
#     }
#
#     return render(request, 'products/product_create.html',context)

# def product_create_view(request):
#     # print("in GET", request.GET)
#     # print("in post", request.POST['title'])
#     print("THIS IS A TEST PRINT")
#     print(request)
#     my_title = request.POST.get('title')
#     print(my_title)
#     # Product.objects.create(title=my_title)
#     context = {
#
#     }
#
#     return render(request, 'products/product_create.html',context)

def product_create_view(request):

    my_form = RawProductForm()
    if request.method == "POST":
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Product.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)

    context = {
        "form":my_form
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
