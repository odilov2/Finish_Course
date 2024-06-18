from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    image = models.ImageField(upload_to='users/users/', null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    description = models.TextField(null=True)

    class Meta:
        db_table = 'users'


class Users_Product(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = 'users_product'


class Teams(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    image = models.ImageField(upload_to='teams/users/')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)

    class Meta:
        db_table = 'teams'


class Category(models.Model):
    name = models.CharField(max_length=50)


class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    description = models.TextField()
    count = models.PositiveIntegerField(null=True)
    image = models.ImageField(upload_to='product/product/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'product'

class RecentProduct(models.Model):
    description = models.TextField()
    count = models.PositiveIntegerField(null=True)
    image = models.ImageField(upload_to='recent_product/recent_product/')
    create_date = models.DateField(auto_now_add=True)
    # user = models.ForeignKey(Users_Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'recentorder'


class Order(models.Model):
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'order'