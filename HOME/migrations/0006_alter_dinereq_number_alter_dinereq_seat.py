# Generated by Django 4.2.2 on 2023-06-06 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HOME', '0005_alter_dinereq_seat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dinereq',
            name='number',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='dinereq',
            name='seat',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
