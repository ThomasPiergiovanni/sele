# Generated by Django 4.0 on 2022-01-30 00:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collectivity', '0007_postalcode_collectivity'),
        ('authentication', '0002_alter_customuser_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='balance',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customuser',
            name='collectivity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='collectivity.collectivity'),
        ),
    ]
