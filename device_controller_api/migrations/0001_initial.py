# Generated by Django 2.2.2 on 2019-08-18 15:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RemoteGPIOController',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('hostname', models.CharField(max_length=50)),
                ('port', models.IntegerField()),
                ('controller_type', models.CharField(
                    choices=[('PI', 'Raspberry Pi Controller (pigpio)'), ('AR', 'Arduino Controller'),
                             ('FA', 'Fake Controller')], default='PI', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='WirelessTransmitter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('pin', models.IntegerField()),
                ('controller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                                 to='device_controller_api.RemoteGPIOController')),
            ],
        ),
        migrations.CreateModel(
            name='RemoteSocket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('group', models.CharField(max_length=50)),
                ('device', models.CharField(max_length=50)),
                ('repeats', models.IntegerField()),
                ('transmitter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                                  to='device_controller_api.WirelessTransmitter')),
            ],
        ),
        migrations.CreateModel(
            name='LEDStrip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('red_pin', models.IntegerField()),
                ('green_pin', models.IntegerField()),
                ('blue_pin', models.IntegerField()),
                ('controller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                                 to='device_controller_api.RemoteGPIOController')),
            ],
        ),
        migrations.CreateModel(
            name='AddressableLEDStrip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('led_count', models.IntegerField()),
                ('spi_device', models.IntegerField()),
                (
                'controller_type', models.CharField(choices=[('WS', 'WS2801 Controller')], default='WS', max_length=2)),
                ('controller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                                 to='device_controller_api.RemoteGPIOController')),
            ],
        ),
    ]
