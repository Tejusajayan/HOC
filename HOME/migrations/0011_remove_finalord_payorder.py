# Generated by Django 4.2.2 on 2023-06-07 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HOME', '0010_finalord_payorder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='finalord',
            name='payorder',
        ),
    ]
