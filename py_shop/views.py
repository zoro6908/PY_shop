from django.shortcuts import render
from django.http import HttpResponse
# from .models import Product
import products.templates


def home(request):
    # products = Product.objects.all()
    return render(request, 'index.html') #, {'products': products})