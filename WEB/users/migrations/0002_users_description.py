# Generated by Django 5.0.6 on 2024-06-17 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
