# Generated by Django 5.0.6 on 2024-06-19 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='slug',
            field=models.SlugField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
