# Generated by Django 4.0 on 2022-03-29 11:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposition', '0017_remove_proposition_kind_remove_proposition_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposition',
            name='duration',
            field=models.PositiveIntegerField(default=60, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
