# Generated by Django 2.1.4 on 2019-01-04 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0031_auto_20181223_2001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subgoodstemplate',
            name='banners',
        ),
        migrations.RemoveField(
            model_name='subgoodstemplate',
            name='category',
        ),
        migrations.RemoveField(
            model_name='subgoodstemplate',
            name='details',
        ),
        migrations.RemoveField(
            model_name='subgoodstemplate',
            name='gtypes',
        ),
        migrations.RemoveField(
            model_name='subgoodstemplate',
            name='image',
        ),
        migrations.RemoveField(
            model_name='subgoodstemplate',
            name='poster',
        ),
        migrations.RemoveField(
            model_name='subgoodstemplate',
            name='shop',
        ),
        migrations.DeleteModel(
            name='SubGoodsTemplate',
        ),
    ]
