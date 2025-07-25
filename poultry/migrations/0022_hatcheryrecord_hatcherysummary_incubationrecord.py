# Generated by Django 5.1.2 on 2024-11-02 08:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poultry', '0021_individualvaccination'),
    ]

    operations = [
        migrations.CreateModel(
            name='HatcheryRecord',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('breed_of_chicken', models.CharField(max_length=100)),
                ('number_of_eggs_set', models.PositiveIntegerField()),
                ('date_of_set', models.DateField()),
                ('hour_of_set', models.TimeField()),
                ('date_of_candling', models.DateField(blank=True, null=True)),
                ('date_of_transfer', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HatcherySummary',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('chicken_breed', models.CharField(max_length=100)),
                ('number_set', models.PositiveIntegerField()),
                ('total_infertile_eggs', models.PositiveIntegerField()),
                ('total_hatched', models.PositiveIntegerField()),
                ('hatch_percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('infertile_percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('place_of_distribution', models.CharField(blank=True, max_length=200, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('hatchery_record', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='summary', to='poultry.hatcheryrecord')),
            ],
        ),
        migrations.CreateModel(
            name='IncubationRecord',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('day', models.PositiveIntegerField()),
                ('incubation_set_temperature', models.DecimalField(decimal_places=2, max_digits=5)),
                ('egg_shell_temp_min', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('egg_shell_temp_med', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('egg_shell_temp_max', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('humidity_percentage', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('co2_level', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('valve_status', models.CharField(blank=True, max_length=50, null=True)),
                ('turning', models.CharField(blank=True, max_length=50, null=True)),
                ('date', models.DateField()),
                ('hatchery_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incubation_records', to='poultry.hatcheryrecord')),
            ],
        ),
    ]
