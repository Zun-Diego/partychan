# Generated by Django 4.1.4 on 2023-12-19 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_reportes_user_report'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportes',
            name='user_report',
        ),
    ]
