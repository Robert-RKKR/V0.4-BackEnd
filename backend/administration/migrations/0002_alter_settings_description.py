# Generated by Django 3.2.9 on 2022-01-14 15:39

from django.db import migrations, models
import main.validators


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='description',
            field=models.CharField(default='ModelBase description.', error_messages={'invalid': 'Enter the correct description value. It must contain 8 to 256 digits, letters and special characters -, _, . or spaces.'}, max_length=256, validators=[main.validators.DescriptionValueValidator()]),
        ),
    ]
