# Generated by Django 3.2 on 2023-06-04 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamanage', '0003_province_intro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='province_intro',
            name='total',
            field=models.IntegerField(default=0, verbose_name='伤亡人数'),
        ),
    ]
