# Generated by Django 2.1.2 on 2018-11-05 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0020_auto_20181102_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodtype',
            name='bonus',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='分销金额'),
        ),
        migrations.AddField(
            model_name='goodtype',
            name='rebate',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='返利金额'),
        ),
    ]
