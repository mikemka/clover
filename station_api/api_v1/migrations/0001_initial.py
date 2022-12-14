# Generated by Django 3.2 on 2022-11-25 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(default='GFDzzwshujIDEpBZ', max_length=16, unique=True, verbose_name='Код доступа')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='Название')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(default='GFDzzwshujIDEpBZ', max_length=16, unique=True, verbose_name='Код доступа')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='Название')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('status', models.IntegerField(choices=[(0, 'Closed'), (1, 'Closing'), (2, 'Opening'), (3, 'Opened')], default=0, verbose_name='Статус станции')),
                ('aruco_marker', models.IntegerField(verbose_name='ArUco marker ID')),
                ('charging', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api_v1.flight', verbose_name='На зарядке')),
            ],
            options={
                'verbose_name': 'зарядная станция',
                'verbose_name_plural': 'зарядные станции',
            },
        ),
    ]
