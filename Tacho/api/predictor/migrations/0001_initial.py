# Generated by Django 3.1.3 on 2020-11-14 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Predictor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicial', models.DateField()),
                ('fecha_final', models.DateField()),
                ('resoluciontemporal', models.CharField(choices=[('d', 'Dia'), ('m', 'Mes'), ('s', 'Semana')], max_length=100)),
            ],
        ),
    ]
