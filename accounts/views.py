from django.shortcuts import render
from django.http import HttpResponse
# from .models import Product
import products.templates
from django.contrib.auth.models import User
from django.contrib import auth
import py_shop.views

# /products -> index function
# Uniform Resource Locator (Address)
# 화면에 뿌려 지는 내용 정의
#
# product의 메인 화면
def signup(request):
    # products = Product.objects.all()
    return render(request, 'signup.html')


def login(request):
    # products = Product.objects.all()
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return render(request, py_shop.views.home)
