# Generated by Django 4.1.6 on 2023-02-23 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('argaping', '0010_ciudad_remove_filtro_nombre_filtro_tipo_operacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='barrio',
            name='ciudad',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='argaping.ciudad'),
            preserve_default=False,
        ),
    ]
