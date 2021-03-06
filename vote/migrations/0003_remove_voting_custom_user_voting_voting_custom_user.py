# Generated by Django 4.0 on 2022-03-17 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_alter_customuser_collectivity'),
        ('vote', '0002_remove_voting_relation_vote_voting_votes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voting',
            name='custom_user',
        ),
        migrations.AddField(
            model_name='voting',
            name='voting_custom_user',
            field=models.ForeignKey(default=7, on_delete=django.db.models.deletion.CASCADE, related_name='voting_custom_user', to='authentication.customuser'),
            preserve_default=False,
        ),
    ]
