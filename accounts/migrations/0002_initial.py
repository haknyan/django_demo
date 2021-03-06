# Generated by Django 3.2.8 on 2021-10-28 02:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('shopping', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('local_shops', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='visited',
            name='shop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shopping.shop'),
        ),
        migrations.AddField(
            model_name='visited',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='info',
            name='area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='local_shops.area'),
        ),
        migrations.AddField(
            model_name='info',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
