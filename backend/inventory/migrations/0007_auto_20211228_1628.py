# Generated by Django 3.2.9 on 2021-12-28 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_rename_lik_deviceinterface_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deviceinterface',
            name='name',
        ),
        migrations.RemoveField(
            model_name='deviceinterface',
            name='status',
        ),
        migrations.RemoveField(
            model_name='deviceinterface',
            name='type',
        ),
        migrations.RemoveField(
            model_name='deviceinterface',
            name='vlan',
        ),
    ]