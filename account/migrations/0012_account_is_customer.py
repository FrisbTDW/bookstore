# Generated by Django 3.0.4 on 2020-03-30 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_auto_20200329_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_customer',
            field=models.BooleanField(default=True),
        ),
    ]
