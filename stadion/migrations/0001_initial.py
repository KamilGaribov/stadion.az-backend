# Generated by Django 3.0.2 on 2020-01-31 13:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Stadion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
                ('city', models.CharField(max_length=63)),
                ('district', models.CharField(blank=True, max_length=63, null=True)),
                ('metro', models.CharField(blank=True, max_length=63, null=True)),
                ('adress', models.CharField(blank=True, max_length=63, null=True)),
                ('floor', models.CharField(choices=[('ot', 'ot'), ('rezin', 'rezin'), ('xalca', 'xalca')], max_length=7)),
                ('size', models.CharField(choices=[('5vs5', '5vs5'), ('6vs6', '6vs6'), ('7vs7', '7vs7'), ('11vs11', '11vs11')], max_length=7)),
                ('price', models.IntegerField()),
                ('cover', models.BooleanField(default=False)),
                ('cafe', models.BooleanField(default=False)),
                ('park', models.BooleanField(default=False)),
                ('video', models.BooleanField(default=False)),
                ('ordered', models.PositiveIntegerField(default=0)),
                ('star', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Stadion',
                'verbose_name_plural': 'Stadionlar',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
                ('bio', models.TextField(blank=True, null=True)),
                ('city', models.CharField(max_length=63)),
                ('played', models.PositiveIntegerField(default=0)),
                ('win', models.PositiveIntegerField(default=0)),
                ('draw', models.PositiveIntegerField(default=0)),
                ('lose', models.PositiveIntegerField(default=0)),
                ('player', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StadionImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='stadion/')),
                ('stadion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stadion.Stadion')),
            ],
        ),
        migrations.CreateModel(
            name='StadionFeedBack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('comment', models.TextField(blank=True, null=True)),
                ('stadion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stadion.Stadion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Hour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('mon', 'mon'), ('tue', 'tue'), ('wed', 'wed'), ('thu', 'thu'), ('fri', 'fri'), ('sat', 'sat'), ('sun', 'sun')], max_length=7)),
                ('nine', models.BooleanField(default=False)),
                ('ten', models.BooleanField(default=False)),
                ('eleven', models.BooleanField(default=False)),
                ('twelve', models.BooleanField(default=False)),
                ('stadion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stadion.Stadion')),
            ],
        ),
    ]
