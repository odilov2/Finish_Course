# Generated by Django 5.0.6 on 2024-06-18 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_users_image_alter_teams_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='teams',
            name='position',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
