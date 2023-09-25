# Generated by Django 4.2.5 on 2023-09-20 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('short_desc', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('stock', models.IntegerField(default=20)),
            ],
        ),
    ]