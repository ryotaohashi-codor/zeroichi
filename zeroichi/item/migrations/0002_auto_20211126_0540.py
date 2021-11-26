# Generated by Django 3.2 on 2021-11-26 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='status',
        ),
        migrations.AddField(
            model_name='itemcheck',
            name='status',
            field=models.IntegerField(choices=[(0, '申請中'), (1, '承認'), (2, '却下')], default=0),
        ),
    ]