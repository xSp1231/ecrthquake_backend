# Generated by Django 3.2 on 2023-06-02 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamanage', '0002_alter_province_eqnum_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Province_intro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(max_length=10, verbose_name='省份')),
                ('deathnum', models.IntegerField(verbose_name='受伤人数')),
                ('injurenum', models.IntegerField(verbose_name='死亡人数')),
                ('total', models.IntegerField(verbose_name='伤亡人数')),
                ('intro', models.CharField(max_length=100, verbose_name='省份地理简介')),
                ('pie_json', models.CharField(max_length=600, verbose_name='饼图数据')),
            ],
            options={
                'db_table': 'province_intro',
            },
        ),
    ]
