# Generated by Django 5.0.2 on 2024-04-02 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0004_delete_movie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=5000)),
                ('director', models.CharField(max_length=200)),
                ('cast', models.CharField(max_length=700)),
                ('genre', models.CharField(max_length=200)),
                ('rating', models.CharField(max_length=10)),
                ('release_date', models.DateField()),
                ('poster', models.ImageField(upload_to='movies_poster')),
            ],
        ),
    ]
