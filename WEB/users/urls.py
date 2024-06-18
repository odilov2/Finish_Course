from django.urls import path
from .views import LogOutView, UsersView, UserRegisterView, UserLoginView


urlpatterns = [
    path('', UsersView.as_view(), name='users'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout')
]