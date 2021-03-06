# Generated by Django 4.0 on 2022-04-14 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0008_discussiontype_discussion_discussion_discussion_type'),
        ('proposition', '0025_proposition_creator_not_taker'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposition',
            name='proposition_discussion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proposition_discussion', to='chat.discussion'),
        ),
    ]
