from django.urls import path
from .views import RecentProductView, ProductDetailView

urlpatterns = [
    path('recentproducts/', RecentProductView.as_view(), name='recent_products'),
    path('product-detail/', ProductDetailView.as_view(), name='product-detail')
]
