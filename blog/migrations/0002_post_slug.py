# Generated by Django 4.2.1 on 2023-05-17 09:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="slug",
            field=models.SlugField(default=0, max_length=200),
        ),
    ]
