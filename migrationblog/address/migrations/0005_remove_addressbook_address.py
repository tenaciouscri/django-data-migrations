# Generated by Django 4.0.2 on 2022-02-02 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0004_address_to_postcode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addressbook',
            name='address',
        ),
    ]
