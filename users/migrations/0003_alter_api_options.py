# Generated by Django 3.2.9 on 2022-01-03 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_api'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='api',
            options={'verbose_name_plural': 'API'},
        ),
    ]