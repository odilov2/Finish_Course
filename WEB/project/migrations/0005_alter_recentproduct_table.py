# Generated by Django 5.0.6 on 2024-06-17 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_recentproduct'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='recentproduct',
            table='recentorder',
        ),
    ]
