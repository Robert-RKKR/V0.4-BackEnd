# Generated by Django 3.2.9 on 2021-12-28 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_auto_20211228_1621'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deviceinterface',
            old_name='lik',
            new_name='name',
        ),
    ]
