# Generated by Django 2.0.6 on 2018-07-21 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_giftcloud', '0010_auto_20180721_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gift',
            name='privacy',
            field=models.CharField(choices=[('PB', 'Public'), ('PI', 'Private')], default='PB', max_length=6),
        ),
    ]
