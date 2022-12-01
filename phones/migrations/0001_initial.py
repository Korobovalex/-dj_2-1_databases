# Generated by Django 4.1.3 on 2022-12-01 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120)),
                ('price', models.DecimalField(decimal_places=1, max_digits=10)),
                ('image', models.ImageField(blank=True, upload_to='phones/%Y/%m/%d')),
                ('release_date', models.DateField(auto_now_add=True)),
                ('slug', models.SlugField(max_length=120, unique=True)),
            ],
        ),
    ]
