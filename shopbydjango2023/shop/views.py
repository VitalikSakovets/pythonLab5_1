from django.shortcuts import render

# Create your views here.

from django.core.paginator import Paginator
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
# Create your views here.
from .models import Category,Product
def about_shop(request):
    return HttpResponse("Page about ComputerShop")
# def product_list(request,category_slug=None):
#     category=None
#     categories=Category.objects.all()
#     products=Product.objects.filter(available=True)
# if category_slug:
# category=get_object_or_404(Category,slug=category_slug)
# products=products.filter(category=category)
# return render(request,'shop/product/list.html',{
# 'category':category,
# 'categories':categories,
# 'products':products,
# })
# def product_detail(request,id):
# product = get_object_or_404(Product, id=id)
# return render(request, 'shop/product/detail.html',{'product': product}))

def contacts(request):
    return HttpResponse("Contacts ComputerShop")