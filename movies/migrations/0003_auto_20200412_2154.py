# Generated by Django 3.0.4 on 2020-04-12 21:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20200412_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(10)]),
        ),
    ]
