# Generated by Django 3.1.1 on 2020-10-18 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodschannel',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='channels', to='goods.goodscategory', verbose_name='顶级商品类别'),
        ),
        migrations.AlterField(
            model_name='sku',
            name='spu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skus', to='goods.spu', verbose_name='商品'),
        ),
        migrations.CreateModel(
            name='GoodsVisitCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('count', models.IntegerField(default=0, verbose_name='访问量')),
                ('date', models.DateField(auto_now_add=True, verbose_name='统计日期')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.goodscategory', verbose_name='商品分类')),
            ],
            options={
                'verbose_name': '统计分类商品访问量',
                'verbose_name_plural': '统计分类商品访问量',
                'db_table': 'tb_goods_visit',
            },
        ),
    ]
