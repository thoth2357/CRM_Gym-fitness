# Generated by Django 3.2.6 on 2022-05-22 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='habitaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_de_la_habitacion', models.CharField(blank=True, max_length=50, null=True)),
                ('capacidad', models.IntegerField()),
            ],
        ),
    ]
