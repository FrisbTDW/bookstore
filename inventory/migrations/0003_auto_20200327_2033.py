# Generated by Django 3.0.4 on 2020-03-27 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20200327_2025'),
    ]

    operations = [
        migrations.RenameField(
            model_name='log',
            old_name='book',
            new_name='book_name',
        ),
    ]