# Generated by Django 4.2.5 on 2023-11-03 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watersystemapp', '0011_alter_address_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='order',
        ),
    ]
