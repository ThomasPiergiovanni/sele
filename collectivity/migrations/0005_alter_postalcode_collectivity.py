# Generated by Django 4.0 on 2022-01-29 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collectivity', '0004_alter_postalcode_collectivity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postalcode',
            name='collectivity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collectivity.collectivity'),
        ),
    ]