# Generated by Django 3.2 on 2021-11-26 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_auto_20211126_0559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='status',
        ),
    ]
