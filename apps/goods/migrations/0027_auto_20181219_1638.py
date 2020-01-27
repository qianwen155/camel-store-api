# Generated by Django 2.1.4 on 2018-12-19 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qfile', '0001_initial'),
        ('shop', '0003_shop_status'),
        ('goods', '0026_banner_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='商品名', max_length=100, verbose_name='商品名')),
                ('goods_brief', models.TextField(max_length=256, verbose_name='商品简短描述')),
                ('status', models.IntegerField(choices=[(0, '在售'), (1, '预览'), (2, '下架')], default=0, verbose_name='商品状态')),
                ('index', models.IntegerField(default=0, verbose_name='优先级')),
                ('duration', models.CharField(choices=[('long_term', '长期'), ('time_frame', '时间范围')], max_length=128, verbose_name='持续时间设置')),
                ('duration_start', models.DateField(blank=True, null=True, verbose_name='持续时间起始时间')),
                ('duration_end', models.DateField(blank=True, null=True, verbose_name='持续时间终止时间')),
                ('delivery_setup', models.CharField(choices=[('date', '配送日期'), ('interval', '固定间隔')], default='interval', max_length=128, verbose_name='配送设置')),
                ('date_setup', models.CharField(blank=True, choices=[('specific', '具体日期'), ('weekly', '每周')], max_length=128, null=True, verbose_name='配送时间设置')),
                ('delivery_data', models.TextField(blank=True, null=True, verbose_name='配送日期')),
                ('interval', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='固定间隔')),
                ('send_start', models.TimeField(blank=True, null=True, verbose_name='配送日开始配送时间')),
                ('send_end', models.TimeField(blank=True, null=True, verbose_name='配送日结束配送时间')),
                ('delivery_method', models.CharField(choices=[('own', '自配送'), ('express', '快递')], max_length=128, verbose_name='配送方式')),
                ('pick_up', models.BooleanField(default=False, verbose_name='是否允许自提')),
                ('postage_setup', models.CharField(choices=[('free', '免邮'), ('distance', '按距离计算')], max_length=128, verbose_name='运费设置')),
                ('postage', models.TextField(blank=True, null=True, verbose_name='运费')),
            ],
            options={
                'verbose_name': '订阅商品',
                'verbose_name_plural': '订阅商品',
                'ordering': ('status', 'index'),
            },
        ),
        migrations.CreateModel(
            name='SubGoodsImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.PositiveSmallIntegerField(default=0, verbose_name='顺序')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='qfile.File', verbose_name='图片')),
            ],
            options={
                'verbose_name': '订阅商品图片',
                'verbose_name_plural': '订阅商品图片',
                'ordering': ('index',),
            },
        ),
        migrations.CreateModel(
            name='SubGoodsTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='商品名', max_length=100, verbose_name='商品名')),
                ('goods_brief', models.TextField(max_length=256, verbose_name='商品简短描述')),
                ('status', models.IntegerField(choices=[(0, '在售'), (1, '预览'), (2, '下架')], default=0, verbose_name='商品状态')),
                ('index', models.IntegerField(default=0, verbose_name='优先级')),
                ('duration', models.CharField(choices=[('long_term', '长期'), ('time_frame', '时间范围')], max_length=128, verbose_name='持续时间设置')),
                ('duration_start', models.DateField(blank=True, null=True, verbose_name='持续时间起始时间')),
                ('duration_end', models.DateField(blank=True, null=True, verbose_name='持续时间终止时间')),
                ('delivery_setup', models.CharField(choices=[('date', '配送日期'), ('interval', '固定间隔')], default='interval', max_length=128, verbose_name='配送设置')),
                ('date_setup', models.CharField(blank=True, choices=[('specific', '具体日期'), ('weekly', '每周')], max_length=128, null=True, verbose_name='配送时间设置')),
                ('delivery_data', models.TextField(blank=True, null=True, verbose_name='配送日期')),
                ('interval', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='固定间隔')),
                ('send_start', models.TimeField(blank=True, null=True, verbose_name='配送日开始配送时间')),
                ('send_end', models.TimeField(blank=True, null=True, verbose_name='配送日结束配送时间')),
                ('delivery_method', models.CharField(choices=[('own', '自配送'), ('express', '快递')], max_length=128, verbose_name='配送方式')),
                ('pick_up', models.BooleanField(default=False, verbose_name='是否允许自提')),
                ('postage_setup', models.CharField(choices=[('free', '免邮'), ('distance', '按距离计算')], max_length=128, verbose_name='运费设置')),
                ('postage', models.TextField(blank=True, null=True, verbose_name='运费')),
                ('banners', models.ManyToManyField(related_name='template_banners', to='goods.SubGoodsImage', verbose_name='详情页轮播图')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='goods.GoodsCategory', verbose_name='商品类别')),
                ('details', models.ManyToManyField(related_name='template_details', to='goods.SubGoodsImage', verbose_name='商品详情图')),
            ],
            options={
                'verbose_name': '订阅商品模板',
                'verbose_name_plural': '订阅商品模板',
            },
        ),
        migrations.CreateModel(
            name='SubGoodsType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(help_text='规格', max_length=100, verbose_name='规格')),
                ('market_price', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='市场价格')),
                ('price', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='价格')),
                ('stock', models.PositiveIntegerField(default=10, verbose_name='库存')),
                ('is_sell', models.BooleanField(default=True, verbose_name='是否在售')),
                ('index', models.PositiveSmallIntegerField(default=0, verbose_name='优先级')),
                ('cycle_num', models.PositiveSmallIntegerField(verbose_name='订阅期数')),
            ],
            options={
                'verbose_name': '订阅商品规格',
                'verbose_name_plural': '订阅商品规格',
                'ordering': ('-is_sell', 'index'),
            },
        ),
        migrations.AddField(
            model_name='subgoodstemplate',
            name='gtype',
            field=models.ManyToManyField(to='goods.SubGoodsType', verbose_name='订阅商品规格'),
        ),
        migrations.AddField(
            model_name='subgoodstemplate',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='qfile.File', verbose_name='封面图'),
        ),
        migrations.AddField(
            model_name='subgoodstemplate',
            name='shop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.Shop', verbose_name='所属店铺'),
        ),
        migrations.AddField(
            model_name='subgoods',
            name='banners',
            field=models.ManyToManyField(related_name='subgoods_banners', to='goods.SubGoodsImage', verbose_name='详情页轮播图'),
        ),
        migrations.AddField(
            model_name='subgoods',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='goods.GoodsCategory', verbose_name='商品类别'),
        ),
        migrations.AddField(
            model_name='subgoods',
            name='details',
            field=models.ManyToManyField(related_name='subgoods_details', to='goods.SubGoodsImage', verbose_name='商品详情图'),
        ),
        migrations.AddField(
            model_name='subgoods',
            name='gtype',
            field=models.ManyToManyField(to='goods.SubGoodsType', verbose_name='订阅商品规格'),
        ),
        migrations.AddField(
            model_name='subgoods',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='qfile.File', verbose_name='封面图'),
        ),
        migrations.AddField(
            model_name='subgoods',
            name='shop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.Shop', verbose_name='所属店铺'),
        ),
    ]
