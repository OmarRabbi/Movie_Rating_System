# Generated by Django 5.0.2 on 2024-04-02 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movie_id', models.AutoField(primary_key=True, serialize=False)),
                ('movie_name', models.CharField(max_length=200)),
                ('movie_description', models.TextField(max_length=5000)),
                ('movie_genre', models.CharField(max_length=200)),
                ('movie_grade', models.CharField(max_length=10)),
                ('movie_release_date', models.DateField()),
            ],
        ),
    ]
