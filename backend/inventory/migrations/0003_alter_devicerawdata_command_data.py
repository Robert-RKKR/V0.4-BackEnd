# Generated by Django 3.2.9 on 2021-12-26 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20211224_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devicerawdata',
            name='command_data',
            field=models.TextField(blank=True, null=True),
        ),
    ]