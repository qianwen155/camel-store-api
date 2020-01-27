# Generated by Django 2.1.7 on 2019-03-26 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('count', '0007_wxuserstatistics_user_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderstatistics',
            name='qrpay_num',
            field=models.PositiveIntegerField(default=0, verbose_name='扫码支付订单数量'),
        ),
        migrations.AddField(
            model_name='turnoversstatistics',
            name='qrpay_turnovers',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='扫码支付订单总销售额'),
        ),
        migrations.AlterField(
            model_name='turnoversstatistics',
            name='sub_turnovers',
            field=models.DecimalField(decimal_places=2, max_digits=15, verbose_name='订阅订单总销售额'),
        ),
    ]
