# Generated by Django 3.2.5 on 2023-04-26 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='make_trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('giver_name', models.CharField(max_length=20)),
                ('start', models.CharField(max_length=20)),
                ('destination', models.CharField(max_length=20)),
                ('time', models.CharField(max_length=20)),
                ('date', models.CharField(max_length=20)),
                ('veh_model', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=20)),
                ('seat', models.CharField(max_length=20)),
            ],
        ),
    ]