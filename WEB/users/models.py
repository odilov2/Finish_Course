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


class TelegramUser(models.Model):
    username = models.CharField(max_length=50)
    full_name = models.CharField(max_length=50)
    chat_id = models.CharField(max_length=50)
    create_date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'telegram_users'
