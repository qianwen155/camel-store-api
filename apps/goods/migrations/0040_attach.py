# Generated by Django 2.1.4 on 2019-01-24 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0039_auto_20190116_1116'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=128, verbose_name='字段名')),
                ('attach_type', models.CharField(max_length=128, verbose_name='类型')),
                ('length', models.PositiveSmallIntegerField(null=True, verbose_name='限定长度')),
                ('max_value', models.FloatField(null=True, verbose_name='最大值')),
                ('min_value', models.FloatField(null=True, verbose_name='最小值')),
            ],
            options={
                'verbose_name': '商品自定义字段',
                'verbose_name_plural': '商品自定义字段',
            },
        ),
    ]
