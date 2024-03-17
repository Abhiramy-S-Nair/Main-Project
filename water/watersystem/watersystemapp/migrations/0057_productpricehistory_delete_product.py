# Generated by Django 4.2.5 on 2024-02-18 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watersystemapp', '0056_delete_vendorbio'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductPriceHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('offer', models.DecimalField(decimal_places=2, max_digits=5)),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watersystemapp.vendorproduct')),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]