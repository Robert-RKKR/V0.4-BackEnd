# Generated by Django 3.2.9 on 2022-01-14 17:02

from django.db import migrations, models
import django.db.models.deletion
import main.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceTypeTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('root', models.BooleanField(default=False)),
                ('deleted', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(error_messages={'blank': 'Name field is mandatory.', 'invalid': 'Enter the correct name value. It must contain 4 to 32 digits, letters and special characters -, _ or spaces.', 'null': 'Name field is mandatory.', 'unique': 'Device with this name already exists.'}, max_length=32, unique=True, validators=[main.validators.NameValueValidator()])),
                ('description', models.CharField(default='ModelBase description.', error_messages={'invalid': 'Enter the correct description value. It must contain 8 to 256 digits, letters and special characters -, _, . or spaces.'}, max_length=256, validators=[main.validators.DescriptionValueValidator()])),
                ('device_type', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='inventory.devicetype')),
            ],
            options={
                'permissions': [],
                'abstract': False,
                'default_permissions': ['read', 'read_write'],
            },
        ),
        migrations.CreateModel(
            name='FsmTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('root', models.BooleanField(default=False)),
                ('deleted', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(error_messages={'blank': 'Name field is mandatory.', 'invalid': 'Enter the correct name value. It must contain 4 to 32 digits, letters and special characters -, _ or spaces.', 'null': 'Name field is mandatory.', 'unique': 'Device with this name already exists.'}, max_length=32, unique=True, validators=[main.validators.NameValueValidator()])),
                ('description', models.CharField(default='ModelBase description.', error_messages={'invalid': 'Enter the correct description value. It must contain 8 to 256 digits, letters and special characters -, _, . or spaces.'}, max_length=256, validators=[main.validators.DescriptionValueValidator()])),
                ('command', models.CharField(max_length=128)),
                ('sfm_expression', models.TextField()),
                ('device_data', models.BooleanField(default=False)),
                ('device_interface', models.BooleanField(default=False)),
                ('device_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='automation.devicetypetemplate')),
            ],
            options={
                'permissions': [],
                'abstract': False,
                'default_permissions': ['read', 'read_write'],
            },
        ),
    ]
