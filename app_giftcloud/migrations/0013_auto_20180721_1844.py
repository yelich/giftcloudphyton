# Generated by Django 2.0.6 on 2018-07-21 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_giftcloud', '0012_auto_20180721_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gift',
            name='privacy',
            field=models.CharField(choices=[('Public', 'Public'), ('Private', 'Private')], default='Public', max_length=8),
        ),
    ]
