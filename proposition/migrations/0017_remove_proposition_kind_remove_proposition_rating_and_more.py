# Generated by Django 4.0 on 2022-03-28 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_alter_customuser_collectivity'),
        ('proposition', '0016_remove_proposition_domain_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proposition',
            name='kind',
        ),
        migrations.RemoveField(
            model_name='proposition',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='proposition',
            name='status',
        ),
        migrations.RemoveField(
            model_name='proposition',
            name='taker',
        ),
        migrations.AddField(
            model_name='proposition',
            name='proposition_kind',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='proposition_kind', to='proposition.kind'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proposition',
            name='proposition_rating',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='proposition_rating', to='proposition.rating'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proposition',
            name='proposition_status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='proposition_status', to='proposition.status'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proposition',
            name='proposition_taker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proposition_taker', to='authentication.customuser'),
        ),
    ]