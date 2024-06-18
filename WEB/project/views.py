from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .models import RecentProduct, Product
from django.views import View


class RecentProductView(View):
    def get(self, request):
        products = RecentProduct.objects.all()
        return render(request, 'register.html', {'recent_products': products})


class ProductDetailView(View):
    def get(self, request, id):
        products = Product.objects.get(id=id)
        return render(request, "products/products_detail.html", context={"products": products})


class ProductListView(LoginRequiredMixin, View):
    def get(self, request, id):
        products = Product.objects.get(id=id)
        search = request.GET.get('search')
        if search is None:
            products = Product.objects.all()
            context = {'products': products}
            return render(request, 'register.html', context)
        else:
            products = Product.objects.filter(title__icontains=search)
            context = {'products': products}
            return render(request, 'register.html', context)


class ServiceView(LoginRequiredMixin, View):
    def get(self, request):
        products = Product.objects.all()
        blogs = Blog.objects.all()
        context = {
            'products': products,
            'blogs': blogs
        }
        return render(request, 'services.html', context)