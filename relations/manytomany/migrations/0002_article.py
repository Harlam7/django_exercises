# Generated by Django 4.2.5 on 2023-09-19 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manytomany', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=100)),
                ('publications', models.ManyToManyField(to='manytomany.publication')),
            ],
        ),
    ]