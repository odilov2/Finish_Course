from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static


from django.urls import path
from .views import (IndexView, AboutView, BlogView, CheckoutView, ContactView, CartView, ServiceView, ShopView,
                    ThankyouView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('project/', include('project.urls')),
    path('users/', include('users.urls')),
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('blog', BlogView.as_view(), name='blog'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('cart/', CartView.as_view(), name='cart'),
    path('service/', ServiceView.as_view(), name='service'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('thankyou/', ThankyouView.as_view(), name='thankyou')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
