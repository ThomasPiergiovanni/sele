# Generated by Django 4.0 on 2022-03-28 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proposition', '0014_remove_proposition_creator_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proposition',
            name='creator_type',
        ),
        migrations.AddField(
            model_name='proposition',
            name='proposition_creator_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='proposition_creator_type', to='proposition.creatortype'),
            preserve_default=False,
        ),
    ]