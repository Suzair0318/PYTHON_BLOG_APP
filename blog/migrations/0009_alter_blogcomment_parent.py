# Generated by Django 5.0.6 on 2024-06-22 22:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_blogcomment_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='parent',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='blog.blogcomment'),
        ),
    ]
