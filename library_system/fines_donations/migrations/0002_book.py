# Generated by Django 4.2.16 on 2024-12-01 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fines_donations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('publication_year', models.IntegerField()),
                ('publisher', models.CharField(max_length=255)),
                ('bar_code', models.CharField(max_length=255)),
            ],
        ),
    ]
