from django.shortcuts import render
from django.shortcuts import  render_to_response
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from show.models import Product
def show_products(request):
    return render_to_response('products.html', {'products': Product.objects.all()})
def show_products_laptop(request):
    return render_to_response('products_laptop.html', {'products': Product.objects.all()})
def show_products_dienthoai(request):
    return render_to_response('products_dienthoai.html', {'products': Product.objects.all()})
def show_products_phukien(request):
    return render_to_response('products_phukien.html', {'products': Product.objects.all()})
def show_products_sach(request):
    return render_to_response('products_sach.html', {'products': Product.objects.all()})
def show_products_banghe(request):
    return render_to_response('products_banghe.html', {'products': Product.objects.all()})
def show_products_khac(request):
    return render_to_response('products_khac.html', {'products': Product.objects.all()})
def show_product(request, product_id=1):
    return render_to_response('product-.html', {'product': Product.objects.get(id=product_id)})