# Generated by Django 4.2.2 on 2023-06-06 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HOME', '0002_food_cate'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='name',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
