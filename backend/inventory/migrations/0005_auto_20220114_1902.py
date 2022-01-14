# Generated by Django 3.2.9 on 2022-01-14 18:02

from django.db import migrations, models
import main.validators


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20220114_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='name',
            field=models.CharField(error_messages={'blank': 'Name field is mandatory.', 'invalid': 'Enter the correct name value. It must contain 4 to 32 digits, letters and special characters -, _ or spaces.', 'null': 'Name field is mandatory.', 'unique': 'ModelBase with this name already exists.'}, max_length=32, unique=True, validators=[main.validators.NameValueValidator()]),
        ),
        migrations.AlterField(
            model_name='credential',
            name='name',
            field=models.CharField(error_messages={'blank': 'Name field is mandatory.', 'invalid': 'Enter the correct name value. It must contain 4 to 32 digits, letters and special characters -, _ or spaces.', 'null': 'Name field is mandatory.', 'unique': 'ModelBase with this name already exists.'}, max_length=32, unique=True, validators=[main.validators.NameValueValidator()]),
        ),
        migrations.AlterField(
            model_name='device',
            name='name',
            field=models.CharField(error_messages={'blank': 'Name field is mandatory.', 'invalid': 'Enter the correct name value. It must contain 4 to 32 digits, letters and special characters -, _ or spaces.', 'null': 'Name field is mandatory.', 'unique': 'ModelBase with this name already exists.'}, max_length=32, unique=True, validators=[main.validators.NameValueValidator()]),
        ),
        migrations.AlterField(
            model_name='devicetype',
            name='name',
            field=models.CharField(error_messages={'blank': 'Name field is mandatory.', 'invalid': 'Enter the correct name value. It must contain 4 to 32 digits, letters and special characters -, _ or spaces.', 'null': 'Name field is mandatory.', 'unique': 'ModelBase with this name already exists.'}, max_length=32, unique=True, validators=[main.validators.NameValueValidator()]),
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(error_messages={'blank': 'Name field is mandatory.', 'invalid': 'Enter the correct name value. It must contain 4 to 32 digits, letters and special characters -, _ or spaces.', 'null': 'Name field is mandatory.', 'unique': 'ModelBase with this name already exists.'}, max_length=32, unique=True, validators=[main.validators.NameValueValidator()]),
        ),
    ]