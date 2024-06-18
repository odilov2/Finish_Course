from django.contrib import admin
from .models import Product, Users, Users_Product, RecentProduct, Order
from users.models import Teams
from import_export.admin import ImportExportModelAdmin


@admin.register(Product)
class ProductsAdmin(ImportExportModelAdmin):
    list_display = ['id', 'name', 'price', 'description']
    list_display_links = ['name']
    search_fields = ['name', 'price']
    ordering = ['id']


# @admin.register(Users)
# class UsersAdmin(ImportExportModelAdmin):
#     list_display = ['id']
#     list_display_links = ['first_name']
#     search_fields = ['username']
#     ordering = ['id']


# @admin.register(Users_Product)
# class Users_ProductAdmin(ImportExportModelAdmin):
#     list_display = ['id']
#     list_display_links = ['first_name']
#     search_fields = ['last_name']
#     ordering = ['id']


# @admin.register(RecentProduct)
# class RecentProductAdmin(ImportExportModelAdmin):
#     list_display = ['id']
#     list_display_links = ['description']
#     search_fields = ['price']
#     ordering = ['id']


@admin.register(Teams)
class TeamsAdmin(ImportExportModelAdmin):
    list_display = ['id', 'first_name']
    list_display_links = ['first_name']
    search_fields = ['last_name']
    ordering = ['id']


# @admin.register(Order)
# class OrderAdmin(ImportExportModelAdmin):
#     list_display = ['id']
#     list_display_links = ['product_id']
#     search_fields = ['id']
#     ordering = ['id']