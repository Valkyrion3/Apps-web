# Generated by Django 4.2.11 on 2024-05-28 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='numeros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num1', models.FloatField()),
                ('num2', models.FloatField()),
                ('num3', models.FloatField()),
            ],
        ),
    ]
