# Generated by Django 2.1.2 on 2018-10-25 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0005_remove_faqcontent_icon'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='faqcontent',
            options={'ordering': ('index', '-add_time'), 'verbose_name': '客服FAQ内容', 'verbose_name_plural': '客服FAQ内容'},
        ),
        migrations.AddField(
            model_name='faqcontent',
            name='index',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='排序'),
        ),
    ]
