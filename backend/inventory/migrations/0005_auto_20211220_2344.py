# Generated by Django 3.2.9 on 2021-12-20 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20211220_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='device',
            name='https_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='device',
            name='root',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='device',
            name='ssh_status',
            field=models.BooleanField(default=False),
        ),
    ]
