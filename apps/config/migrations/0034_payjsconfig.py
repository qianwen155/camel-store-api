# Generated by Django 2.1.8 on 2019-10-14 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0033_invoice_switch'),
    ]

    operations = [
        migrations.CreateModel(
            name='PayJSConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='配置项')),
                ('content', models.CharField(default='', max_length=100, verbose_name='配置内容')),
            ],
            options={
                'verbose_name': 'PAYJS配置',
                'verbose_name_plural': 'PAYJS配置',
            },
        ),
    ]
