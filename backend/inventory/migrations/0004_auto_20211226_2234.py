# Generated by Django 3.2.9 on 2021-12-26 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_alter_devicerawdata_command_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deviceinterface',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.device'),
        ),
        migrations.AlterUniqueTogether(
            name='deviceinterface',
            unique_together={('device', 'port')},
        ),
    ]