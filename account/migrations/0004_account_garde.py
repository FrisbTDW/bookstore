# Generated by Django 3.0.4 on 2020-03-29 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20200329_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='garde',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')], default='12', max_length=100),
        ),
    ]
