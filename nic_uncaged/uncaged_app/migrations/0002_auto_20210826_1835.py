# Generated by Django 3.1.7 on 2021-08-26 22:35

from django.db import migrations



# def seed_db(apps, schema_editor):


class Migration(migrations.Migration):

    dependencies = [
        ('uncaged_app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_db)
    ]