# Generated by Django 4.1.5 on 2023-02-04 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('argaping', '0006_alter_propiedad_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='propiedad',
            name='tipo_operacion',
            field=models.CharField(default='alquiler', max_length=15),
            preserve_default=False,
        ),
    ]
