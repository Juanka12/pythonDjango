# Generated by Django 4.1.3 on 2022-12-01 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('equipo', models.CharField(max_length=30)),
                ('nacionalidad', models.CharField(max_length=30)),
                ('edad', models.IntegerField(max_length=2)),
                ('posicion', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Seleccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('continente', models.CharField(max_length=30)),
                ('mundiales_ganados', models.IntegerField(max_length=3)),
            ],
        ),
    ]
