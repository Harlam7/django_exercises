# Generated by Django 4.2.5 on 2023-09-15 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0002_comments_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='signature',
            field=models.CharField(default='Firma', max_length=100),
        ),
    ]
