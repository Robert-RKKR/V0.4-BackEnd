# Generated by Django 3.2.9 on 2022-01-14 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0002_auto_20220114_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loggerdata',
            name='task_id',
            field=models.CharField(max_length=128, null=True),
        ),
    ]