# Generated by Django 4.1.6 on 2023-02-10 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('argaping', '0008_rename_precio_propiedad_precio_ars_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propiedad',
            name='precio_ars',
            field=models.DecimalField(decimal_places=2, max_digits=18),
        ),
    ]
