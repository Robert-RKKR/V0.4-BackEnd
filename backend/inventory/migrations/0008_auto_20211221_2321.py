# Generated by Django 3.2.9 on 2021-12-21 22:21

from django.db import migrations, models
import inventory.validators


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_auto_20211221_2259'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='color',
            options={},
        ),
        migrations.AlterModelOptions(
            name='credential',
            options={},
        ),
        migrations.AlterModelOptions(
            name='device',
            options={},
        ),
        migrations.AlterModelOptions(
            name='group',
            options={},
        ),
        migrations.AlterField(
            model_name='color',
            name='description',
            field=models.CharField(default='Credentials description.', error_messages={'invalid': 'Enter the correct description value. It must contain 8 to 256 digits, letters and special characters -, _, . or spaces.'}, max_length=256, validators=[inventory.validators.DescriptionValueValidator()]),
        ),
        migrations.AlterField(
            model_name='color',
            name='hexadecimal',
            field=models.CharField(error_messages={'blank': 'Colour field is mandatory.', 'invalid': 'Enter the correct colour value. It must be a 3/6 hexadecimal number with # character on begining.', 'null': 'Colour field is mandatory.'}, max_length=7, unique=True, validators=[inventory.validators.ColorValueValidator()]),
        ),
        migrations.AlterField(
            model_name='color',
            name='name',
            field=models.CharField(error_messages={'blank': 'Name field is mandatory.', 'invalid': 'Enter the correct name value. It must contain 8 to 32 digits, letters and special characters -, _ or spaces.', 'null': 'Name field is mandatory.'}, max_length=32, unique=True, validators=[inventory.validators.NameValueValidator()]),
        ),
        migrations.AlterField(
            model_name='credential',
            name='description',
            field=models.CharField(default='Credentials description.', error_messages={'invalid': 'Enter the correct description value. It must contain 8 to 256 digits, letters and special characters -, _, . or spaces.'}, max_length=256, validators=[inventory.validators.DescriptionValueValidator()]),
        ),
        migrations.AlterField(
            model_name='credential',
            name='name',
            field=models.CharField(error_messages={'blank': 'Name field is mandatory.', 'invalid': 'Enter the correct name value. It must contain 8 to 32 digits, letters and special characters -, _ or spaces.', 'null': 'Name field is mandatory.'}, max_length=32, unique=True, validators=[inventory.validators.NameValueValidator()]),
        ),
        migrations.AlterField(
            model_name='credential',
            name='password',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='credential',
            name='username',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='device',
            name='certificate',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='device',
            name='description',
            field=models.CharField(default='Device description.', error_messages={'invalid': 'Enter the correct description value. It must contain 8 to 256 digits, letters and special characters -, _, . or spaces.'}, max_length=256, validators=[inventory.validators.DescriptionValueValidator()]),
        ),
        migrations.AlterField(
            model_name='device',
            name='device_type',
            field=models.IntegerField(choices=[(0, 'Autodetect'), (1, 'Cisco IOS'), (2, 'Cisco XR'), (3, 'Cisco XE'), (4, 'Cisco NXOS'), (6, 'Cisco ASA')], default=0),
        ),
        migrations.AlterField(
            model_name='device',
            name='hostname',
            field=models.CharField(error_messages={'blank': 'IP / DNS name field is mandatory.', 'invalid': 'Enter a valid IP address or DNS resolvable hostname. It must contain 4 to 32 digits, letters and special characters -, _, . or spaces.', 'null': 'IP / DNS name field is mandatory.'}, max_length=32, unique=True, validators=[inventory.validators.HostnameValueValidator()]),
        ),
        migrations.AlterField(
            model_name='device',
            name='https_port',
            field=models.IntegerField(default=443),
        ),
        migrations.AlterField(
            model_name='device',
            name='ico',
            field=models.IntegerField(choices=[(0, 'static/ico/model/device/switch.svg'), (1, 'static/ico/model/device/border_router.svg'), (2, 'static/ico/model/device/chassis.svg'), (3, 'static/ico/model/device/console.svg'), (4, 'static/ico/model/device/firewall.svg'), (5, 'static/ico/model/device/router.svg'), (6, 'static/ico/model/device/router_firewall.svg'), (7, 'static/ico/model/device/router_wifi_1.svg'), (8, 'static/ico/model/device/router_wifi_2.svg'), (9, 'static/ico/model/device/stack.svg'), (10, 'static/ico/model/device/stack_firewall_1.svg'), (11, 'static/ico/model/device/stack_firewall_2.svg'), (12, 'static/ico/model/device/switch.svg'), (13, 'static/ico/model/device/wifi-connection.svg'), (14, 'static/ico/model/device/wireless-router.svg')], default=0),
        ),
        migrations.AlterField(
            model_name='device',
            name='name',
            field=models.CharField(error_messages={'blank': 'Name field is mandatory.', 'invalid': 'Enter the correct name value. It must contain 4 to 32 digits, letters and special characters -, _ or spaces.', 'null': 'Name field is mandatory.'}, max_length=32, unique=True, validators=[inventory.validators.NameValueValidator()]),
        ),
        migrations.AlterField(
            model_name='device',
            name='secret',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='ssh_port',
            field=models.IntegerField(default=22),
        ),
        migrations.AlterField(
            model_name='device',
            name='token',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='description',
            field=models.CharField(default='Credentials description.', error_messages={'invalid': 'Enter the correct description value. It must contain 8 to 256 digits, letters and special characters -, _, . or spaces.'}, max_length=256, validators=[inventory.validators.DescriptionValueValidator()]),
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(error_messages={'blank': 'Name field is mandatory.', 'invalid': 'Enter the correct name value. It must contain 4 to 32 digits, letters and special characters -, _ or spaces.', 'null': 'Name field is mandatory.'}, max_length=32, unique=True, validators=[inventory.validators.NameValueValidator()]),
        ),
    ]
