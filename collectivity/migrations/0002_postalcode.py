# Generated by Django 4.0 on 2022-01-25 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collectivity', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostalCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postal_code', models.CharField(max_length=5)),
                ('insee_code', models.CharField(max_length=5)),
            ],
        ),
    ]
