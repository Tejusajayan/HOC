# Generated by Django 4.2.2 on 2023-06-07 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HOME', '0008_remove_finalord_ordcon'),
    ]

    operations = [
        migrations.AddField(
            model_name='finalord',
            name='paymentid',
            field=models.CharField(default='-'),
        ),
        migrations.AlterField(
            model_name='finalord',
            name='number',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]