# Generated by Django 3.2.9 on 2022-01-18 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0010_fsmtemplate_required'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fsmtemplate',
            name='required',
        ),
    ]
