# Generated by Django 4.1.3 on 2022-12-01 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='lte_exists',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
