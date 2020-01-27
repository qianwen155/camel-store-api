# Generated by Django 2.2.1 on 2019-06-19 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_migrate_old_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrcode',
            name='device',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='devices', to='shop.Printer', verbose_name='设备'),
        ),
    ]
