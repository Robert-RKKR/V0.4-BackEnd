# Generated by Django 3.2.9 on 2022-01-14 18:02

from django.db import migrations, models
import django.utils.timezone
import main.validators


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='devicetypetemplate',
            name='value',
            field=models.CharField(default=django.utils.timezone.now, max_length=32, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fsmtemplate',
            name='value',
            field=models.CharField(default=django.utils.timezone.now, max_length=32, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='devicetypetemplate',
            name='name',
            field=models.CharField(error_messages={'blank': 'Name field is mandatory.', 'invalid': 'Enter the correct name value. It must contain 4 to 32 digits, letters and special characters -, _ or spaces.', 'null': 'Name field is mandatory.', 'unique': 'ModelBase with this name already exists.'}, max_length=32, unique=True, validators=[main.validators.NameValueValidator()]),
        ),
        migrations.AlterField(
            model_name='fsmtemplate',
            name='name',
            field=models.CharField(error_messages={'blank': 'Name field is mandatory.', 'invalid': 'Enter the correct name value. It must contain 4 to 32 digits, letters and special characters -, _ or spaces.', 'null': 'Name field is mandatory.', 'unique': 'ModelBase with this name already exists.'}, max_length=32, unique=True, validators=[main.validators.NameValueValidator()]),
        ),
    ]
