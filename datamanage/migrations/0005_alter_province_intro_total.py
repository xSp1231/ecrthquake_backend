# Generated by Django 3.2 on 2023-06-04 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamanage', '0004_alter_province_intro_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='province_intro',
            name='total',
            field=models.IntegerField(null=True, verbose_name='伤亡人数'),
        ),
    ]
