# Generated by Django 2.0.6 on 2018-07-21 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_giftcloud', '0009_auto_20180720_1136'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gift',
            old_name='gift_choices',
            new_name='privacy',
        ),
    ]
