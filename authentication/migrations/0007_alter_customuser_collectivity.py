# Generated by Django 4.0 on 2022-02-20 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collectivity', '0011_alter_collectivity_postal_code'),
        ('authentication', '0006_alter_customuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='collectivity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='collectivity.collectivity'),
        ),
    ]
