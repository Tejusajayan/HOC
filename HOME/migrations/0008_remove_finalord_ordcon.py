# Generated by Django 4.2.2 on 2023-06-06 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HOME', '0007_finalord_name_finalord_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='finalord',
            name='ordcon',
        ),
    ]