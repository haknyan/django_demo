# Generated by Django 3.2.8 on 2021-10-27 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchases',
            name='status',
            field=models.CharField(max_length=32, null=True),
        ),
    ]