# Generated by Django 3.1.7 on 2021-09-04 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uncaged_app', '0002_auto_20210826_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='filmography',
            name='imdb_id',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='filmography',
            name='imdb_rating',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='filmography',
            name='page_link',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='filmography',
            name='plot',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='filmography',
            name='runtime',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='filmography',
            name='uncaged_rating',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='filmography',
            name='likes',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='filmography',
            name='role',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='filmography',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='filmography',
            name='year',
            field=models.SmallIntegerField(null=True),
        ),
    ]
