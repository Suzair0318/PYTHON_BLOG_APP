# Generated by Django 5.0.6 on 2024-06-19 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0002_delete_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=12)),
                ('complain', models.TextField()),
            ],
        ),
    ]
