# Generated by Django 3.2 on 2023-06-13 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamanage', '0005_alter_province_intro_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='province_intro',
            name='image',
            field=models.ImageField(default='pictures/default.jpg', upload_to='pictures/'),
        ),
    ]