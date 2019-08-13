# Generated by Django 2.2.1 on 2019-08-12 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssignLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=250)),
                ('link_id', models.CharField(max_length=250)),
                ('allowed', models.IntegerField()),
                ('date', models.CharField(max_length=250)),
                ('left', models.IntegerField(default=0)),
                ('used', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Lawyer',
            fields=[
                ('bar_card', models.CharField(max_length=120, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('full_name', models.CharField(max_length=120)),
                ('status', models.CharField(blank=True, max_length=120, null=True)),
                ('company', models.CharField(blank=True, max_length=120, null=True)),
                ('practice_areas', models.CharField(blank=True, max_length=480, null=True)),
                ('address', models.CharField(max_length=120)),
                ('practice_location', models.CharField(blank=True, max_length=120, null=True)),
                ('gmaps_img', models.CharField(blank=True, max_length=2000, null=True)),
                ('profile_img', models.CharField(blank=True, max_length=2000, null=True)),
                ('license_date', models.CharField(blank=True, max_length=60, null=True)),
                ('statutory_profile_date', models.CharField(blank=True, max_length=60, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SeenDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assign_links_id', models.CharField(max_length=20)),
                ('ip', models.CharField(max_length=20)),
                ('time', models.CharField(max_length=500)),
                ('date', models.CharField(max_length=500)),
                ('url_seen', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_update', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appellate_court', models.CharField(blank=True, max_length=480, null=True)),
                ('coa_case_number', models.CharField(blank=True, max_length=480, null=True)),
                ('case_number', models.CharField(blank=True, max_length=480, null=True)),
                ('case_type', models.CharField(blank=True, max_length=480, null=True)),
                ('date_filed', models.CharField(blank=True, max_length=480, null=True)),
                ('style', models.CharField(blank=True, max_length=480, null=True)),
                ('trial_court', models.CharField(blank=True, max_length=480, null=True)),
                ('trial_court_case_number', models.CharField(blank=True, max_length=480, null=True)),
                ('trial_court_county', models.CharField(blank=True, max_length=480, null=True)),
                ('v', models.CharField(blank=True, max_length=480, null=True)),
                ('case_events', models.TextField(blank=True, null=True)),
                ('trial_court_information', models.TextField(blank=True, null=True)),
                ('parties', models.TextField(blank=True, null=True)),
                ('calendars', models.TextField(blank=True, null=True)),
                ('appellate_briefs', models.TextField(blank=True, null=True)),
                ('lawyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lawyers.Lawyer')),
            ],
        ),
    ]
