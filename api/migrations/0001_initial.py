# Generated by Django 5.0.7 on 2024-07-26 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filmes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('genero', models.CharField(max_length=255)),
                ('ano', models.CharField(max_length=255)),
                ('idioma', models.CharField(max_length=255)),
                ('classific', models.CharField(max_length=255)),
            ],
        ),
    ]
