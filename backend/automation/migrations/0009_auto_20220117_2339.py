# Generated by Django 3.2.9 on 2022-01-17 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0008_auto_20220117_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='policymanager',
            name='result',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='policymanager',
            name='tasks_ids',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
