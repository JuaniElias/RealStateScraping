# Generated by Django 4.1.3 on 2022-11-29 02:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barrio',
            fields=[
                ('id_barrio', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Filtro',
            fields=[
                ('id_filtro', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Propiedad',
            fields=[
                ('id_prop', models.IntegerField(primary_key=True, serialize=False)),
                ('precio', models.IntegerField()),
                ('calle', models.CharField(max_length=250)),
                ('nro', models.CharField(max_length=6)),
                ('barrio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='argaping.barrio')),
            ],
        ),
    ]
