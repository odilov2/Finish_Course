# Generated by Django 5.0.6 on 2024-06-17 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_users_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'users_product',
            },
        ),
        migrations.AddField(
            model_name='users',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='users/users/'),
        ),
    ]
