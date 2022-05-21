# Generated by Django 3.2.6 on 2022-05-21 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clases', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cuotas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tipo_de_tarifa', models.CharField(max_length=50, verbose_name='Tipo_de_tarifa')),
                ('numbre_de_la_tarifa', models.CharField(max_length=50, verbose_name='Tipo_de_tarifa')),
                ('session', models.IntegerField()),
                ('actividad', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='clases.clases', verbose_name='actividades para agregar para agregar')),
            ],
        ),
    ]