# Generated by Django 4.2.2 on 2023-06-06 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HOME', '0006_alter_dinereq_number_alter_dinereq_seat'),
    ]

    operations = [
        migrations.AddField(
            model_name='finalord',
            name='name',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='finalord',
            name='number',
            field=models.PositiveBigIntegerField(default=1),
            preserve_default=False,
        ),
    ]
