# Generated by Django 3.0.8 on 2020-09-18 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]
