# Generated by Django 3.0.8 on 2020-09-10 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_auto_20200901_1619"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="description",
        ),
    ]
