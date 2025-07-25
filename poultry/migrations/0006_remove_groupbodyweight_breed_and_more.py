# Generated by Django 4.2.16 on 2024-09-26 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poultry', '0005_alter_groupbodyweight_id_alter_groupeggproduction_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupbodyweight',
            name='breed',
        ),
        migrations.RemoveField(
            model_name='groupbodyweight',
            name='date_of_hatch',
        ),
        migrations.RemoveField(
            model_name='groupbodyweight',
            name='female_count',
        ),
        migrations.RemoveField(
            model_name='groupbodyweight',
            name='house',
        ),
        migrations.RemoveField(
            model_name='groupbodyweight',
            name='male_count',
        ),
        migrations.RemoveField(
            model_name='groupbodyweight',
            name='point_of_lay_date',
        ),
        migrations.RemoveField(
            model_name='groupbodyweight',
            name='total_bird_count',
        ),
        migrations.RemoveField(
            model_name='groupeggproduction',
            name='breed',
        ),
        migrations.RemoveField(
            model_name='groupeggproduction',
            name='date_of_hatch',
        ),
        migrations.RemoveField(
            model_name='groupeggproduction',
            name='female_count',
        ),
        migrations.RemoveField(
            model_name='groupeggproduction',
            name='house',
        ),
        migrations.RemoveField(
            model_name='groupeggproduction',
            name='male_count',
        ),
        migrations.RemoveField(
            model_name='groupeggproduction',
            name='point_of_lay_date',
        ),
        migrations.RemoveField(
            model_name='groupeggproduction',
            name='total_bird_count',
        ),
        migrations.RemoveField(
            model_name='groupfeedwaterintake',
            name='breed',
        ),
        migrations.RemoveField(
            model_name='groupfeedwaterintake',
            name='female_count',
        ),
        migrations.RemoveField(
            model_name='groupfeedwaterintake',
            name='house',
        ),
        migrations.RemoveField(
            model_name='groupfeedwaterintake',
            name='male_count',
        ),
        migrations.RemoveField(
            model_name='groupfeedwaterintake',
            name='total_bird_count',
        ),
        migrations.CreateModel(
            name='ChickenGroup',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('date_of_hatch', models.DateField()),
                ('point_of_lay_date', models.DateField(blank=True, null=True)),
                ('female_count', models.IntegerField()),
                ('male_count', models.IntegerField()),
                ('total_bird_count', models.IntegerField()),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poultry.breed')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poultry.house')),
            ],
        ),
        migrations.AddField(
            model_name='groupbodyweight',
            name='chicken_group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='poultry.chickengroup'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='groupeggproduction',
            name='chicken_group',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='poultry.chickengroup'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='groupfeedwaterintake',
            name='chicken_group',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='poultry.chickengroup'),
            preserve_default=False,
        ),
    ]
