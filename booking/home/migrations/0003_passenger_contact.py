# Generated by Django 4.1.4 on 2023-04-23 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_s_flight_depart_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger_contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conutry_code', models.CharField(max_length=55)),
                ('mobile_no', models.CharField(max_length=11)),
                ('Email', models.EmailField(max_length=55)),
                ('travel_passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.travel_passenger')),
            ],
        ),
    ]
