# Generated by Django 3.2 on 2023-05-29 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Province_eqnum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(max_length=10, verbose_name='省份')),
                ('num2013', models.IntegerField(verbose_name='2013')),
                ('num2014', models.IntegerField(verbose_name='2014')),
                ('num2015', models.IntegerField(verbose_name='2015')),
                ('num2016', models.IntegerField(verbose_name='2016')),
                ('num2017', models.IntegerField(verbose_name='2017')),
                ('num2018', models.IntegerField(verbose_name='2018')),
                ('num2019', models.IntegerField(verbose_name='2019')),
                ('num2020', models.IntegerField(verbose_name='2020')),
                ('num2021', models.IntegerField(verbose_name='2021')),
                ('num2022', models.IntegerField(verbose_name='2022')),
            ],
        ),
    ]
