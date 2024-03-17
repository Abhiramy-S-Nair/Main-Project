# Generated by Django 4.2.5 on 2024-03-16 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watersystemapp', '0076_deliveryboys'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deliveryboys',
            name='gst_number',
        ),
        migrations.RemoveField(
            model_name='deliveryboys',
            name='phone_number',
        ),
        migrations.AlterField(
            model_name='deliveryboys',
            name='driving_license',
            field=models.ImageField(upload_to='driving_licenses'),
        ),
        migrations.AlterField(
            model_name='deliveryboys',
            name='identity_proof',
            field=models.ImageField(upload_to='identity_proofs'),
        ),
        migrations.AlterField(
            model_name='deliveryboys',
            name='profile_photo',
            field=models.ImageField(upload_to='profile_photos'),
        ),
    ]