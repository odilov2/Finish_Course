from django.db import models
from users.models import Users_Product, Users


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