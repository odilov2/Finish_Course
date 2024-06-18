from django.shortcuts import render
from project.models import Product
from django.views import View

from users.models import Teams


class IndexView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'register.html', {'products': products})


class BlogView(View):
    def get(self, request):
        return render(request, 'blog.html')


class CartView(View):
    def get(self, request):
        return render(request, 'cart.html')


class CheckoutView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'checkout.html')


class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')


class ServiceView(View):
    def get(self, request):
        return render(request, 'services.html')


class ShopView(View):
    def get(self, request):
        return render(request, 'shop.html')


class ThankyouView(View):
    def get(self, request):
        return render(request, 'thankyou.html')


class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')




