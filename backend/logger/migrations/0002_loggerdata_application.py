# Generated by Django 3.2.9 on 2021-12-30 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='loggerdata',
            name='application',
            field=models.CharField(default='Old', max_length=128),
            preserve_default=False,
        ),
    ]