# Generated by Django 3.2.9 on 2022-01-16 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoggerData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('application', models.CharField(max_length=128)),
                ('severity', models.IntegerField(choices=[(1, 'DEBUG'), (2, 'INFO'), (3, 'WARNING'), (4, 'ERROR'), (5, 'CRITICAL')])),
                ('message', models.CharField(max_length=1024)),
                ('task_id', models.CharField(max_length=128, null=True)),
                ('system_message', models.BooleanField(default=False)),
                ('color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.color')),
                ('credential', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.credential')),
                ('device', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.device')),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.group')),
            ],
        ),
    ]
