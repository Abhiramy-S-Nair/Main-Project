# Generated by Django 4.2.5 on 2024-02-22 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watersystemapp', '0060_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendorproduct',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='watersystemapp.category'),
        ),
    ]
