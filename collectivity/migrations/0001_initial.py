# Generated by Django 4.0 on 2022-01-08 12:11

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collectivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Nom')),
                ('insee_code', models.CharField(max_length=5, verbose_name='Code INSEE')),
                ('activity', models.CharField(max_length=3, verbose_name='Groupe actif')),
                ('feat_geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
    ]
