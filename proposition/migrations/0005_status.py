# Generated by Django 4.0 on 2022-01-23 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposition', '0004_domain'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, unique=True)),
            ],
        ),
    ]
