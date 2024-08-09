# Generated by Django 5.0.6 on 2024-06-19 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('time_stamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]
