# Generated by Django 3.1.4 on 2020-12-09 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parking',
            name='address',
            field=models.CharField(default=None, max_length=150),
            preserve_default=False,
        ),
    ]
