# Generated by Django 4.2.16 on 2024-09-24 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poultry', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='breed',
            old_name='breed_name',
            new_name='name',
        ),
    ]
