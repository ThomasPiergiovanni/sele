# Generated by Django 4.0 on 2022-01-29 12:08

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('collectivity', '0002_postalcode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postalcode',
            name='insee_code',
        ),
        migrations.AddField(
            model_name='postalcode',
            name='collectivity',
            field=models.ForeignKey(default=99999, on_delete=django.db.models.deletion.CASCADE, to='collectivity.collectivity'),
            preserve_default=False,
        ),
    ]
