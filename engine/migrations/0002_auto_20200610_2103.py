# Generated by Django 3.0.6 on 2020-06-10 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longUrl', models.TextField()),
                ('shortUrl', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='ShortUrl',
        ),
    ]
