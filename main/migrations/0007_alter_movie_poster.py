# Generated by Django 5.0.2 on 2024-04-02 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_movie_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.URLField(default=None, max_length=500, null=True),
        ),
    ]